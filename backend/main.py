from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
# from starlette.middleware import Middleware

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}

@app.get("/data")
async def get_data():
    return {"stocks": ["AAPL", "GOOGL", "TSLA"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)