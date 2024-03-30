import smtplib
from email.message import EmailMessage


# Function to send OTP to the user's email
def send_otp(sender_email, password, otp):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = sender_email
        smtp_password = password

        # Create EmailMessage object
        msg = EmailMessage()
        msg['From'] = smtp_username
        msg['To'] = input("Enter Email of Recipient: ")
        msg['Subject'] = 'OTP Verification'
        msg.set_content(f'Your OTP is: {otp}')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            if server.login(smtp_username, smtp_password):
                server.send_message(msg)
                print("OTP sent successfully.")
                return True
            else:
                print(
                    "Authentication error: Please check your email address and password.")
                return False
    except Exception as e:
        print("Error occurred while sending OTP:", e)
        return False
    finally:
        del password
