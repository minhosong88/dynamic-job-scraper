import requests
from bs4 import BeautifulSoup


all_jobs = []


def scrape_page(url):
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
            company, position, region = job.find_all("span", class_="company")
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
        job_data = {
            "title": title,
            "company": company,
            "position": position,
            "region": region,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)


def get_pages(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    num_of_pages = len(
        soup.find("div", class_="pagination").find_all("span", class_="page"))
    return num_of_pages


url = "https://weworkremotely.com/remote-full-time-jobs?page=1"
num_of_pages = get_pages(url)

for i in range(num_of_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}"
    scrape_page(url)
