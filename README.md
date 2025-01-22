# Quals-Performance-Tests

## Description
This locust file is implemented to perform load tests on the GetCompanies API. 
## Installation

### Prerequisites
- Python 3.x
- `pip` package manager

### Installing Dependencies
1. Clone the repository:
    ```bash
    git clone git@github.com:NohaTariq/Quals-Performance-Tests.git
    cd Quals-Performance-Tests
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash  
python -m locust -f  <finename>.py
```