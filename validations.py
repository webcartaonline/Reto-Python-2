"""Validation functions for the data of a piece.

None of these functions print anything: they only raise ValueError
when the received value is not valid.
"""

ALLOWED_STATUSES = ["available", "reserved", "sold"]


def validate_not_empty(value, field_name):
    """Check that a text field is not empty."""
    if value is None:
        raise ValueError("The field '" + field_name + "' cannot be empty.")

    if str(value).strip() == "":
        raise ValueError("The field '" + field_name + "' cannot be empty.")

    return True


def validate_price(price):
    """Check that the price is a number greater than zero."""
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("The price must be a number.")

    if price <= 0:
        raise ValueError("The price must be greater than zero.")

    return True


def validate_status(status):
    """Check that the status is one of the allowed ones."""
    if not isinstance(status, str):
        raise ValueError("The status must be text.")

    if status.strip().lower() not in ALLOWED_STATUSES:
        raise ValueError(
            "The status must be one of: " + ", ".join(ALLOWED_STATUSES) + "."
        )

    return True


def validate_description(description):
    """Check that the description includes the word used or certified."""
    if not isinstance(description, str):
        raise ValueError("The description must be text.")

    text = description.lower()

    if "used" not in text and "certified" not in text:
        raise ValueError(
            "The description must contain the word 'used' or 'certified'."
        )

    return True
