from flask import Flask, render_template, request
from extractors.wwr import WWRJobSearch
from extractors.wanted_job_search import WantedJobSearch

app = Flask("JobScraper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    wanted = WantedJobSearch().extract_wanted_jobs(keyword)
    wwr = WWRJobSearch().extract_wwr_jobs_keyword(keyword)
    jobs = wanted + wwr

    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run(host='0.0.0.0', port=8080, debug=True)


# if __name__ == "__main__":
#     search = WantedJobSearch()

#     # Add your keywords here
#     # examples of keywords: flutter, nextjs, kotlin, python, etc.
#     keywords = input("Enter keywords separated by commas: ").split(',')
#     for keyword in keywords:
#         search.add_keyword(keyword.strip())

#     search.save_to_excel()
