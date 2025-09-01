# Wallet Service API

This is a RESTful API for a simple wallet service, built with Python, FastAPI, and MongoDB. It provides basic functionalities for managing users, wallets, and transactions.

## Features

-   **User Management**: Create and manage users.
-   **Wallet Management**: Handle wallet creation and balance inquiries.
-   **Transaction History**: Retrieve paginated transaction history for users.
-   **Fund Transfers**: Transfer funds between wallets.

## Project Structure

The project follows a modular structure to separate concerns:

```
├── main.py                 # Main application entry point
├── requirements.txt        # Project dependencies
├── config/
│   └── db.py               # MongoDB database connection and setup
├── controllers/
│   └── ..._controller.py   # Data access logic (interacts with the database)
├── handlers/
│   └── ..._handler.py      # Business logic for API endpoints
├── routers/
│   └── ..._routers.py      # API endpoint definitions (routing)
└── schemas/
    └── ..._schemas.py      # Pydantic models for data validation and serialization
```

## Prerequisites

-   Python 3.9+
-   MongoDB instance (local or cloud-hosted)
-   `pip` for package management

## Setup and Installation

1.  **Clone the repository:**

    ```sh
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your MongoDB connection string. The application uses this file to connect to the database.

    **.env file example:**

    ```
    MONGO_DETAILS="mongodb://localhost:27017"
    ```

## Running the Application

To run the development server, use `uvicorn`:

```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs`.

## API Endpoints

Here are some of the main endpoints available:

-   **Users**:
    -   `POST /users/`: Create a new user.
    -   `GET /users/{user_id}`: Get user details.
-   **Wallet**:
    -   `POST /wallet/add-money`: Add money to a wallet.
    -   `GET /wallet/balance/{user_id}`: Get wallet balance for a user.
-   **Transactions**:
    -   `GET /transactions/{user_id}`: Get a paginated list of transactions for a user (e.g., `/transactions/{user_id}?page=1&limit=10`).
    -   `GET /transaction/{transaction_id}`: Get details for a specific transaction.
-   **Transfers**:
    -   `POST /transfers/`: Initiate a transfer between wallets.

# misogi_eval_2

step1:
pip install -r requirements.txt

step2:
uvicorn main:app --reload

browser

http://localhost:8000/docs#/
