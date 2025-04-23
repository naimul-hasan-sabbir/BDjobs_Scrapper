import requests
from bs4 import BeautifulSoup

BASE_URL = "https://jobs.bdjobs.com/"

def fetch_job_listings(page=1):
    url = (f"{BASE_URL}jobsearch.asp?"
+           f"fcatId=8&icatId=&page={page}")
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

def parse_job_listings(html):
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())  # Debugging line to check the HTML structure
    rows = soup.select('table#vacancyTable tr.vacancyrow')
    jobs = []
    for row in rows:
        cols = row.find_all('td')
        title = cols[1].get_text(strip=True)
        link  = BASE_URL + cols[1].a['href']
        company  = cols[2].get_text(strip=True)
        location = cols[3].get_text(strip=True)
        date_posted = cols[4].get_text(strip=True)
        jobs.append(dict(
            title=title,
            link=link,
            company=company,
            location=location,
            date_posted=date_posted
        ))
    return jobs


def scrape_bdjobs():
    all_jobs = []
    page = 1
    while True:
        html_content = fetch_job_listings(page)
        jobs = parse_job_listings(html_content)
        
        if not jobs:  # Stop if no jobs are found
            break
        
        all_jobs.extend(jobs)
        page += 1
    
    return all_jobs

def save_jobs_to_file(jobs, filename='output/jobs.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for job in jobs:
            file.write(f"Title: {job['title']}\n")
            file.write(f"Company: {job['company']}\n")
            file.write(f"Location: {job['location']}\n")
            file.write(f"Date Posted: {job['date_posted']}\n")
            file.write("\n")

if __name__ == "__main__":
    jobs = scrape_bdjobs()
    save_jobs_to_file(jobs)