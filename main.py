import json
import os
import httpx
from mcp.server import FastMCP
from mcp.types import TextContent
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

app = FastMCP("weather-mcp-server")

HOST = os.getenv("AMAP_HOST", "https://restapi.amap.com")
KEY = os.getenv("AMAP_KEY")


@app.tool(
    name="query_weather",
    description="查询指定地区的天气情况"
)
async def query_weather(address) -> list[TextContent] | None:
    """
    mcp 函数 query_weather
    调用高德地图 api 查询指定地区的天气情况
    :param address: 指定地区
    :return:
    """
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{HOST}/v3/geocode/geo", params={"key": KEY, "address": address})
            if resp.status_code != 200:
                """请求失败"""
                return [TextContent(type="text", text=f"request error-0 {resp.status_code} - {resp.content}")]
            resp_dict = json.loads(resp.text)
            if resp_dict["status"] != "1":
                """失败 这里要注意接口响应的 status 是 字符串 1，否则判断不成功"""
                return [TextContent(type="text", text=f"request error-1 {resp.status_code} - {resp_dict['info']}")]
            # 能正确得到数据了
            city = resp_dict["geocodes"][0]["adcode"]

            resp = await client.get(f"{HOST}/v3/weather/weatherInfo", params={"key": KEY, "city": city})
            if resp.status_code != 200:
                """请求失败"""
                return [TextContent(type="text", text=f"request error-2 {resp.status_code} - {resp.content}")]
            resp_dict = json.loads(resp.text)
            if resp_dict["status"] != "1":
                """失败  这里要注意接口响应的 status 是 字符串 1，否则判断不成功"""
                return [TextContent(type="text", text=f"request error-3 {resp.status_code} - {resp_dict['info']}")]

            return [TextContent(type="text", text=resp.text)]

        except Exception as e:
            raise e


def main():
    print("Hello from weather-mcp-server!")


if __name__ == "__main__":
    app.run(transport="stdio")
