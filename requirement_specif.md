# Mini Requirements Specification

R1. The payment amount shall be an integer from 1 to 500,000 FCFA.

R2. For 1–10,000 FCFA, the fee shall be 100 FCFA.

R3. For 10,001–50,000 FCFA, the fee shall be 250 FCFA.

R4. For 50,001–500,000 FCFA, the fee shall be 500 FCFA.

R5. The PIN shall contain exactly four digits.

R6. A payment shall succeed only when the PIN is valid and the balance is at least amount + fee.

R7. Invalid amounts shall be rejected.
