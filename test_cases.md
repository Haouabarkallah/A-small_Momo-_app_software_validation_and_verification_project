# Test Cases

| ID | Preconditions | Input | Expected Result | Type |
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
| TC12 | Valid account | non-numeric amount | Reject at UI/input conversion | Error |
