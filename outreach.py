import smtplib
import pandas as pd
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===================== CONFIGURATION =====================
# Enter your email credentials below before running
your_email = "your_email@gmail.com"         # <-- Add your email here
your_password = "your_app_password_here"    # <-- Add your Gmail App Password here
smtp_server = "smtp.gmail.com"
smtp_port = 587
# ========================================================

def send_outreach():
    try:
        # 1. Load data from Excel file
        df = pd.read_excel('contacts.xlsx')
        
        # 2. Setup SMTP Server
        print("Connecting to server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(your_email, your_password)
        
        for index, row in df.iterrows():
            recipient_email = row['Email']
            recipient_name = row['Name']
            company = row['Company']
            project = row['Recent Project']

            message = MIMEMultipart()
            message['From'] = f"Raj Mane <{your_email}>"
            message['To'] = recipient_email
            message['Subject'] = f"Inquiry regarding {project} | Connection Request"

            body = (
                f"Dear {recipient_name},\n\n"
                f"I hope this email finds you well.\n\n"
                f"I have been following the developments at {company}, "
                f"specifically regarding the {project}. Given your expertise, "
                "I am reaching out to explore potential synergies.\n\n"
                "Best regards,\n\n"
                "Raj Mane\n"
                "Tech Intern Dilatio.co"
            )
            
            message.attach(MIMEText(body, 'plain'))

            server.send_message(message)
            print(f"✅ [{index+1}/{len(df)}] Sent to {recipient_email}")
            
            # Wait to avoid Gmail spam detection
            time.sleep(5)

        server.quit()
        print("\n🚀 All emails sent successfully.")

    except Exception as e:
        print(f"❌ Critical Error: {e}")

if __name__ == "__main__":
    send_outreach()
