import os

from locust import FastHttpUser, task, between
from tasks.RetrievingCompanies import RetrievingCompanies
from tasks.RetrievingCompaniesWithFilters import RetrievingCompaniesWithFilters

class RetrievingCompaniesScenario(FastHttpUser):
    host = os.getenv("BASE_URL")  # Read from .env file
    tasks = [RetrievingCompanies, RetrievingCompaniesWithFilters]  # Weight tasks by their occurrence
    wait_time = between(1,3)