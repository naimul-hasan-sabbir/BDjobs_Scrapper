from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import time
import os

BASE_URL = "https://www.bdjobs.com/"

options = Options()
# options.add_argument('headless')  # Uncomment to run headless
options.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def navigate_to_website(url):
    driver.get(url)

def extract_job_data():
    try:
        job_listings = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "c-card")]'))
        )
        jobs = []
        for job_listing in job_listings:
            try:
                company_elem = job_listing.find_element(By.XPATH, './/div[@class="companyDetails"]/h3')
                company_name = company_elem.text.strip()
                job_link_elem = job_listing.find_element(By.XPATH, './/div[@class="companyDetails"]/ul/li/a')
                job_title = job_link_elem.text.strip()
                job_link = job_link_elem.get_attribute('href')
                jobs.append({
                    'title': job_title,
                    'company': company_name,
                    'location': '',  # Not available in this block
                    'date_posted': '',  # Not available in this block
                    'link': job_link
                })
            except Exception as e:
                print(f"Error extracting job data: {e}")
        return jobs
    except Exception as e:
        print(f"Error extracting job data: {e}")
        return []

def navigate_to_pages(pagination_links):
    jobs = []
    for link in pagination_links:
        try:
            link.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="job-box"]'))
            )
            jobs.extend(extract_job_data())
        except Exception as e:
            print(f"Error navigating to page: {e}")
    return jobs

def get_pagination_links():
    try:
        pagination_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@class="page-link"]'))
        )
        pagination_links = [link for link in pagination_links if link.text and link.text.isdigit()]
        return pagination_links
    except Exception as e:
        print(f"Error getting pagination links: {e}")
        return []

def scrape_bdjobs():
    url = BASE_URL
    navigate_to_website(url)
    jobs = extract_job_data()
    pagination_links = get_pagination_links()
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(navigate_to_pages, [link]) for link in pagination_links]
        for future in futures:
            jobs.extend(future.result())
    driver.quit()
    return jobs

def save_jobs_to_file(jobs, filename='output/jobs.txt'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        for job in jobs:
            file.write(f"Title: {job['title']}\n")
            file.write(f"Company: {job['company']}\n")
            file.write(f"Location: {job['location']}\n")
            file.write(f"Date Posted: {job['date_posted']}\n")
            file.write(f"Link: {job['link']}\n")
            file.write("\n")

if __name__ == "__main__":
    jobs = scrape_bdjobs()
    save_jobs_to_file(jobs)