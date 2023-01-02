from time import sleep
import json
from kafka import KafkaProducer
import logging, os

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

TOPIC = os.environ.get('TOPIC')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

logging.info('topic is %s and broker is %s', TOPIC, KAFKA_BROKER_URL)

def main():
        
    producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER_URL],
                            value_serializer=lambda x: 
                            json.dumps(x).encode('utf-8'))

    i = 0
    while True:
        data = {
            'number': i
        }
        logging.info(data)
        producer.send(TOPIC, value=data)

        i += 1
        sleep(5)


if __name__ == "__main__":
    logging.info("sending messages to Kafka broker")
    main()