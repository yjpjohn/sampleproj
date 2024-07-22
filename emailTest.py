import imaplib
import email
from email.header import decode_header


# Gmail login credentials
username = "aa"
password = "aa"
recipient_email = "aa@gmail.com"
subject_line_filter = "Application Outage"  # Subject line filter to identify relevant emails

# Connect to the server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
# Login to your account
mail.login(username, password)
# Select the mailbox you want to use
mail.select("inbox")

specific_sender = "sender@gmail.com"

# Search for all emails
#status, messages = mail.search(None, 'ALL')
status, messages = mail.search(None,f'(UNSEEN FROM "{specific_sender}")')
print(status)
print(messages)


# Convert messages to a list of email IDs
email_ids = messages[0].split()

# Initialize a list to store the outages
outages = []

# Loop through the email IDs
for email_id in email_ids:
    # Fetch the email by ID
    res, msg = mail.fetch(email_id, "(RFC822)")

    for response in msg:
        if isinstance(response, tuple):
            # Parse the email content
            msg = email.message_from_bytes(response[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            print(subject)
            if isinstance(subject, bytes):
                # If it's bytes, decode to str
                subject = subject.decode(encoding if encoding else "utf-8")
                print(subject)



