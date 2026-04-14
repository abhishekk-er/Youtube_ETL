# 🚀 YouTube ETL Pipeline with Airflow

A production-style Data Engineering project that extracts video data from the YouTube API, processes it, and orchestrates workflows using Apache Airflow.

------------------------------------------------------------

📌 Project Overview

This pipeline performs:

1. Extract – Fetch video data from YouTube Data API  
2. Transform – Structure and clean the data  
3. Load – Store processed data (currently JSON, extendable to PostgreSQL)  
4. Orchestrate – Automate workflows using Airflow DAGs  

------------------------------------------------------------

🧰 Tech Stack

- Python  
- Apache Airflow  
- Docker  
- PostgreSQL (planned)  
- YouTube Data API  
- GitHub  

------------------------------------------------------------

⚙️ Architecture

YouTube API → Python ETL → Airflow DAG → JSON Output (/data)
                                   ↓
                            (Future: PostgreSQL)

------------------------------------------------------------

📂 Project Structure

Youtube_ETL/
│
├── dags/
│   ├── main.py
│   └── api/
│       └── video_stats.py
│
├── data/
├── docker/
├── .env
├── requirements.txt
└── README.md

------------------------------------------------------------

🔑 Features

- Automated pipeline using Airflow DAGs  
- API integration with pagination & batching  
- Modular ETL design  
- Dockerized setup  
- Scalable architecture  

------------------------------------------------------------

🚀 How to Run

1. Clone repository
git clone https://github.com/YOUR_USERNAME/youtube-etl-airflow.git
cd youtube-etl-airflow

2. Set environment variables

Create a .env file:

YOUTUBE_API_KEY=your_api_key
CHANNEL_HANDLE=your_channel_handle

3. Start Airflow

docker-compose up

4. Open Airflow UI

http://localhost:8080

5. Add Variables in Airflow UI

YOUTUBE_API_KEY = your_api_key  
CHANNEL_HANDLE = your_channel  

6. Trigger DAG: produce_json

------------------------------------------------------------

📊 Output

JSON file generated in:

/data/YOUTUBE_ETL_<date>.json

Contains:
- Video ID  
- Title  
- Published Date  
- Duration  
- Views, Likes, Comments  

------------------------------------------------------------

🧪 Future Improvements

- Load data into PostgreSQL  
- Incremental data loading  
- Data quality checks (SODA)  
- Testing (pytest)  
- CI/CD (GitHub Actions)  
- Dashboarding  

------------------------------------------------------------

🧠 Key Learnings

- ETL pipeline design  
- API pagination & batching  
- Airflow DAG orchestration  
- Debugging real-world pipelines  
- Docker-based workflows  

------------------------------------------------------------

💼 Why This Project Matters

This project demonstrates real-world data engineering practices including:
- Workflow orchestration
- Containerization
- Pipeline automation
- Production debugging

------------------------------------------------------------

⭐ Star the repo if you found it useful!
