from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
mcp = FastMCP("mcp-product")

api_base = os.environ["API_base"]

@mcp.tool()
async def get_data() -> Any:
    async with httpx.AsyncClient as client:
        response = await client.get(api_base)
        return response.json()

if __name__ == "__main__":
    mcp.run(transport='stdio')    
