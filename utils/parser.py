import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup
from pydantic import HttpUrl

async def scraper(url: HttpUrl):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            return resp