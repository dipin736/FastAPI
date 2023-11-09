# FastAPI

# User Registration and Profile Picture Storage with FastAPI, PostgreSQL, and MongoDB


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FastAPI.git
   cd FastAPI

    1. Install the required Python packages using pip:

            pip install -r requirements.txt

    2. Set up your database configurations in the application:

    PostgreSQL: Modify the DATABASE_URL in the main.py file to include your PostgreSQL database credentials.

            DATABASE_URL = "postgresql://yourusername:yourpassword@localhost/yourdatabase"

            MongoDB: Ensure that you have a running MongoDB instance on mongodb://localhost:27017.


## Running the Application

--Start the FastAPI application:

    uvicorn main:app --reload

The application will be running on http://127.0.0.1:8000. You can access the API at this address.
