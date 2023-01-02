import logging
import json
# from pymongo import MongoClient
from kafka import KafkaConsumer
import os 

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

TOPIC = os.environ.get('TOPIC')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')

def main():
    try:
        consumer = KafkaConsumer(
            TOPIC,
            bootstrap_servers=[KAFKA_BROKER_URL],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        for message in consumer:
            logging.info("%s:%d:%d: key=%s value=%s", message.topic, message.partition,
                                                 message.offset, message.key, message.value)

    except Exception as e:
        logging.info('Connection successful', e)


if __name__ == "__main__":
    logging.info('Consumer starting')
    main()

    # for msg in consumer:
    #     record = json.loads(msg.value)
    #     number = record['number']
        
    #     # Create dictionary and ingest data into MongoDB
    #     try:
    #         rec = {
    #             'name':number
    #         }
    #         rec_id1 = db.test.insert_one(rec)

    #         print("Data inserted with record ids", rec)
    #     except Exception as e:
    #         logging.info('Could not insert into MongoDB', e)
