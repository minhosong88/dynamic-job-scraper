from flask import Flask, render_template, request
from extractors.wwr import WWRJobSearch
from extractors.wanted_job_search import WantedJobSearch

app = Flask("JobScraper")


@app.route("/")
def home():
    return render_template("home.html")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    keywords = keyword.split(",")
    formatted_keywords = ", ".join([keyword.strip() for keyword in keywords])
    all_jobs = []
    for keyword in keywords:
        keyword = keyword.strip()
        if keyword in db:
            jobs = db[keyword]
        else:
            wanted = WantedJobSearch().scrape_keyword(keyword)
            wwr = WWRJobSearch().scrape_keyword(keyword)
            jobs = wanted + wwr
            db[keyword] = jobs
        all_jobs.extend(jobs)
    return render_template("search.html", keyword=formatted_keywords, jobs=all_jobs)


app.run(host='0.0.0.0', port=8080, debug=True)


# if __name__ == "__main__":
#     search = WantedJobSearch()

#     # Add your keywords here
#     # examples of keywords: flutter, nextjs, kotlin, python, etc.
#     keywords = input("Enter keywords separated by commas: ").split(',')
#     for keyword in keywords:
#         search.add_keyword(keyword.strip())

#     search.save_to_excel()
