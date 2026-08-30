from app.payment import process_payment


# IT01 — Successful payment
def test_successful_payment_integrates_fee_pin_and_balance():
    result = process_payment(10_000, "1234", 20_000)

    assert result["success"] is True
    assert result["fee"] == 100
    assert result["total"] == 10_100
    assert result["remaining_balance"] == 9_900


# IT02 — Wrong PIN
def test_payment_rejected_for_wrong_pin():
    result = process_payment(10_000, "9999", 20_000)

    assert result["success"] is False
    assert result["message"] == "Invalid PIN"


# IT03 — Insufficient balance
def test_payment_rejected_for_insufficient_balance():
    result = process_payment(50_001, "1234", 50_500)

    assert result["success"] is False
    assert result["message"] == "Insufficient balance"
    assert result["fee"] == 500
    assert result["total"] == 50_501