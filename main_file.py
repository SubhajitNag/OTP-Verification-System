import os
import sys
from module_1_generate_otp import generate_otp
from module_2_send_otp import send_otp
from module_3_prompt_otp import enter_otp
from module_4_verify_email import verify_otp


def main():
    otp = str(generate_otp())

    user_email = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')
    # password = None
    # password = ""

    if user_email is not None and password is not None:
        print("Successfully retrieved credentials")
        otp_sent = send_otp(user_email, password, otp)
    else:
        print("Unable to retrieve credentials. Exiting...")
        sys.exit()

    if otp_sent:
        chances = 3
        while chances > 0:
            entered_otp = enter_otp()
            if verify_otp(otp, entered_otp):
                print("OTP verification successful. Access granted!")
                break
            else:
                chances -= 1
                print("Incorrect OTP. Please try again.")
                print(f"You have {chances} chances left.")
                print()
        if chances == 0:
            print("You have exceeded the maximum number of attempts. Access denied.")


if __name__ == "__main__":
    main()
