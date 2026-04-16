from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ["apple", "banana", "laptop", "phone"]

order_id = 1

while True:
    data = {
        "order_id": order_id,
        "product": random.choice(products),
        "price": random.randint(10, 1000)
    }

    producer.send("orders", data)
    print("Sent:", data)

    order_id += 1
    time.sleep(random.randint(1, 10))