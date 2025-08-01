
from imapclient import IMAPClient
import email

class EmailIngestion:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def fetch_emails(self):
        with IMAPClient("imap.example.com") as server:
            server.login(self.user, self.password)
            server.select_folder("INBOX")
            messages = server.search(["UNSEEN"])
            for uid, message_data in server.fetch(messages, "RFC822").items():
                msg = email.message_from_bytes(message_data[b"RFC822"])
                # Extract ticket number or details here
