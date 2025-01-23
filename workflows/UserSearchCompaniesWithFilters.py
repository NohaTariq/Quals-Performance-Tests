import os

from locust import FastHttpUser, task, between
from tasks.RetrievingCompaniesWithFilters import RetrievingCompaniesWithFilters
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RetrievingCompaniesWithFiltersScenario(FastHttpUser):
    host = os.getenv("BASE_URL")  # Read from .env file
    tasks = [RetrievingCompaniesWithFilters]  # Weight tasks by their occurrence
    wait_time = between(1, 3)