import re


def validate_phone_number(phone_number: str):
    if not re.match(r'^7\d{10}$', phone_number):
        raise ValueError('Invalid phone number. Need 7XXXXXXXXX')
    return True
