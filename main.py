# filepath: BDjobs_scrapper/main.py

import sys
from BDjobs_scrapper.scraper.bdjobs import scrape_bdjobs
from BDjobs_scrapper.utils.file_handler import write_jobs_to_file

def main():
    try:
        jobs = scrape_bdjobs()
        write_jobs_to_file(jobs, 'output/jobs.txt')
        print(f"Successfully saved {len(jobs)} job listings to output/jobs.txt")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()