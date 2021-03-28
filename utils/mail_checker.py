#!/home/michaelfareshi/.virtualenvs/myvenv/bin/python3.8
# -*- coding: utf-8 -*-
from email_validator import validate_email, EmailNotValidError


def email_validator(email):
    try:
        # Validate.
        valid = validate_email(email)

        # Update with the normalized form.
        email = valid.email
        print(email)
        return 1
    except EmailNotValidError as e:
        print(str(e))
        return 0
