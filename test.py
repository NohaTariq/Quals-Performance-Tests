import os
from locust import HttpUser, task, between
from dotenv import load_dotenv
import requests


# Load environment variables from .env file
load_dotenv()


class CompanyUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """Called when a simulated user starts."""
        self.token = self.get_auth_token()
        print("Hello World")

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

    @task
    def get_companies(self):
        """Task to get the list of companies."""
        # Use the full URL for the GET request
        full_url = "https://us02.procore.com/qualifications/rest/v1.0/companies?per_page=50&page=1"  # Replace with the full URL
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.client.get(full_url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved companies.")
        else:
            print("Failed to retrieve companies: {}".format(response.text))

  