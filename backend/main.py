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
            return {
                "symbol": symbol,
                "fiscalDateEnding": latest_report["fiscalDateEnding"],
                "totalRevenue": latest_report["totalRevenue"],
                "netIncome": latest_report["netIncome"]
            }
        return {"error": "No income data found"}
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
