import os

KEY = os.urandom(16)
iv = os.urandom(16)


def get_cookie(user_data):
    user_data = user_data.replace(";", "").replace("=", "")
    return "comment1=cooking%20MCs;userdata=" \\\
        + user_data + ";comment2=%20like%20a%20pound%20of%20bacon"


def validate_user(cookie):
    return ";admin=true;" in cookie
