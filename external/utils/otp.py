import pyotp


def get_otp_by_secret(secret):
    otp = pyotp.TOTP(secret)
    # print("Actual OTP:", otp.now())
    return otp.now()
