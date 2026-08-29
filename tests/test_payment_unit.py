import pytest
from app.payment import (
    validate_amount,
    calculate_fee,
    validate_pin,
    check_balance,
)


def test_amount_at_minimum():
    assert validate_amount(1) is True


def test_amount_zero_is_rejected():
    with pytest.raises(ValueError):
        validate_amount(0)


def test_amount_at_first_boundary():
    assert calculate_fee(10_000) == 100


def test_amount_just_above_first_boundary():
    assert calculate_fee(10_001) == 250


def test_amount_at_second_boundary():
    assert calculate_fee(50_000) == 250


def test_amount_just_above_second_boundary():
    assert calculate_fee(50_001) == 500


def test_amount_at_maximum():
    assert calculate_fee(500_000) == 500


def test_amount_above_maximum_is_rejected():
    with pytest.raises(ValueError):
        validate_amount(500_001)


def test_negative_amount_is_rejected():
    with pytest.raises(ValueError):
        validate_amount(-100)


def test_valid_pin():
    assert validate_pin("1234") is True


def test_invalid_pin():
    assert validate_pin("12A4") is False


def test_sufficient_balance():
    assert check_balance(10_100, 10_000, 100) is True


def test_insufficient_balance():
    assert check_balance(10_099, 10_000, 100) is False
