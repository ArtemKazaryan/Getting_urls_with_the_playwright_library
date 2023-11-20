import sqlite3
from typing import List, Any

from selenium import webdriver
from bs4 import BeautifulSoup
import time


def end_load(level_depth, load_pause, menu_url, div_tag_class, div_tag, a_tag_class, a_tag):
    import time
    from playwright.sync_api import sync_playwright
    from bs4 import BeautifulSoup

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(menu_url)
        for i in range(level_depth + 1):
            page.keyboard.press('End')
            time.sleep(load_pause)

    html = page.content()
    soup = BeautifulSoup(html, "html.parser")
    links0 = soup.find_all(div_tag, class_=div_tag_class)
    links = []
    for link0 in links0:
        links1 = link0.find_all(a_tag, class_=a_tag_class)
        for link1 in links1:
            links.insert(0, link1["href"])
        return links
#


# def end_load(level_depth, load_pause, menu_url, div_tag_class, div_tag, a_tag_class, a_tag):
#     import time
#     from playwright.sync_api import Playwright, sync_playwright, expect
#     from bs4 import BeautifulSoup
#
#     def run(playwright: Playwright) -> list[Any]:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto(menu_url)
#         for i in range(level_depth + 1):
#             page.keyboard.press('End')
#             time.sleep(load_pause)
#         html = page.content()
#         soup = BeautifulSoup(html, "html.parser")
#         links0 = soup.find_all(div_tag, class_=div_tag_class)
#         links = []
#         for link0 in links0:
#             links1 = link0.find_all(a_tag, class_=a_tag_class)
#             for link1 in links1:
#                 links.insert(0, link1["href"])
#             return links
#         context.close()
#         browser.close()
#
#     with sync_playwright() as playwright:
#         run(playwright)




    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=True)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto(menu_url)
    #     for i in range(level_depth + 1):
    #         page.keyboard.press('End')
    #         time.sleep(load_pause)
    #
    # html = page.content()
    # soup = BeautifulSoup(html, "html.parser")
    # links0 = soup.find_all(div_tag, class_=div_tag_class)
    # links = []
    # for link0 in links0:
    #     links1 = link0.find_all(a_tag, class_=a_tag_class)
    #     for link1 in links1:
    #         links.insert(0, link1["href"])
    #     return links





# import asyncio
# from playwright.async_api import async_playwright
# from bs4 import BeautifulSoup
# async def end_load(level_depth, load_pause, menu_url, div_tag_class, div_tag, a_tag_class, a_tag):
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch(headless=True)
#         context = await browser.newcontext()
#         page = await context.newpage()
#         await page.goto(menu_url)
#         # context.close()
#         # browser.close()
#         for i in range(level_depth + 1):
#             await page.keyboard.press('End')
#             # page.keyboard.press('End')
#             await asyncio.sleep(load_pause)
#             # time.sleep(load_pause)
#         html = await page.content()
#         # html = page.content()
#         soup = BeautifulSoup(html, "html.parser")
#         links0 = soup.findall(div_tag, class_=div_tag_class)
#         print(f'links0 ----------------------------{links0}')
#         links = []
#         for link0 in links0:
#             links1 = link0.findall(a_tag, class_=a_tag_class)
#             for link1 in links1:
#                 links.insert(0, link1["href"])
#             return links




def scroll_load(level_depth, load_pause, menu_url, div_tag_class, div_tag, a_tag_class, a_tag):
    driver = webdriver.Chrome()
    driver.get(menu_url)
    for i in range(level_depth + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(load_pause)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    links0 = soup.find_all(div_tag, class_=div_tag_class)

    driver.quit()

    links = []
    for link0 in links0:
        links1 = link0.find_all(a_tag, class_=a_tag_class)
        for link1 in links1:
            links.insert(0, link1["href"])

        return links


def create_tables_and_add_resources(db_name, resources):
    conn = sqlite3.connect(db_name)

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS resource(
        resource_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        resource_name TEXT,
        resource_url TEXT,
        top_tag TEXT,
        bottom_tag TEXT,
        title_cut TEXT,
        date_cut TEXT);
    """)
    conn.commit()

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        res_id INT,
        link TEXT,
        title TEXT,
        content TEXT,
        nd_date TEXT,
        s_date TEXT,
        not_date TEXT);
    """)
    conn.commit()

    cur.executemany("INSERT INTO resource(resource_name, resource_url, top_tag, bottom_tag, title_cut, date_cut)"
                    " VALUES(?, ?, ?, ?, ?, ?);", resources)
    conn.commit()
    conn.close()


def add_to_items(db_name, resource_id, link, title, content, nd_date, s_date, not_date):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    news_item_obj = (resource_id, link, title, content, nd_date, s_date, not_date)
    cur.execute("INSERT INTO items(res_id, link, title, content, nd_date, s_date, not_date) VALUES(?, ?, ?, ?, ?, ?, ?);",
                news_item_obj)
    conn.commit()
    conn.close()

