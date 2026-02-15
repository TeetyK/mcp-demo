from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
import dotenv
dotenv.load_dotenv("F:\\mcp-demo\\.env")
mcp = FastMCP("mcp-product")

api_base = os.environ["API_base"]
@mcp.tool()
async def search_data(title: str) -> Any:
    """Function Search data for mcp-product etc. blog มีรายการอะไรบ้าง"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{api_base}?title={title}")
        return response.json()
    
@mcp.tool()
async def add_data(title: str, body: str) -> Any:
    """Function add data for mcp-product etc. เพิ่มข้อมูล {title} ที่มี {body} เข้าไปหน่อย """
    async with httpx.AsyncClient() as client:
        response = await client.post(api_base, json={'title': title, 'body': body})
        return response.json()['id']

@mcp.tool()
async def get_data() -> Any:
    """Function get data for mcp-product etc. แสดงข้อมูฃทั้งหมดให้หน่อย all data"""
    async with httpx.AsyncClient() as client:
        response = await client.get(api_base)
        return response.json()

if __name__ == "__main__":
    mcp.run(transport='stdio')    
