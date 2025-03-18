# Quanvest
## README



Quanvest is an automated system designed to analyze historical stock data and generate investment-based predictions. The project integrates Next.js for the frontend and FastAPI for the backend, with PostgreSQL as the primary database.

### Features
- Fetch and store stock data in PostgreSQL
- Preprocess stock data for machine learning
- Implement vector database for enhanced querying (upcoming)
- Train models for fundamental investment-based predictions

### Installation

#### 1. Clone the Repository
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

#### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

#### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

#### 4. Set Up PostgreSQL
- Install PostgreSQL and create a database
- Update database credentials in `.env` file

#### 5. Run the Backend (FastAPI)
```sh
uvicorn main:app --reload
```

#### 6. Run the Frontend (Next.js)
```sh
npm install
npm run dev
```

### Roadmap
- [x] Store stock data in PostgreSQL
- [x] Fetch more stocks for a broader dataset
- [ ] Start vectorizing and preprocessing for ML training
- [ ] Implement stock prediction model
- [ ] Deploy the application




### License
This project is licensed under the Apache License 2.0.
