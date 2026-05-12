from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import resend

load_dotenv()

app = Flask(__name__)
# Enable CORS for the frontend to communicate with the backend
CORS(app)

resend.api_key = os.getenv("RESEND_API_KEY", "re_6mgdu92j_3fNjjtqazmQT9q9wP3MGQ8pU")
DESTINATION_EMAIL = "william@justmemedia.ca"

def send_email(subject, body):
    # Until the custom domain is verified in Resend, we must use their onboarding domain
    # and send TO the registered account email (william@justmemedia.ca)
    params = {
        "from": "Just Me Media <onboarding@resend.dev>",
        "to": [DESTINATION_EMAIL],
        "subject": subject,
        "text": body,
    }
    email = resend.Emails.send(params)
    return email

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get('name', 'N/A')
        company = data.get('company', 'N/A')
        email = data.get('email', 'N/A')
        service = data.get('service', 'N/A')
        message = data.get('message', 'N/A')
        
        body = f"New Project Enquiry:\n\nName: {name}\nCompany: {company}\nEmail: {email}\nService: {service}\nMessage:\n{message}"
        
        send_email("New Project Enquiry — Just Me Media", body)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/partners', methods=['POST'])
def partners():
    try:
        data = request.json
        name = data.get('name', 'N/A')
        email = data.get('email', 'N/A')
        role = data.get('role', 'N/A')
        strategy = data.get('strategy', 'N/A')
        
        body = f"New Partner Application:\n\nName: {name}\nEmail: {email}\nRole/Expertise: {role}\nStrategy:\n{strategy}"
        
        send_email("New Partner Application — Just Me Media", body)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "justmemedia-backend"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
