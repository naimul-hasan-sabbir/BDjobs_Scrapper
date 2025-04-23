import os

def write_jobs_to_file(jobs, file_path='output/jobs.txt'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        for job in jobs:
            file.write(f"Title: {job['title']}\n")
            file.write(f"Company: {job['company']}\n")
            file.write(f"Location: {job['location']}\n")
            file.write(f"Posted on: {job.get('date', job.get('date_posted', 'N/A'))}\n")
            file.write("\n")  # Add a newline for better separation between jobs

def read_jobs_from_file(file_path='output/jobs.txt'):
    jobs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()
            for i in range(0, len(content), 5):  # Assuming each job takes 5 lines
                job = {
                    'title': content[i].strip().split(": ")[1],
                    'company': content[i+1].strip().split(": ")[1],
                    'location': content[i+2].strip().split(": ")[1],
                    'date': content[i+3].strip().split(": ")[1],
                }
                jobs.append(job)
    except FileNotFoundError:
        print("The file does not exist.")
    return jobs