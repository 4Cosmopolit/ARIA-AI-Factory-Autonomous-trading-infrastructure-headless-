"""
docs/examples/mcp-server-template.py — эталонный шаблон MCP-сервера ARIA AI‑Factory v13.01

Скопируйте этот файл и добавьте свою бизнес‑логику в функции инструментов.
"""

import asyncio
import json
import logging
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

# ---------------------------------------------------------------------------
# Логирование
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-template")

# ---------------------------------------------------------------------------
# Здесь регистрируются ваши инструменты.
# Каждый инструмент должен быть объявлен в list_tools и обработан в call_tool.
# ---------------------------------------------------------------------------
TOOLS = {
    "hello": {
        "description": "Say hello to someone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name to greet"}
            },
            "required": ["name"]
        }
    },
    "add": {
        "description": "Add two numbers",
        "inputSchema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    }
}

# ---------------------------------------------------------------------------
# Бизнес‑логика инструментов
# ---------------------------------------------------------------------------
async def handle_hello(name: str) -> str:
    logger.info(f"hello called with name={name}")
    return f"Hello, {name}! This is ARIA MCP server."

async def handle_add(a: float, b: float) -> float:
    logger.info(f"add called with a={a}, b={b}")
    return a + b

# ---------------------------------------------------------------------------
# Диспетчер вызовов
# ---------------------------------------------------------------------------
async def dispatch_tool(name: str, arguments: dict) -> types.TextContent:
    if name == "hello":
        result = await handle_hello(arguments["name"])
        return types.TextContent(type="text", text=str(result))
    elif name == "add":
        result = await handle_add(arguments["a"], arguments["b"])
        return types.TextContent(type="text", text=str(result))
    else:
        raise ValueError(f"Unknown tool: {name}")

# ---------------------------------------------------------------------------
# Инициализация и запуск сервера
# ---------------------------------------------------------------------------
async def main():
    server = Server("aria-mcp-template")

    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name=name,
                description=info["description"],
                inputSchema=info["inputSchema"]
            )
            for name, info in TOOLS.items()
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        try:
            result = await dispatch_tool(name, arguments)
            return [result]
        except Exception as e:
            logger.error(f"Tool {name} failed: {e}")
            return [types.TextContent(type="text", text=json.dumps({"error": str(e)}))]

    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="aria-mcp-template",
                server_version="13.01"
            ),
            notification_options=NotificationOptions(),
        )

if __name__ == "__main__":
    asyncio.run(main())
