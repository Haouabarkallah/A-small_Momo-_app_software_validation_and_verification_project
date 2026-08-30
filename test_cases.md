# Test Cases


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
