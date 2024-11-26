import re
def extract_emails(text):
    email_pattern=r'[a-zA-Z0-9.%+-]+@[a-z A-Z 0-9.-]+\.[a-z A-Z]{2}'
    return re.findall(email_pattern,text)
sample_text=("Please contact us at support@example.com or sales@example.org")
email=extract_emails(sample_text)
print("Extracted emails: ",email)