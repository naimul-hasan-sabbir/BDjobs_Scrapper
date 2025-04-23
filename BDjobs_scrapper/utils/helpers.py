def format_job_data(job_title, company, location, posting_date):
    return f"Job Title: {job_title}\nCompany: {company}\nLocation: {location}\nPosted On: {posting_date}\n"

def log_message(message):
    print(f"[LOG] {message}")