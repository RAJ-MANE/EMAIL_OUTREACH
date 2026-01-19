Automated Email Outreach System (Python)

A Python-based automated email outreach tool that sends personalized emails in bulk using contact data from an Excel file. Designed for professional cold outreach, internships, business networking, and academic projects.

🛠️ Tech Stack

Python 3.x

smtplib

pandas

email.mime

Gmail SMTP

📁 Project Structure
.
├── main.py           # Email automation script
├── contacts.xlsx     # Recipient list
├── .env              # (Ignored) Email credentials
├── .gitignore        # Security config
└── README.md         # Documentation

📊 Excel File Format

Your contacts.xlsx file must contain the following columns:

Name	Email	Company	Recent Project
John Doe	john@gmail.com
	ABC Corp	AI Chatbot
⚙️ Installation
Step 1: Install Dependencies
pip install pandas openpyxl python-dotenv

🔐 Secure Credential Setup

⚠️ Never hardcode credentials in your code or push them to GitHub

There are two safe ways to provide your Gmail credentials:

✅ Option 1: Set Environment Variables (Windows)

In Command Prompt:

set SMTP_EMAIL=your_email@gmail.com
set SMTP_PASSWORD=your_app_password
python main.py


This method keeps credentials outside your source code.

✅ Option 2: Use a .env File (Recommended)

Create a file named .env in the project root:

SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password


Modify your code slightly:

from dotenv import load_dotenv
import os

load_dotenv()
your_email = os.getenv("SMTP_EMAIL")
your_password = os.getenv("SMTP_PASSWORD")


Then add .env to your .gitignore file:

.env


This ensures your credentials are never pushed to GitHub.

🔒 Gmail App Password Setup

Gmail requires App Passwords instead of normal passwords.

Steps:

Go to Google Account → Security

Enable 2-Step Verification

Generate an App Password

Use that password in your configuration



▶️ Running the Script
python main.py


You will see logs like:

Connecting to server...
[1/20] Sent to example@gmail.com
...
All emails sent successfully.

