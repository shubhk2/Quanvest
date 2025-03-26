# Quanvest

## Overview

Quanvest is a stock market financial analysis tool leveraging an NLP model to assist users in querying financial data. The system integrates multiple data sources, stores structured financial information, and enables efficient retrieval through an API-driven architecture.

## Features

- **Stock Data Storage**: Fetch and store stock market data, including financial statements and price history.
- **Financial Insights**: Process and analyze financial data using an NLP model.
- **Database Management**: Structured storage using PostgreSQL and MongoDB(for future).
- **FastAPI Backend**: Provides RESTful API endpoints for financial data retrieval.
- **Modular Design**: CRUD operations for stocks, balance sheets, income statements, cash flows, and fundamentals.

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy
- **Database**: PostgreSQL (for structured financial data), MongoDB (for unstructured or flexible storage)
- **External APIs**: Alpha Vantage (stock market data) and World Bank or RBI APIs or Ministry Of Stats(macroeconomic data)
- **ML Framework**: NLP-based model for natural language financial queries(finBert for now)

## Setup Instructions

```sh
# Clone the repository
git clone https://github.com/shubhk2/Quanvest.git
cd Quanvest

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (update .env file)

# Run the FastAPI server
uvicorn backend.main:app --reload
```

## Database Setup
```sh
# Start PostgreSQL service
sudo systemctl start postgresql

# Create database and user
psql -U postgres
CREATE DATABASE quanvest;
CREATE USER postgres WITH PASSWORD 'shubhk2004';
GRANT ALL PRIVILEGES ON DATABASE quanvest TO postgres;
```

## Project Structure

```
Quanvest/
│-- backend/
│   ├── crud/                # CRUD operations for database models
│   ├── models/              # SQLAlchemy ORM models
│   ├── routes.py            # API endpoints
│   ├── schemas.py           # Pydantic schemas for data validation
│   ├── database.py          # Database connection setup
│   ├── fetch_data.py        # Data fetching from APIs
│   ├── config.py            # Configuration settings
│   ├── main.py              # FastAPI entry point
│-- README.md                # Project documentation
│-- requirements.txt         # Python dependencies
|-- #frontend
```

## API Endpoints

- **Stock Data**: `/stocks/`
- **Balance Sheets**: `/balance_sheets/`
- **Income Statements**: `/income_statements/`
- **Cash Flow Statements**: `/cash_flows/`
- **Fundamentals**: `/fundamentals/`
- **Stock_Prices**:`/stock_prices/`

## License

This project is open-source and available under the MIT License.



