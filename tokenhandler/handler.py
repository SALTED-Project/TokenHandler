import json
import requests
from datetime import datetime

class TokenHandler():
    """Handles the interaction with the authentication provider, that is necessary to obtain an up to date token."""

    def __init__(self, token_endpoint, auth_client_id, auth_client_secret, scope= 'salted', grant_type= 'client_credentials', token_expiry_time = 0):
        """Initializes TokenHandler.
        
        token_endpoint (str): URL specifying the authentication endpoint.
        auth_client_id (str): Keycloak Client ID.
        auth_client_secret (str): Keycloak Client Secret.
        scope (str): Keycloak Scope.
        grant_type (str): Keycloak Grant Type used.
        token_expiry_time (int): Expiry Time of Token.
        """
        self.__token_endpoint = token_endpoint
        self.__data = {
            'grant_type': grant_type,
            'client_id': auth_client_id,
            'client_secret': auth_client_secret,
            'scope': scope
        }
        self.__token_expiry_time = token_expiry_time
        self.__token = ''        
        self.__headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    def update_token(self) -> None:
        """
        Update token if the current one has expired.
        Returns valid token.
        """
        if (self.__token_expiry_time > datetime.timestamp(datetime.now())): return
        res = requests.post(self.__token_endpoint, headers=self.__headers, data=self.__data)
        res_dict = json.loads(res.text)
        res.close()
        self.__token = res_dict["access_token"]
        self.__token_expiry_time = datetime.timestamp(datetime.now()) + res_dict["expires_in"] - 10

        return self.__token
    
    
    
