from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time


p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(3)

page.click("button.Aside_searchButton__rajGo")

time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(3)

page.keyboard.down("Enter")

time.sleep(3)

page.click("a#search_tab_position")

for i in range(5):
    time.sleep(3)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")
