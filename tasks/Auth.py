from locust import FastHttpUser

import os
import requests

class Auth(FastHttpUser):
    def on_start(self):
        self.token = self.get_auth_token()

    def get_auth_token(self):
        """Function to retrieve the bearer token."""
        auth_url = os.getenv("AUTH_URL")
        payload = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET")
        }
        response = requests.post(auth_url, json=payload)

        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            raise Exception("Failed to retrieve token: {}".format(response.text))