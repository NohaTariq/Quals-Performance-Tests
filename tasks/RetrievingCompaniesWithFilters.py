from locust import task, between
from tasks.Auth import Auth
import requests
import random
from const.companiesData import CERTIFICATES, TRADES


class RetrievingCompaniesWithFilters(Auth):
    def addFilters(key,filters):
        filterString = ""
        for filter in filters:
            filterString += f"&filters[{key}][]={filter}"
        return filterString

    @task(1)
    def get_companies_with_filters(self):
        full_url = f"""qualifications/rest/v1.0/companies?per_page=50&page=1
        {RetrievingCompaniesWithFilters.addFilters('certifications',random.sample(CERTIFICATES, 1))}
        {RetrievingCompaniesWithFilters.addFilters('trades',random.sample(TRADES, 1))}"""
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Procore-Company-Id": '42'
        }
        response = self.client.get(full_url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved companies with filters.")
        else:
            print("Failed to retrieve companies: {}".format(response.text))
            print(response.status_code)
            print(response.message)

    