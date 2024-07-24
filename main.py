from wanted_job_search import WantedJobSearch

if __name__ == "__main__":
    search = WantedJobSearch()
    search.add_keyword("flutter")
    search.add_keyword("nextjs")
    search.add_keyword("kotlin")

    search.save_to_excel()
