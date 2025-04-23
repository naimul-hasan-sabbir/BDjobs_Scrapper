# BDjobs Scraper

BDjobs Scraper is a Python application that automates the extraction of live IT job listings from the BDjobs website. The collected job data is saved in a structured text file for easy access and review.

## Features

- Scrapes live IT job listings from BDjobs.com
- Saves job data (title, company, location, date) to a text file
- Modular, maintainable, and extensible codebase
- Easy to configure and run

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

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/BDjobs_Scraper.git
   cd BDjobs_Scraper
   ```
2. Install dependencies using pipenv:
   ```sh
   pipenv install
   ```

## Usage

To run the scraper and save job listings to `output/jobs.txt`:

```sh
pipenv run python main.py
```

## Customization

- Update scraping logic in `scraper/bdjobs.py` if the BDjobs website structure changes.
- Adjust output formatting in `utils/file_handler.py` as needed.
- Modify configuration in `config/settings.py` for custom settings.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
