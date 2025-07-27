# Step 1: Install library (already done)
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step 2: Twilio credentials
account_sid = 'AC3f63bccf17fb42abaff7e584d8e6faeb'
auth_token = '0126f5e66ee7a4047b241c88ac565321'

client = Client(account_sid, auth_token)  # ✅ variable name should not be capitalized

# Step 3: Send WhatsApp message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')  # Print actual error

# Step 4: User inputs
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code: ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step 5: Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

try:
    # Combine and parse date and time
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()

    # Calculate delay
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print('❌ The specified time is in the past. Please enter a future date and time.')
    else:
        print(f'✅ Message scheduled to be sent to {name} at {schedule_datetime}.')

        # Wait until the scheduled time
        time.sleep(delay_seconds)

        # Send message
        send_whatsapp_message(recipient_number, message_body)

except ValueError:
    print("❌ Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
