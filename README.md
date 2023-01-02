```
docker network create kafka-network
docker-compose -f docker-compose-kafka.yaml up -d
docker-compose up --build

docker-compose -f docker-compose-kafka.yaml logs broker


## List Brokers
docker exec -ti broker /usr/bin/broker-list.sh

## List Topics
docker exec -ti broker /opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181

topic-test


## Describe Topic
docker exec -ti broker /opt/kafka/bin/kafka-topics.sh --describe --topic topic-test --bootstrap-server broker:9092

## View Message Content Sent to Topic
docker exec -ti broker /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server broker:9092 --topic topic-test --from-beginning --max-messages 10

```
