import os
from locust import FastHttpUser, task, between
from dotenv import load_dotenv
from tasks.DirctoryMatch import matchAPI  # Import the DirectoryMatch task


# Load environment variables from .env file
load_dotenv()

class MatchingCompaniesScenario(FastHttpUser):
    host = os.getenv("BASE_URL")  # Read from .env file
    tasks = [matchAPI]  
    wait_time = between(1, 3)

