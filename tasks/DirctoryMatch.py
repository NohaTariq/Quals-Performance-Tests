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
        data={"vendor_ids":["598134328938336", "598134329279859", "598134326667633",
                            "598134326667665","598134326667672", "562949960646190",
                            "4743908","29034876",
                            "562949961806383",
                            "598134329244297",
                            "4997457",
                            "598134325942850",
                            "30656504",
                            "562949962135646",
                            "22445084",
                            "32331890",
                            "13213841",
                            "598134328823880",
                            "20511307",
                            "5962816",
                            "32716373",
                            "32391326",
                            "30510860",
                            "32454696",
                            "30625444",
                            "12397419",
                            "2567271",
                            "29669890",
                            "19025154",
                            "26527689",
                            "4847787",
                            "29474689",
                            "28023369",
                            "562949958469076",
                            "32058829",
                            "562949956595917",
                            "562949958187719",
                            "32132533",
                            "598134327035287"]}
       

        # Make the POST request
        response = self.client.post(full_url, headers=headers,data=json.dumps(data))

        # Check if the response is successful
        if response.status_code == 201:
            print("Successfully matched companies by CCD.")
        else:
            print("Failed to match companies: {}".format(response.text))
            #print("Response Code: {}".format(response.status_code))
        
