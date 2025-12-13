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