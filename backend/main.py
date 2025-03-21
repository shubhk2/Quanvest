import requests
from fastapi import FastAPI

app = FastAPI()

API_KEY="EYRSR3K2PLPRL72F"
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/income/{symbol}")
async def get_income_statement(symbol: str):
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract Revenue & Net Income (latest year)
        annual_reports = data.get("annualReports", [])
        if annual_reports:
            latest_report = annual_reports[0]
            return latest_report
        return {"error": "No income data found"}
    else:
        return {"error": "Failed to fetch data"}

@app.get("/balance/{symbol}")
async def get_balance_sheet(symbol: str):
    url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extract Total Assets & Total Liabilities (latest year)
        annual_reports = data.get("annualReports", [])
        if annual_reports:
            latest_report = annual_reports[0]
            return  latest_report

        return {"error": "No balance sheet data found"}
    else:
        return {"error": "Failed to fetch data"}

@app.get("/fundamentals/{symbol}")
async def get_fundamentals(symbol: str):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    print(response.json())

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

@app.get("/cashflow/{symbol}")
async def get_cash_flow(symbol: str):
    url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        # Extract Operating Cash Flow & Capital Expenditures (latest year)
        annual_reports = data.get("annualReports", [])
        if annual_reports:
            latest_report = annual_reports[0]
            return latest_report
        return {"error": "No cash flow data found"}
    else:
        return {"error": "Failed to fetch data"}


@app.get("/stock_prices/monthly/{symbol}")
async def get_monthly_stock_prices(symbol: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    time_series = data.get("Monthly Adjusted Time Series", {})

    if not time_series:
        return {"error": "No data available for this stocks symbol"}

    # Extract only the most recent month for display
    latest_date = sorted(time_series.keys())[-1]
    latest_data = time_series[latest_date]

    return latest_data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
