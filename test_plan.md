# Test Plan

## Objective
To verify that the MoMo payment feature correctly validates the payment amount, calculates the correct fee, validates the PIN, checks the balance and accepts or rejects the payment appropriately.

## Scope
Amount validation, fee calculation, PIN validation, balance checking, Successful payment and Rejected payment

## Out of scope
Mobile network, Real banking infrastructure, Real SMS delivery and Production authentication

## Test levels
- Unit testing
- Integration testing

## Test techniques
- Functional testing
- Black-box testing
- Equivalence Partitioning
- Boundary Value Analysis
- Negative testing

## Entry criteria
Application code and requirements are available.

## Exit criteria
All planned tests pass and important branches are covered.

## Test environment
Python 3.x, pytest, pytest-cov.
