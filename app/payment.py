MAX_AMOUNT = 500_000
MIN_AMOUNT = 1
CORRECT_PIN = "1234"


def validate_amount(amount):
    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer")
    if amount < MIN_AMOUNT or amount > MAX_AMOUNT:
        raise ValueError("Amount must be between 1 and 500000 FCFA")
    return True


def calculate_fee(amount):
    validate_amount(amount)

    if amount <= 10_000:
        return 100

    if amount <= 50_000:
        return 250

    return 500


def validate_pin(pin):
    return (
        isinstance(pin, str)
        and len(pin) == 4
        and pin.isdigit()
        and pin == CORRECT_PIN
    )


def check_balance(balance, amount, fee):
    if balance < 0:
        raise ValueError("Balance cannot be negative")
    return balance >= amount + fee


def process_payment(amount, pin, balance):
    validate_amount(amount)

    if not validate_pin(pin):
        return {
            "success": False,
            "message": "Invalid PIN"
        }

    fee = calculate_fee(amount)
    total = amount + fee

    if not check_balance(balance, amount, fee):
        return {
            "success": False,
            "message": "Insufficient balance",
            "fee": fee,
            "total": total
        }

    return {
        "success": True,
        "message": "Payment successful",
        "fee": fee,
        "total": total,
        "remaining_balance": balance - total
    }