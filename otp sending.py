import random
from twilio.rest import Client

# Your Twilio account credentials
account_sid = "ACb46b5d839db74a15419ca6890b23e95f"
auth_token = 'd79e6548865c5b8c4ad9c3d9fbf1c7b7'
twilio_number = "+15866904027"
# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send OTP via SMS
def send_otp(recipient_number):
    # Generate a random OTP (you can use any method to generate OTP)
    otp = '123456'  # Example OTP

    # Send the OTP via SMS
    message = client.messages.create(
        body=f'Your OTP is: {otp}',
        from_=twilio_number,
        to=recipient_number
    )

    print("OTP sent successfully!")
    return otp

# Function to check OTP validity
def validate_otp(otp_entered, otp_received):
    return otp_entered == otp_received

# Main login function
def login():
    # Get user's phone number
    recipient_number = input("Enter your phone number: ")

    # Send OTP
    otp_received = send_otp(recipient_number)

    # Prompt user to enter OTP
    otp_entered = input("Enter the OTP received: ")

    # Validate OTP
    if validate_otp(otp_entered, otp_received):
        print("Login successful!")
    else:
        print("Login failed. Invalid OTP.")

# Call the login function
login()