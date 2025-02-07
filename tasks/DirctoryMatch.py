from locust import task, between
from tasks.Auth import Auth
from const import companiesData
import requests
import json

class matchAPI(Auth):
    @task
    def get_directory_matched_companies(self):
        full_url = f"""qualifications/rest/v1.0/vendors/match"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        # Create the JSON payload
        payload = {
           "vendor_ids": (companiesData.Vendor_Ids)
        }     
        # Make the POST request
        response = self.client.post(full_url, headers=headers,json=(payload))

        # Check if the response is successful
        if response.status_code == 201:
            print("Successfully matched companies by CCD.")
        else:
            print("Failed to match companies: {}".format(response.text))
            #print("Response Code: {}".format(response.status_code))
        
