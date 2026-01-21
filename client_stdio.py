# -*- coding: utf-8 -*-
"""
@File    : client_stdio.py
@Author  : wxvirus
@Time    : 2025/12/14 17:09
@Desc    : 
"""
import os

from mcp import ClientSession, StdioServerParameters
from openai import OpenAI
from dotenv import load_dotenv
from mcp.client.stdio import stdio_client

# 加载 .env 文件
load_dotenv()


class MCPClient:
    """
    MCP 客户端
    """

    def __init__(self):
        self.session: ClientSession = None
        self.openai = OpenAI(
            base_url="https://api.openai.com/v2",
            api_key="sk-1234"
        )
        self.model = "gpt-4o"

    async def connect_to_server(self):
        """建立连接"""
        server_params = StdioServerParameters(
            command="uv",
            args=[
                "--directory",
                "/Volumes/MOVESPEED/ai-coding/weather-mcp-server",
                "run",
                "main.py"
            ],
            env={
                "KEY": os.getenv("AMAP_KEY")
            }
        )
        stream_context = stdio_client(server_params)
        # with stdio_client() 就会触发 __aenter__()
        stream = await stream_context.__aenter__()

        session_context = ClientSession(*stream)
        self.session = await session_context.__aenter__()

        await self.session.initialize()
        print("session initialized stdio client!")

        response = await self.session.list_tools()
        tools = response.tools
        print(f"tools listed stdio client! with tools {tools}")
