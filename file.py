import csv


def save_to_file(keyword, jobs=[]):
    try:
        with open(f"{keyword}_jobs.csv", mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Link"])
            for job in jobs:
                writer.writerow(job)
    except IOError as e:
        print(f"Error writing to file {keyword}_jobs.csv: {e}")
