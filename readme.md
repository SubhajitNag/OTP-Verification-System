# Python Email OTP Verification

This Python script generates a one-time password (OTP) and sends it to a specified email address for verification purposes.
It's a simple implementation using the `smtplib` and `email.message` libraries to demonstrate email-based OTP verification.

## Features

- Generates a 6-digit OTP.
- Sends the OTP to the user's email address.
- Verifies the OTP entered by the user.

## Prerequisites
Before you can run this script, you need to set up a few things:

1. **Python 3**: Make sure you have Python 3.x installed on your system.
2. **Email Account**: The script uses an email account to send OTPs. You'll need to provide the email address and password.For Gmail accounts, you need to set up an App Password if 2-Factor Authentication (2FA) is enabled.

## Setup
### Environment Variables
You need to set the following environment variables for the script to access your email account securely:
Window Icon -> View Advanced System Settings -> Environment Variables -> User Variable:
- `EMAIL_ADDRESS`: The email address used to send OTPs.
- `EMAIL_PASSWORD`: The password for the email account.


#### Running the Script
To run the script, simply navigate to the directory containing the script and run in CMD:

python otp_verification.py