import re


class PasswordError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message


def special(pw):
    return bool(re.search(r"[^\w\s]", pw))


def validate_password(password: str):
    pw_len = len(password) >= 10
    pw_special = special(password)
    pw_alpha = any(i.isalpha() for i in password)
    pw_digit = any(i.isdigit() for i in password)
    if all([pw_digit, pw_alpha, pw_special, pw_digit]):
        return password
    raise PasswordError("password error")


def option_validation(user_input):
    result = any(True for i in user_input if int(i) > 4 or int(i) < 1)
    if result:
        raise InvalidInputError("Not valid input")
    return user_input


