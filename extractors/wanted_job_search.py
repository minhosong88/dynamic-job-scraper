from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv
from extractors.job_data import JobData


class WantedJobSearch:

    def __init__(self):
        self.keywords = []

    def add_keyword(self, keyword):
        self.keywords.append(keyword.strip())

    def add_keywords_from_input(self, keyword):
        keywords = keyword.split(',')
        for keyword in keywords:
            self.add_keyword(keyword)

    def run_playwright(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(url)

            for i in range(5):
                time.sleep(1.5)
                page.keyboard.down("End")

            content = page.content()
            browser.close()
        return content

    def scrape_keyword(self, keyword):
        jobs_db = []
        url = f"https://www.wanted.co.kr/search?query={keyword}&tab=position"
        content = self.run_playwright(url)
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__REty8")
        for job in jobs:
            partial_link = job.find("a")["href"]
            link = f"https://www.wanted.co.kr{partial_link}"
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company_name = job.find(
                "span", class_="JobCard_companyName__N1YrF").text
            reward = job.find("span", class_="JobCard_reward__cNlG5").text
            job = JobData(title, company_name, reward, link).to_list()
            jobs_db.append(job)

        return jobs_db

    def extract_wanted_jobs(self, keyword):
        self.add_keywords_from_input(keyword)
        jobs_db = []
        for keyword in self.keywords:
            keyword_jobs = self.scrape_keyword(keyword)
            jobs_db.extend(keyword_jobs)
        return jobs_db

    def save_to_csv(self, keyword):
        self.add_keywords_from_input(keyword)
        for keyword in self.keywords:
            keyword_jobs = self.scrape_keyword(keyword)
            with open(f"wanted_{keyword}_jobs.csv", mode="w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Company", "Reward", "Link"])
                for job in keyword_jobs:
                    writer.writerow(job)
