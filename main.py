from wanted_job_search import WantedJobSearch

if __name__ == "__main__":
    search = WantedJobSearch()

    # Add your keywords here
    # examples of keywords: flutter, nextjs, kotlin, python, etc.
    keywords = input("Enter keywords separated by commas: ").split(',')
    for keyword in keywords:
        search.add_keyword(keyword.strip())

    search.save_to_excel()
