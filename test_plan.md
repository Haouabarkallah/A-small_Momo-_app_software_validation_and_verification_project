# Test Plan

## Objective
Verify that the MoMo fee-payment module calculates fees correctly and refuses invalid or unauthorized payments.

## Scope
Amount validation, fee calculation, PIN validation, balance checking and payment processing.

## Out of scope
Real mobile-network communication, bank infrastructure and production authentication.

## Test levels
- Unit testing
- Integration testing

## Test techniques
- Equivalence Partitioning
- Boundary Value Analysis
- Negative testing
- White-box branch coverage

## Entry criteria
Application code and requirements are available.

## Exit criteria
All planned tests pass and important branches are covered.

## Test environment
Python 3.x, pytest, pytest-cov.
