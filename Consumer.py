from confluent_kafka import Consumer
from db import DatabaseWriter

class MyConsumer:

    def __init__(self):
        self.dbWriter = DatabaseWriter()
        self.handler = {"battery": self.dbWriter.IncrementBatteryCount,
                        "biological": self.dbWriter.IncrementBioCount,
                        "brown-glass": self.dbWriter.IncrementBrownGlassCount,
                        "cardboard": self.dbWriter.IncrementCarboardCount,
                        "clothes": self.dbWriter.IncrementClothesCount,
                        "green-glass": self.dbWriter.IncrementGreenGlassCount,
                        "metal": self.dbWriter.IncrementMetalCount,
                        "paper": self.dbWriter.IncrementPaperCount,
                        "plastic": self.dbWriter.IncrementPlasticCount,
                        "shoes": self.dbWriter.IncrementShoeCount,
                        "trash": self.dbWriter.IncrementTrashCount,
                        "white-glass": self.dbWriter.IncrementWhiteGlassCount}
        
    def handleMessage(self, trashObject):
        func = self.handler[trashObject]
        func()