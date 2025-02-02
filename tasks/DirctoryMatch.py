from locust import task, between
from tasks.Auth import Auth
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
        #vendor Ids to be passed to the post request
        data={"vendor_ids":["598134328938336", "598134329279859", "598134326667633", "598134326667665","598134326667672"]}
       

        # Make the POST request
        response = self.client.post(full_url, headers=headers,data=json.dumps(data))

        # Check if the response is successful
        if response.status_code == 200:
            print("Successfully matched companies by CCD.")
        else:
            print("Failed to match companies: {}".format(response.text))
            print("Response Code: {}".format(response.status_code))
            print("Response Headers: {}".format(response.headers))

        
