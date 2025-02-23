# Stock Portfolio Management API

This project implements a RESTful API using Django REST Framework to manage stock portfolio transactions, calculate average buy prices, and track balance quantities. It adheres to the First-In-First-Out (FIFO) principle for selling shares and supports stock splits.

## Features

* **Transaction Management:**
    * Allows adding BUY, SELL, and SPLIT transactions.
    * Stores transaction details including trade date, company, trade type, quantity, price, and split ratio.
* **Average Buy Price Calculation:**
    * Calculates the average buy price of a stock based on FIFO.
    * Handles stock splits by adjusting quantities and prices accordingly.
* **Balance Quantity Tracking:**
    * Tracks the balance quantity of shares held for each company.
    * provides the remaining shares after sell transactions.
* **FIFO Implementation:**
    * Implements the FIFO method for selling shares, ensuring that the oldest shares are sold first.
* **API Endpoints:**
    * Provides endpoints to create transactions (BUY, SELL, SPLIT).
    * Provides an endpoint to retrieve the average buy price and balance quantity for a specific company up to a given date.

## Requirements

* Python
* Django
* Django REST Framework

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/parmarmanish007/stocks_management.git
    cd cd stocks_management/
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate
    venv\Scripts\activate
    ```

3.  **Install Requirements :**

    ```bash
    pip install -r requiremenets.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. Create Transaction (POST /api/transactions/)

* **Method:** POST
* **Content-Type:** application/json
* **Body:**
    ```json
    {
        "trade_date": "YYYY-MM-DD",
        "company": "Company Name",
        "trade_type": "BUY" or "SELL" or "SPLIT",
        "quantity": integer (required for BUY/SELL),
        "price": decimal (required for BUY/SELL),
        "split_ratio": "old:new" (required for SPLIT)
    }
    ```
* **Example BUY request body:**
    ```json
      {
        "trade_date": "2025-02-23",
        "company": "ABC Ltd.",
        "trade_type": "BUY",
        "quantity": 100,
        "price": 1000
      }
    ```
* **Example SPLIT request body:**
    ```json
       {
        "trade_date": "2025-02-23",
        "company": "ABC Ltd.",
        "trade_type": "SPLIT",
        "split_ratio": "1:2"
       }
    ```
* **Example SELL request body:**
    ```json
        {
          "trade_date": "2025-02-23",
          "company": "ABC Ltd.",
          "trade_type": "SELL",
          "quantity": 50,
          "price": 12.00
        }
    ```
* **Response:**
    * Returns the created transaction object.

### 2. Get Portfolio (GET /api/portfolio/)

* **Method:** GET
* **Query Parameters:**
    * `trade_date`: YYYY-MM-DD
    * `company`: Company Name
* **Example Request:** `/api/portfolio/?trade_date=2025-02-23&company=ABC Ltd.`
* **Response:**
    ```json
    {
      "balance_qty": 150,
      "avg_buy_price": 500.0
    }
    ```

## Example Usage

1.  **Add transactions using the POST /transactions/ endpoint.**
2.  **Retrieve the portfolio summary using the GET /portfolio/ endpoint.**

## Notes

* Ensure that the `trade_date` is in the correct format (YYYY-MM-DD).
* Company names are case sensitive.
* For split transactions, quantity and price fields should be left null.
* The API returns errors with appropriate HTTP status codes and error messages.