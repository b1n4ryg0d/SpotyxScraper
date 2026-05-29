import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup
from pydantic import HttpUrl

async def scraper(url: HttpUrl, search_data: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                results = soup.find_all(class_=search_data)
                return results
            else:
                return f"err: {response.status}"