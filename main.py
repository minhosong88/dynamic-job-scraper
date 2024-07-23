from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv


p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# time.sleep(3)

# page.click("button.Aside_searchButton__rajGo")

# time.sleep(3)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(3)

# page.keyboard.down("Enter")

# time.sleep(3)

# page.click("a#search_tab_position")

for i in range(5):
    time.sleep(3)
    page.keyboard.down("End")

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__REty8")

jobs_db = []

for job in jobs:
    url = job.find("a")["href"]
    link = f"https://www.wanted.co.kr{url}"
    title = job.find("strong", class_="JobCard_title__HBpZf").text
    company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
    reward = job.find("span", class_="JobCard_reward__cNlG5").text
    job = {
        "title": title,
        "company_name": company_name,
        "reward": reward,
        "link": link
    }
    jobs_db.append(job)

print(jobs_db)


file = open("jobs.csv", mode="w", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Reward", "Link"])
for job in jobs_db:
    writer.writerow(job.values())
