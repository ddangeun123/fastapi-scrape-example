from fastapi import FastAPI
from selenium import webdriver
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import asyncio

app = FastAPI()
executor = ThreadPoolExecutor(max_workers=4)

def fetch(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return str(soup)

@app.get("/crawl/")
async def read_root(url: str):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, fetch, url)
    return {"html": result}