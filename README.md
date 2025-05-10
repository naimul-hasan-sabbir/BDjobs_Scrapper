# BDjobs Scrapper

A Python project to scrape job listings from [bdjobs.com](https://www.bdjobs.com/) using Selenium. The script extracts job titles and company names from the Hot Jobs section and saves them to a text file.

## Features

- Uses Selenium with ChromeDriver (managed by webdriver-manager)
- Scrapes job title and company name from bdjobs.com
- Handles pagination with concurrency for faster scraping
- Outputs results to `output/jobs.txt`

## Requirements

- Python 3.8+
- Google Chrome browser

## Project Structure

```
BDjobs_scrapper/
├── main.py                # Main entry point of the application
├── scraper/               # Web scraping logic
│   ├── __init__.py
│   ├── bdjobs.py          # Main scraping functions
│   └── parser.py          # (For future use) HTML parsing helpers
├── utils/                 # Utility functions and file handling
│   ├── __init__.py
│   ├── file_handler.py    # File read/write operations
│   └── helpers.py         # Utility/helper functions
├── config/                # Configuration settings
│   ├── __init__.py
│   └── settings.py        # Scraper configuration
output/
└── jobs.txt               # Output file for scraped job listings
Pipfile                    # Dependency management
Pipfile.lock               # Locked dependency versions
README.md                  # Project documentation
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/BDjobs_Scrapper.git
   cd BDjobs_Scrapper
   ```
2. **Install dependencies:**
   ```sh
   pipenv install
   ```
   Or, if you use pip:
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the scraper:**
   ```sh
   pipenv run python main.py
   ```
   Or, if using pip:
   ```sh
   python main.py
   ```

## Output Example

Below is a sample of the output generated in `output/jobs.txt`:

```
Title: Manager-Hospital
Company: Ad-din Foundation
Location:
Posted on:

Title: Senior UI/UX Designer
Company: BYSL Global Technology Group
Location:
Posted on:

Title: Officer-Brand
Company: Kohinoor Chemical Co. (BD) Ltd.
Location:
Posted on:

Title: Management Trainee
Company: Mutual Trust Bank PLC
Location:
Posted on:

Title: Executive - Manufacturing Pl...
Company: A Well-Reputed Top-Ranking Pharmaceutical Company
Location:
Posted on:

... (more jobs)
```

## Notes

- The script uses Selenium and webdriver-manager to automatically handle ChromeDriver installation.
- Make sure you have Google Chrome installed and up to date.
- If you want to run the scraper in headless mode, uncomment the `headless` option in `bdjobs.py`.

## License

MIT
