from locust import task
from dotenv import load_dotenv
from tasks.Auth import Auth


class RetrievingCompanies(Auth):
    @task(1)
    def get_companies(self):
        """Task to get the list of companies."""
        # Use the full URL for the GET request

        full_url = f"qualifications/rest/v1.0/companies?per_page=50&page=1"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Procore-Company-Id": '42'
        }
        response = self.client.get(full_url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved companies.")
        else:
            print("Failed to retrieve companies: {}".format(response.text))
            print(response.status_code)
