# Wanted Job Search

This project provides a tool for scraping job listings from Wanted.co.kr based on specified keywords. It uses Playwright for web scraping and BeautifulSoup for parsing HTML content.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact Information](#contact-information)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/minhosong88/dynamic-scraper.git
    cd dynamic-scraper
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Add your keywords to `main.py` and run the script:

    ```python
    from wanted_job_search import WantedJobSearch

    if __name__ == "__main__":
        search = WantedJobSearch()

        # Add your keywords here
        # examples of keywords: flutter, nextjs, kotlin, python, etc.
        keywords = input("Enter keywords separated by commas: ").split(',')
        for keyword in keywords:
            search.add_keyword(keyword.strip())

        search.save_to_excel()
    ```

2. Run the script:

    ```bash
    python main.py
    ```

3. The job listings will be saved in CSV files named after each keyword.

## Project Structure
  wanted-job-search/
  ├── job_data.py
  ├── wanted_job_search.py
  ├── main.py
  ├── requirements.txt
  └── README.md
- `job_data.py`: Contains the `JobData` class which defines the structure of job data.
- `wanted_job_search.py`: Contains the `WantedJobSearch` class which handles the scraping logic.
- `main.py`: The main script to run the job search.
- `requirements.txt`: Lists the required packages.
- `README.md`: This readme file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact Information

For any questions or suggestions, feel free to contact:

- Name: [Minho Song]
- Email: [hominsong@naver.com]
- GitHub: [https://github.com/minhosong88/]
