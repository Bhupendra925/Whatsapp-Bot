# Whatsapp-Bot
📱 Twilio WhatsApp Message Scheduler Bot
This Python script allows you to schedule WhatsApp messages using the Twilio API and send them automatically at a specified date and time.

##🚀 Features
✅ Schedule messages for a future date & time

✅ Send WhatsApp messages using Twilio Sandbox

✅ Input-based message creation

✅ Error handling for invalid times and credentials

##🧰 Requirements
Python 3.6+

A Twilio account with WhatsApp sandbox access

##📦 Installation
Clone the repository or copy the script

Install dependencies
Copy
Edit
pip install twilio
##🔑 Setup
Sign up at https://twilio.com

Get your Account SID and Auth Token

Go to the Twilio WhatsApp Sandbox

Send the join code to the sandbox number from your WhatsApp

##📝 Usage
bash
Copy
Edit
python your_script_name.py
You will be prompted to enter:
Recipient name

WhatsApp number (e.g., +91xxxxxxxxxx)

Message to send

Scheduled date (YYYY-MM-DD)

Scheduled time (HH:MM in 24-hour format)

The bot will:

Wait until the scheduled time

Send the message automatically via WhatsApp

##🧪 Example Output
pgsql
Copy
Edit
Enter the recipient name: John
Enter the recipient WhatsApp number with country code: +919876543210
Enter the message you want to send to John: Hello from Twilio!
Enter the date to send the message (YYYY-MM-DD): 2025-07-27
Enter the time to send the message (HH:MM in 24-hour format): 19:00
✅ Message scheduled to be sent to John at 2025-07-27 19:00:00.
Message sent successfully! Message SID: SMxxxxxxxxxxxxxxxxxx
##⚠️ Notes
This script uses the Twilio Sandbox, which requires recipients to opt-in by sending the join code.

For production use (without sandbox), you must apply for WhatsApp Business API access on Twilio.

##🛡 License
MIT License © 2025
