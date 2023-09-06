from confluent_kafka import Producer

# class KafkaProducer:
#     def __init__(self) -> None:
#         self.producer_config = {
#                 'bootstrap.servers': 'localhost',
#                 'security_protocol': "...",
                
#             }

#         self.producer = Producer(self.producer_config)

producer_config = {'bootstrap.servers': 'localhost:9092'
                   }
producer = Producer(producer_config)



