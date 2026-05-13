import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import time
from dotenv import load_dotenv
from database import init_db, add_lead, get_pending_leads, update_lead_status
from prompt_templates import OLLAMA_PROMPT
from scraper import scrape_website
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3") 

MAX_EMAILS_PER_DAY = 20
SEND_GAP_SECONDS = 240 # 4 minutes per task requirements
def generate_email(lead, website_content=""):
    # lead tuple: (id, company_name, contact_name, contact_email, website, practice_areas, status, generated_email, created_at, sent_at)
    prompt = OLLAMA_PROMPT.format(
        company_name=lead[1],
        contact_name=lead[2] if lead[2] else "there",
        website=lead[4],
        practice_areas=lead[5],
        website_content=website_content
    )
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        print(f"Error generating email for {lead[3]}: {e}")
        return None

def send_email(to_email, subject, body_text):
    msg = MIMEMultipart()
    msg['From'] = f"William Commu <{GMAIL_USER}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    print(f"DEBUG: Sending from {msg['From']} with Reply-To {os.getenv('REPLY_TO')}")
    if os.getenv("REPLY_TO"):
        msg['Reply-To'] = os.getenv("REPLY_TO")

    # Append simple footer
    footer = "\n\nJust Me Media · justmemedia.ca"
    body_with_footer = body_text + footer

    # Plain text for that personal cold-email feel
    msg.attach(MIMEText(body_with_footer, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        return False

def get_sends_today():
    from database import DB_NAME
    import sqlite3
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    today = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("SELECT COUNT(*) FROM leads WHERE status IN ('sent', 'followed_up') AND sent_at LIKE ?", (f"{today}%",))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def process_pipeline():
    leads = get_pending_leads()
    if not leads:
        print("No pending leads found in the pipeline.")
        return

    print(f"Found {len(leads)} pending leads. Starting outreach...")
    
    for lead in leads:
        # Check daily limit
        if get_sends_today() >= MAX_EMAILS_PER_DAY:
            print(f"Daily limit of {MAX_EMAILS_PER_DAY} emails reached. Stopping for today.")
            break

        lead_id = lead[0]
        company_name = lead[1]
        contact_email = lead[3]
        website_url = lead[4]
        
        print(f"\n--- Processing Lead: {company_name} ({contact_email}) ---")
        
        # Step 1: Scrape website
        print(f"1. Scraping website: {website_url}...")
        website_content = scrape_website(website_url)

        # Step 2: Generate email
        print("2. Generating personalized email using Ollama...")
        email_body = generate_email(lead, website_content=website_content)
        
        if email_body:
            print("3. Email generated successfully. Saving to database...")
            update_lead_status(lead_id, 'generated', generated_email=email_body)
            
            # Step 3: Send email
            subject = f"Quick question regarding {company_name}"
            
            print(f"4. Sending email via Gmail SMTP ({GMAIL_USER})...")
            if send_email(contact_email, subject, email_body):
                print(f"Success! Email sent to {contact_email}.")
                update_lead_status(lead_id, 'sent', sent_at=datetime.now())
                
                # Polite delay to avoid rate limits
                print(f"Waiting {SEND_GAP_SECONDS} seconds before the next lead (Rate Limiting)...")
                time.sleep(SEND_GAP_SECONDS)
            else:
                print(f"Error: Failed to send email to {contact_email}")
        else:
            print("Error: Failed to generate email text.")

def seed_test_lead():
    add_lead(
        company_name="Acme Corp", 
        contact_name="John", 
        contact_email="william@justmemedia.ca", # Test lead
        website="acmecorp.com", 
        practice_areas="SaaS, B2B Software"
    )

if __name__ == "__main__":
    init_db()
    
    # Uncomment the next line to seed a test lead into your database
    seed_test_lead()
    
    # Process the pipeline
    process_pipeline()
