# MoMo V&V Project

Small console application created for the Software Verification & Validation exam.

## Features
- Validate payment amount: 1 to 500,000 FCFA
- Calculate transaction fee
- Validate 4-digit PIN
- Check sufficient balance
- Process payment

## Fee rules
- 1–10,000 FCFA -> 100 FCFA
- 10,001–50,000 FCFA -> 250 FCFA
- 50,001–500,000 FCFA -> 500 FCFA

## Run the application
```bash
python main.py
```

## Run automated tests
```bash
pytest -v
```

## Run coverage
```bash
pytest --cov=app --cov-branch --cov-report=term-missing
```
