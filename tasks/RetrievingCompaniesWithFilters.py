from locust import task, between
from tasks.Auth import Auth
import requests
import random
from const.companiesData import CERTIFICATES, TRADES


class RetrievingCompaniesWithFilters(Auth):
    def addFilters(key,filters):
        filterString = ""
        for filter in filters:
            filterString += f"&filters[{key}]={filter}"
        return filterString

    @task
    def get_companies_with_filters(self):
        filters = {
            "trades": "architectural_concrete",
            "certifications": "Certified Business Enterprise (CBE)"
        }
        full_url = f"""qualifications/rest/v1.0/companies?per_page=50&page=1
        {RetrievingCompaniesWithFilters.addFilters('certifications',random.sample(CERTIFICATES, 3))}
        {RetrievingCompaniesWithFilters.addFilters('trades',random.sample(TRADES, 3))}"""
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.client.get(full_url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved companies with filters.")
        else:
            print("Failed to retrieve companies: {}".format(response.text))
            print(response.status_code)

    