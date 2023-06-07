import json
import requests
from datetime import datetime

class TokenHandler():
    """Handles the interaction with the authentication provider, that is necessary to obtain an up to date token."""

    def __init__(self, token_endpoint: str, auth_client_id: str, auth_client_secret: str):
        """Initializes TokenHandler.
        
        token_endpoint (str): URL specifying the authentication endpoint.
        auth_client_id (str): Keycloak Client ID.
        auth_client_secret (str): Keycloak Client Secret.
        """
        self.__token_endpoint = token_endpoint
        self.__data = {
            'grant_type': 'client_credentials',
            'client_id': auth_client_id,
            'client_secret': auth_client_secret,
            'scope': 'salted'
        }
        self.__token_expiry_time = 0
        self.__token = ''        
        self.__headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    def __update_token(self) -> None:
        """
        Update token if the current one has expired.
        """
        if (self.__token_expiry_time > datetime.timestamp(datetime.now())): return
        res = requests.post(self.__token_endpoint, headers=self.__headers, data=self.__data)
        res_dict = json.loads(res.text)
        res.close()
        if "access_token" not in res_dict:
            raise RuntimeError("Access token could not be obtained. Credentials might be invalid.")
        self.__token = res_dict["access_token"]
        self.__token_expiry_time = datetime.timestamp(datetime.now()) + res_dict["expires_in"] - 10

    def get_token(self) -> str:
        """
        Returns an up-to-date valid token.
        """
        self.__update_token()
        return self.__token
    
