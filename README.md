# SALTED - Token Handler

TokenHandler is a Python class intended to ease the authentication process within SALTED. It is aimed at partners working on WP2 and WP4 activities, but may also be of use to external users developing DET components.



## Installation

Install as package in your Python 3 environment:
```bash
pip install git+https://github.com/SALTED-Project/TokenHandler.git
```

## Usage


```python

from tokenhandler.handler import TokenHandler
import requests

# instantiate TokenHandler
th = TokenHandler("https://auth.salted-project.eu/realms/SALTED/protocol/openid-connect/token", <your keycloak client ID>, <your keycloak client secret>)

# obtain valid token
token = th.update_token()

# test token with scorpio broker
headers = {
    'Authorization' : 'Bearer '+ token,
    'Accept': 'application/ld+json'
}
r = requests.get("https://context-broker.salted-project.eu/ngsi-ld/v1/entities?type=Organization",headers=headers)
print(r.json())


```

