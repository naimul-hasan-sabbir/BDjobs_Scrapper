from bs4 import BeautifulSoup

def parse_job_listing(job_element):
    title = job_element.find('h2', class_='job-title').get_text(strip=True)
    company = job_element.find('div', class_='company-name').get_text(strip=True)
    location = job_element.find('div', class_='job-location').get_text(strip=True)
    posting_date = job_element.find('div', class_='posting-date').get_text(strip=True)
    
    return {
        'title': title,
        'company': company,
        'location': location,
        'posting_date': posting_date
    }

def parse_jobs(html_content): 
    soup = BeautifulSoup(html_content, 'html.parser')
    job_elements = soup.find_all('div', class_='job-listing')
    
    jobs = []
    for job_element in job_elements:
        job = parse_job_listing(job_element)
        jobs.append(job)
    
    return jobs