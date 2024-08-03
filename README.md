# Dynamic Job Scraper: Automating Job Search with Efficiency

## Project Overview

Welcome to the **Dynamic Job Scraper** project! This tool is designed to streamline your job search by automatically extracting and compiling job listings from various online sources. Whether you are looking for remote opportunities or local positions, this scraper will save you time and effort by consolidating job data into easy-to-use CSV files.

## Features

- **Multiple Keyword Search**: Search for job listings using multiple keywords separated by commas.
- **Real-Time Scraping**: Scrape job listings from multiple sources in real-time.
- **Export to CSV**: Save search results as CSV files for easy sharing and analysis.
- **User-Friendly Interface**: Simple and clean web interface built with PicoCSS.
- **In-Memory File Handling**: Efficient in-memory file creation and handling.

## Project Structure
QuantumScraper/
│
├── extractors/
│ ├── job_data_wwr.py
│ ├── job_data.py
│ ├── wanted_job_search.py
│ └── wwr.py
│
├── templates/
│ ├── export.html
│ ├── home.html
│ └── search.html
│
├── file.py
├── main.py
├── requirements.txt
├── .gitignore
└── .gitattributes

### Extractors

- **`job_data_wwr.py`**: Defines the `JobDataWWR` class for managing job data sourced from We Work Remotely.
- **`job_data.py`**: Defines the `JobData` class for managing job data sourced from Wanted.
- **`wanted_job_search.py`**: Implements the scraping logic for the Wanted job site.
- **`wwr.py`**: Implements the scraping logic for the We Work Remotely job site.

### Templates

- **`export.html`**: Template for exporting job search results.
- **`home.html`**: Homepage template for the web interface.
- **`search.html`**: Template for displaying search results.

### Core Components

- **`file.py`**: Contains functions to save job data to files.
- **`main.py`**: The main application script that runs the Flask web server and handles routing.
- **`requirements.txt`**: Lists the required Python packages for the project.

### requirements.txt
Lists the required Python packages for the project:

``` makefile
beautifulsoup4==4.9.3
playwright==1.12.2
requests==2.25.1
```

## How It Works

### Classes and Functions

1. **JobDataWWR Class** (`job_data_wwr.py`)
   - **Attributes**: `title`, `company`, `position`, `region`, `link`
   - **Method**: `to_list` - Converts job attributes to a list format.

2. **JobData Class** (`job_data.py`)
   - **Attributes**: `title`, `company_name`, `reward`, `link`
   - **Method**: `to_list` - Converts job attributes to a list format.

3. **WantedJobSearch Class** (`wanted_job_search.py`)
   - Manages job searches on the Wanted job site using Playwright and BeautifulSoup.
   - **Methods**: `add_keyword`, `add_keywords_from_input`, `run_playwright`, `scrape_keyword`, `save_to_csv`

4. **WWRJobSearch Class** (`wwr.py`)
   - Manages job searches on the We Work Remotely job site using requests and BeautifulSoup.
   - **Methods**: `add_keyword`, `add_keywords_from_input`, `scrape_page`, `scrape_keyword`, `get_pages`, `pages_save_to_csv`, `keyword_search_save_to_csv`

### Flask Web Application

- The Flask app (`main.py`) serves as the web interface for the Dynamic Job Scraper.
- Users can perform job searches, view results, and export data to CSV files.
- 
## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/QuantumScraper.git
   cd QuantumScraper
   ```
2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ````
3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```
4. Install Playwright browsers:

    ```sh
    playwright install
    ```

### Usage

1. Start the Flask server:
    
    ```sh
    python main.py
    ```
2. Open your web browser and navigate to http://localhost:8080.

3. Use the home page to search for job listings by entering keywords separated by commas.

4. View and export the search results.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request. We appreciate your help in enhancing this project.


## Contact Information

For any questions, suggestions, or issues, please contact:

- **Name**: Minho Song
- **Email**: [hominsong@naver.com](mailto:hominsong@naver.com)
- **GitHub**: [minhosong88](https://github.com/minhosong88)
