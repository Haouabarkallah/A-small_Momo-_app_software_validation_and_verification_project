import pytest

from app.payment import (
    validate_amount,
    calculate_fee,
    validate_pin,
    check_balance,
)


# TC01 — Normal path
def test_amount_normal():
    assert calculate_fee(5_000) == 100


# TC02 — Boundary
def test_amount_at_first_boundary():
    assert calculate_fee(10_000) == 100


# TC03 — Boundary
def test_amount_just_above_first_boundary():
    assert calculate_fee(10_001) == 250


# TC04 — Boundary
def test_amount_at_second_boundary():
    assert calculate_fee(50_000) == 250


# TC05 — Boundary
def test_amount_just_above_second_boundary():
    assert calculate_fee(50_001) == 500


# TC06 — Boundary
def test_amount_at_maximum():
    assert calculate_fee(500_000) == 500


# TC07 — Error path
def test_amount_zero_is_rejected():
    with pytest.raises(ValueError):
        validate_amount(0)


# TC08 — Error path
def test_negative_amount_is_rejected():
    with pytest.raises(ValueError):
        validate_amount(-100)


# TC09 — Error path
def test_amount_above_maximum_is_rejected():
    with pytest.raises(ValueError):
        validate_amount(500_001)


# TC12 — Error path
def test_non_numeric_amount_is_rejected():
    with pytest.raises((ValueError, TypeError)):
        validate_amount("abc")


# Additional unit test — minimum valid amount
def test_amount_at_minimum():
    assert validate_amount(1) is True


# Additional unit test — valid PIN
def test_valid_pin():
    assert validate_pin("1234") is True


# Additional unit test — invalid PIN
def test_invalid_pin():
    assert validate_pin("12A4") is False


# Additional unit test — sufficient balance
def test_sufficient_balance():
    assert check_balance(10_100, 10_000, 100) is True


# Additional unit test — insufficient balance
def test_insufficient_balance():
    assert check_balance(10_099, 10_000, 100) is False


 # Additional function
def test_negative_balance_is_rejected():
    with pytest.raises(ValueError):
        check_balance(-1, 10_000, 100)    