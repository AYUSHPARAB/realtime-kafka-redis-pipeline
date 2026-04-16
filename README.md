# Real-Time Kafka Redis FastAPI Pipeline

A real-time data streaming project that simulates order generation, processes streaming data, stores results in Redis, and visualizes live analytics through a web dashboard.

## Architecture

Producer → Kafka → Consumer → Redis → FastAPI → Frontend

This project uses:
- Apache Kafka for event streaming
- Redis for in-memory data storage
- FastAPI for backend APIs
- HTML, JavaScript, and Chart.js for frontend visualization
- Docker for service orchestration

## Features

- Continuous order data generation using a producer
- Real-time stream processing using Kafka consumer
- Stores latest order, total revenue, and product-wise revenue
- REST APIs using FastAPI
- Live dashboard with auto-updating charts

## Tech Stack

- Python
- Apache Kafka
- Redis
- FastAPI
- Uvicorn
- HTML, JavaScript, Chart.js
- Docker

## How to Run

### 1. Start Docker services
docker compose up -d

### 2. Start Consumer
python consumer.py

### 3. Start Producer
python producer.py

### 4. Start Backend API
python -m uvicorn backend:app --reload

### 5. Open Dashboard
Open index.html in a browser

## Project Structure

producer.py
consumer.py
backend.py
index.html
docker-compose.yaml
requirements.txt

## Learning Outcome

This project demonstrates event-driven architecture, real-time data processing, stream analytics, backend-frontend integration, and distributed system basics.

## Future Improvements

- Add Apache Flink for stream processing
- Deploy on cloud platforms like AWS or GCP
- Add authentication layer
- Replace Redis with scalable database solutions