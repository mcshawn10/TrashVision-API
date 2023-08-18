from confluent_kafka import Producer

class KafkaProducer:
    def __init__(self) -> None:
        self.producer_config = {
                'bootstrap.servers': 'your_kafka_broker_address',
                'security_protocol': "...",
                
            }

        self.producer = Producer(self.producer_config)



