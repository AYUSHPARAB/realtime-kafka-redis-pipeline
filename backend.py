from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/latest")
def get_latest():
    return r.hgetall("latest_order")

@app.get("/revenue")
def get_revenue():
    return {"total_revenue": int(r.get("total_revenue") or 0)}

@app.get("/products")
def get_products():
    return r.hgetall("product_revenue")