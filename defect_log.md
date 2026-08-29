# Defect Log

## D01 — Wrong fee at 50,001 FCFA
- Severity: High
- Status: Fixed
- Steps: Enter 50,001 FCFA and calculate the fee.
- Expected: 500 FCFA.
- Actual (before fix): 250 FCFA.
- Root cause: Incorrect boundary condition in fee calculation.
- Regression test: `test_amount_just_above_second_boundary`.

## D02 — Zero amount accepted
- Severity: Medium
- Status: Fixed
- Steps: Enter 0 FCFA.
- Expected: Transaction rejected.
- Actual (before fix): Amount accepted.
- Root cause: Missing lower-bound validation.
- Regression test: `test_amount_zero_is_rejected`.

## D03 — Incorrect PIN accepted
- Severity: Critical
- Status: Fixed
- Steps: Enter a valid amount and PIN 9999.
- Expected: Transaction rejected.
- Actual (before fix): Transaction processed.
- Root cause: PIN validation was not enforced before payment.
- Regression test: `test_payment_rejected_for_wrong_pin`.
