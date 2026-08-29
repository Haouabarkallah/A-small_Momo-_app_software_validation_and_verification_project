# Fault Model

## Syntax fault
Example: `if amount = 10000:` instead of a valid comparison.
Expected detection: interpreter/test execution.

## Semantic fault
Example: using `amount <= 50000` for the 500 FCFA fee class when the specification requires 500 FCFA only above 50,000.
Expected detection: boundary value tests.

## Intentional fault
A developer deliberately changes the upper fee boundary from 50,000 to 60,000.
Expected detection: tests for 50,001 FCFA.

## Test selection rationale
The model prioritizes:
- boundary faults -> Boundary Value Analysis
- invalid-input faults -> Equivalence Partitioning
- PIN/balance faults -> negative and integration tests
- logic faults -> branch coverage
