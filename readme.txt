PIPELINE PRACTICE (KAFKA + REDIS DOCKER SETUP)

OVERVIEW

This project is a simple streaming data pipeline using:

Apache Kafka (message broker)
Zookeeper (Kafka coordination service)
Redis (in-memory database / cache)
Docker Compose (container orchestration)

It is used for learning basic event streaming and data flow between services.

ARCHITECTURE

Producer → Kafka Topic → Consumer → Redis

SERVICES

Zookeeper : Kafka coordination service (port 2181)
Kafka : Message broker (port 9092)
Redis : In-memory datastore (port 6379)

HOW TO START

Start all services:

docker compose up -d

Check running containers:

docker ps

KAFKA USAGE (INSIDE DOCKER)

Create topic:
docker exec -it kafka kafka-topics --create --topic test-topic --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1

List topics:
docker exec -it kafka kafka-topics --list --bootstrap-server kafka:9092

Produce messages:
docker exec -it kafka kafka-console-producer --topic test-topic --bootstrap-server kafka:9092

Consume messages:
docker exec -it kafka kafka-console-consumer --topic test-topic --from-beginning --bootstrap-server kafka:9092

PYTHON EXAMPLE (OPTIONAL)

Producer:
Uses KafkaProducer to send messages to Kafka topic.

Consumer:
Uses KafkaConsumer to read messages and store them into Redis.

Redis stores latest messages for fast retrieval.

IMPORTANT CONFIGURATION

Kafka inside Docker must use:
KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092

DO NOT use localhost inside Docker containers.

Use localhost only when accessing Kafka from your host machine.

COMMON ISSUES

Kafka not reachable:
Check listener configuration
Use kafka:9092 inside Docker
No messages received:
Ensure consumer is running before producing messages
Redis empty:
Check consumer is writing data correctly

TECHNOLOGIES USED

Apache Kafka
Zookeeper
Redis
Docker
Python (optional scripts)

GOALS

Learn event streaming basics
Understand Kafka producer/consumer model
Practice Docker networking
Use Redis for fast data storage

FUTURE IMPROVEMENTS

Add Kafka UI dashboard
Add REST API producer
Add schema validation (JSON/Avro)
Add monitoring tools
Add Apache Flink for real-time stream processing