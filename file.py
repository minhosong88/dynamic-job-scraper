import csv
from io import BytesIO, TextIOWrapper


def save_to_file(keyword, jobs=[]):
    file_path = f"{keyword}_jobs.csv"
    try:
        with open(f"{file_path}", mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Company", "Link"])
            for job in jobs:
                writer.writerow(job)
    except IOError as e:
        print(f"Error writing to file {keyword}_jobs.csv: {e}")
    return file_path


def save_file_to_memory(keyword, jobs=[]):
    output = BytesIO()
    wrapper = TextIOWrapper(output, encoding='utf-8', newline="")
    writer = csv.writer(wrapper)
    writer.writerow(["Title", "Company", "Link"])
    for job in jobs:
        writer.writerow(job)
    wrapper.flush()
    output.seek(0)
    wrapper.detach()
    return output
