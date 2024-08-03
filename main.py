from flask import Flask, redirect, render_template, request, url_for
from extractors.wwr import WWRJobSearch
from extractors.wanted_job_search import WantedJobSearch
from file import save_to_file

app = Flask("JobScraper")


@app.route("/")
def home():
    return render_template("home.html")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    else:
        keywords = keyword.split(",")
        formatted_keywords = ", ".join(
            [keyword.strip() for keyword in keywords])
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


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    error_message = request.args.get("error")
    success_message = request.args.get("success")
    selected_jobs = []

    if keyword:
        keyword = keyword.strip()
        if keyword in db:
            selected_jobs = db[keyword]
        else:
            return redirect(f"/search?keyword={keyword}")
    else:
        return render_template("export.html", db=db, selected_keyword=None, jobs=[])

    return render_template("export.html", db=db, selected_keyword=keyword, jobs=selected_jobs, error=error_message, success=success_message)


@app.route("/save")
def save():
    keyword = request.args.get("keyword")
    if not keyword or keyword == "":
        error_message = f"No Keyword Provided."
        return redirect(url_for("export", error=error_message))
    keyword = keyword.strip()
    if keyword in db:
        all_jobs = db[keyword]
    else:
        error_message = f"{keyword} Not In Database."
        return redirect(url_for("export", error=error_message))

    save_to_file(keyword, jobs=all_jobs)
    success_message = f"{keyword} Jobs have been saved to {keyword}_jobs.csv"
    return redirect(url_for("export", success=success_message))


app.run(host='0.0.0.0', port=8080, debug=True)


# if __name__ == "__main__":
#     search = WantedJobSearch()

#     # Add your keywords here
#     # examples of keywords: flutter, nextjs, kotlin, python, etc.
#     keywords = input("Enter keywords separated by commas: ").split(',')
#     for keyword in keywords:
#         search.add_keyword(keyword.strip())

#     search.save_to_excel()
