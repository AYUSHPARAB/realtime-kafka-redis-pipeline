from kafka import KafkaConsumer
import json
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value

    pipe = r.pipeline()

    # Store latest order
    pipe.hset("latest_order", mapping=data)

    # Total revenue
    pipe.incrby("total_revenue", data["price"])

    # Product-wise revenue
    pipe.hincrby("product_revenue", data["product"], data["price"])

    pipe.execute()

    print("Processed:", data)