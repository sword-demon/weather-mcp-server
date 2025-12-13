# weather-mcp-server

## 安装依赖

```bash
uv add "mcp[cli]" httpx
```

## 准备高德 KEY 以及高德 API

地理/逆地理编码文档地址: https://lbs.amap.com/api/webservice/guide/api/georegeo/

KEY 自己去申请即可

天气查询文档地址：https://lbs.amap.com/api/webservice/guide/api-advanced/weatherinfo

### 注意点

调用高德地图 API，返回的响应码`status`应该判断是否等于`"1"`字符串 1，而不是数字 1

## 调试自己的 mcp

```bash
# 在当前项目目录下
mcp dev main.py
```

会出现一个web 网页，可以连接上`mcp server`，进行测试`tools`

## 如何使用

### 1. 配置环境变量

首先复制 `.env.example` 文件为 `.env`:

```bash
cp .env.example .env
```

然后编辑 `.env` 文件，填入你的高德地图 API Key:

```env
# 高德地图 API 配置
AMAP_KEY=你的高德地图API_KEY
AMAP_HOST=https://restapi.amap.com
```

### 2. 安装依赖

```bash
uv sync
```

### 3. 在 Claude Desktop 中配置

编辑 Claude Desktop 的配置文件:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

添加以下配置:

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "/你的项目路径/weather-mcp-server",
        "run",
        "main.py"
      ]
    }
  }
}
```

注意: 将 `/你的项目路径/weather-mcp-server` 替换为你实际的项目路径。

### 4. 重启 Claude Desktop

保存配置文件后，重启 Claude Desktop 应用，MCP 服务器将自动加载。

### 5. 使用天气查询功能

在 Claude Desktop 中，你可以直接询问天气信息，例如:

- "北京的天气怎么样？"
- "查询上海今天的天气"
- "深圳现在天气如何？"

Claude 将自动调用 `query_weather` 工具来获取天气信息。

## 项目结构

```
weather-mcp-server/
├── main.py              # MCP 服务器主程序
├── pyproject.toml       # 项目依赖配置
├── .env                 # 环境变量配置（不上传 git）
├── .env.example         # 环境变量配置模板
├── uv.lock             # 依赖锁定文件
└── README.md           # 项目说明文档
```

## 工具说明

### query_weather

查询指定地区的天气情况。

**参数:**
- `address` (string): 地区名称，例如 "北京"、"上海"、"深圳" 等

**返回:**
- 天气信息的 JSON 数据，包括温度、天气状况、风向、湿度等信息