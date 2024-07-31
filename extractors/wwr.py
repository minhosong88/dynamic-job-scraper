import requests
import csv
from bs4 import BeautifulSoup
from extractors.job_data_wwr import JobDataWWR


class WWRJobSearch:

    def __init__(self):
        self.keywords = []

    def add_keyword(self, keyword):
        self.keywords.append(keyword.strip())

    def add_keywords_from_input(self, keyword):
        keywords = keyword.split(',')
        for keyword in keywords:
            self.add_keyword(keyword)

    def scrape_page(self, url):
        all_jobs = []
        response = requests.get(url)
        soup = BeautifulSoup(
            response.content,
            "html.parser",
        )
        jobs = soup.find("section", class_="jobs",).find_all("li")[1:-1]
        for job in jobs:
            # There are jobs that do not contain region information
            try:
                title = job.find("span", class_="title").text
                company, position, region = job.find_all(
                    "span", class_="company")
                url = job.find(
                    "div", class_="tooltip--flag-logo").next_sibling["href"]
                company = company.text
                position = position.text
                region = region.text
            except ValueError:
                try:
                    title = job.find("span", class_="title").text
                    company, position = job.find_all("span", class_="company")
                    url = job.find(
                        "div", class_="tooltip--flag-logo").next_sibling["href"]
                    company = company.text
                    position = position.text
                    region = "Not provided"
                except ValueError:
                    continue
            job_data = JobDataWWR(
                title, company, position, region, url).to_list()
            all_jobs.append(job_data)
        return all_jobs

    def keyword_serch(self, keyword):
        base_url = "https://weworkremotely.com/remote-jobs/search?&term="
        response = requests.get(f"{base_url}{keyword}")
        if response.status_code != 200:
            print("Can't request website")
            return []

        all_jobs = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs_sections = soup.find_all("section", class_="jobs")
        jobs = [
            job for jobs_section in jobs_sections for job in jobs_section.find_all("li")]
        filtered_jobs = [
            job for job in jobs if "view_all" not in job.get("class", [])]

        for job in filtered_jobs:
            # There are jobs that do not contain region information
            try:
                title = job.find("span", class_="title").text
                company, position, region = job.find_all(
                    "span", class_="company")
                url = job.find(
                    "div", class_="tooltip--flag-logo").next_sibling["href"]
                company = company.text
                position = position.text
                region = region.text
            except ValueError:
                try:
                    title = job.find("span", class_="title").text
                    company, position = job.find_all(
                        "span", class_="company")
                    url = job.find(
                        "div", class_="tooltip--flag-logo").next_sibling["href"]
                    company = company.text
                    position = position.text
                    region = "Not provided"
                except ValueError:
                    continue
            job_data = JobDataWWR(
                title, company, position, region, url).to_list()
            all_jobs.append(job_data)
        return all_jobs

    def extract_wwr_jobs_keyword(self, keyword):
        self.add_keywords_from_input(keyword)
        jobs_db = []
        for keyword in self.keywords:
            keyword_jobs = self.keyword_serch(keyword)
            jobs_db.extend(keyword_jobs)
        return jobs_db

    def get_pages(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        num_of_pages = len(
            soup.find("div", class_="pagination").find_all("span", class_="page"))
        return num_of_pages

    def pages_save_to_csv(self):
        url = "https://weworkremotely.com/remote-full-time-jobs?page=1"
        num_of_pages = self.get_pages(url)
        with open(f"wwr_jobs.csv", mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Position", "Region", "Link"])
            for i in range(num_of_pages):
                url = f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}"
                jobs = self.scrape_page(url)
                for job in jobs:
                    writer.writerow(job)

    def keyword_search_save_to_csv(self, keyword):
        self.add_keywords_from_input(keyword)
        for keyword in self.keywords:
            keyword_jobs = self.keyword_serch(keyword)
            if not keyword_jobs:
                continue
            try:
                with open(f"wwr_{keyword}_jobs.csv", mode="w", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        ["Title", "Company", "Position", "Region", "Link"])
                    for job in keyword_jobs:
                        writer.writerow(job)
            except IOError as e:
                print(f"Error writing to CSV for keyword {keyword}: {e}")
