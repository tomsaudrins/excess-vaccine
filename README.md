# Auto-Register for excess Vaccine in Copenhagen

Small python script to speed-up the application process for the excess vaccine provided by the CPH region.
Should be working even after website requests for more cookies, as it will select the minimum required every time.
As this possibility was just anounced, I am not sure if the URL for the application itself changes, therefore it is retrieved every time.

## Installation

Installing the dependencies:

```sh
$ pip install -r requirements.txt
```
Example:

```py
from Vaccine import Register
Register(name = "Jens L. Bech", age = "49", address = "Skolevej 14, 2", zipcode = "1868 Frederiksberg C", phone = "29291981", center = "Øksnehallen, Halmtorvet 11, København V")
```
