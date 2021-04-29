# Auto-Register for excess Vaccine in Copenhagen

Small python script to speed-up the application process for the excess vaccine provided by the CPH region.

## Installation

Installing the dependencies:

```sh
$ pip install -r requirements.txt
```
Example:

```py
from Vaccine import Register
Register("Jens L. Bech", "49", "Skolevej 14, 2", "1868 Frederiksberg C", "29291981", 5)
```

In resetPassword.py enter your private and public keys and mobile number for sms to be sent from.
In database.py enter your srv_string

## Previews
 Dashboard             |  Transactions
:-------------------------:|:-------------------------:
![](https://i.imgur.com/eY0jNY4.png)  |  ![](https://i.imgur.com/VTsyVls.png)

        

[![](https://i.gyazo.com/5eb8a04bc082be7d9f5c9be5af46e6ac.gif)](https://gyazo.com/5eb8a04bc082be7d9f5c9be5af46e6ac) 

## Todos

- Finish the interest rate implementation for the accounts.
- Create an admin panel to change details of user accounts.
- Add account verification process, each new account has to be approved by an employee.
