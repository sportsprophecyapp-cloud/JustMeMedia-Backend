import os
import imaplib
import email
import sqlite3
import time
from datetime import datetime
from dotenv import load_dotenv
from database import DB_NAME, update_lead_status

load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def check_for_replies():
    try:
        # Connect to Gmail IMAP
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        mail.select('inbox')

        # Search for all messages
        # In a real scenario, we might want to search for UNSEEN or since a certain date
        status, data = mail.search(None, 'ALL')
        mail_ids = data[0].split()

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Get all emails we've contacted
        cursor.execute("SELECT contact_email, company_name FROM leads WHERE status IN ('sent', 'followed_up')")
        active_leads = {email: company for email, company in cursor.fetchall()}
        
        replies_found = 0

        for m_id in mail_ids:
            status, data = mail.fetch(m_id, '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            from_header = msg.get('From')
            # Extract email address from "Name <email@example.com>"
            from_email = email.utils.parseaddr(from_header)[1].lower()
            
            if from_email in active_leads:
                company_name = active_leads[from_email]
                print(f"!!! REPLY DETECTED from {company_name} ({from_email}) !!!")
                
                # Update database
                cursor.execute("UPDATE leads SET status = 'replied' WHERE contact_email = ?", (from_email,))
                conn.commit()
                
                print(f"Notification: {company_name} has replied! Switching to manual mode for this lead.")
                replies_found += 1
                
        conn.close()
        mail.logout()
        return replies_found

    except Exception as e:
        print(f"Error checking for replies: {e}")
        return 0

if __name__ == "__main__":
    print(f"Starting Reply Detector for {GMAIL_USER}...")
    while True:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Checking for new replies...")
        found = check_for_replies()
        if found > 0:
            print(f"Processed {found} new replies.")
        else:
            print("No new replies detected.")
            
        print("Waiting 15 minutes for the next check...")
        time.sleep(900) # 15 minutes
