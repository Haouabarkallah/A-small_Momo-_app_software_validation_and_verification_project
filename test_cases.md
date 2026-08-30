# Test Cases

<!-- | ID | Preconditions | Input | Expected Result | Type |
|---|---|---|---|---|
| TC01 | Valid account | amount=5,000 | fee=100 | Normal |
| TC02 | Valid account | amount=10,000 | fee=100 | Boundary |
| TC03 | Valid account | amount=10,001 | fee=250 | Boundary |
| TC04 | Valid account | amount=50,000 | fee=250 | Boundary |
| TC05 | Valid account | amount=50,001 | fee=500 | Boundary |
| TC06 | Valid account | amount=500,000 | fee=500 | Boundary |
| TC07 | Valid account | amount=0 | Reject | Error |
| TC08 | Valid account | amount=-100 | Reject | Error |
| TC09 | Valid account | amount=500,001 | Reject | Error |
| TC10 | Valid account | wrong PIN | Reject | Error |
| TC11 | Low balance | valid amount | Reject | Error |
| TC12 | Valid account | non-numeric amount | Reject at UI/input conversion | Error | -->

| ID       | Precondition                | Input                               | Expected Result               | Oracle                                  |
| -------- | --------------------------- | ----------------------------------- | ----------------------------- | --------------------------------------- |
| **TC01** | Solde suffisant, PIN valide | Amount = 5,000; PIN = valid         | Payment successful; Fee = 100 | Compare actual fee/status with expected |
| **TC02** | Solde suffisant, PIN valide | Amount = 10,000                     | Fee = 100; Payment accepted   | Compare actual fee with expected        |
| **TC03** | Solde suffisant, PIN valide | Amount = 10,001                     | Fee = 250; Payment accepted   | Compare actual fee/status               |
| **TC04** | Solde suffisant, PIN valide | Amount = 50,000                     | Fee = 250; Payment accepted   | Compare actual fee/status               |
| **TC05** | Solde suffisant, PIN valide | Amount = 50,001                     | Fee = 500; Payment accepted   | Compare actual fee/status               |
| **TC06** | Solde suffisant, PIN valide | Amount = 500,000                    | Fee = 500; Payment accepted   | Compare actual fee/status               |
| **TC07** | Compte disponible           | Amount = 0                          | Payment rejected              | Expected rejection = Actual rejection   |
| **TC08** | Compte disponible           | Amount = -100                       | Payment rejected              | Expected rejection = Actual rejection   |
| **TC09** | Compte disponible           | Amount = 500,001                    | Payment rejected              | Expected rejection = Actual rejection   |
| **TC10** | Solde suffisant             | Valid amount + wrong PIN            | Payment rejected              | Expected rejection = Actual rejection   |
| **TC11** | PIN valide                  | Amount valid + insufficient balance | Payment rejected              | Expected rejection = Actual rejection   |
| **TC12** | Compte disponible           | Non-numeric amount                  | Input rejected/error          | Expected error = Actual error           |
