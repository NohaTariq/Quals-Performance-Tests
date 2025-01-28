import os
import subprocess
from dotenv import load_dotenv

def main():
    """Main entry point for running Locust tests."""
    load_dotenv()  # Load environment variables from .env file

    print("Starting Locust performance tests...")

    # Run Locust with all user classes
    subprocess.run([
        "locust",
        "-f", "workflows/AllWorkflows.py",  # Point to the file containing user classes
        "-u", "50",  # Total number of users
        "-r", "1",  # Hatch rate (users per second)
        "--run-time", "20s",  # Total runtime (2 minutes)
    ])

if __name__ == "__main__":
    main()
