import psycopg2

class DatabaseWriter:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(user='postgres', password='postgres', host='localhost', dbname='trashObjects_data')
        self.cursor = self.connection.cursor()
    
    def __del__(self):
        self.cursor.close()

    def InitializeDB(self): # only called if needed

        # Parse the message data
        # data = message.decode('utf-8')# Connect to PostgreSQ
        alter_table_query = "ALTER TABLE \"trashObjects\" ADD COLUMN recyclable BOOLEAN;"
        self.cursor.execute(alter_table_query)

        self.cursor.execute("""INSERT INTO "trashObjects" (object, count, type, recyclable) VALUES
                        ('battery', 0, 'waste', true),
                        ('biological', 0, 'compost', false),
                        ('brown-glass', 0, 'glass', true),
                        ('cardboard', 0, 'paper-based', true),
                        ('clothes', 0, 'apparel', true),
                        ('green-glass', 0, 'glass', true),
                        ('metal', 0, 'metal', true),
                        ('paper', 0, 'paper-based', true),
                        ('plastic', 0, 'plastic', true),
                        ('shoes', 0, 'apparel', true),
                        ('trash', 0, 'waste', false),
                        ('white-glass', 0, 'glass', true);

        """)

        self.connection.commit()
        self.cursor.close()

    def IncrementBatteryCount(self):
        
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'battery';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()

    def IncrementBioCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'biological';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()

    def IncrementBrownGlassCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'brown-glass';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()

    def IncrementCarboardCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'carboard;  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()

    def IncrementClothesCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'clothes';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()

    def IncrementGreenGlassCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'green-glass';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()
    def IncrementMetalCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'metal';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()
    def IncrementPaperCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'paper';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()
    def IncrementPlasticCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'plastic';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()

    def IncrementShoeCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'shoe';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()
    def IncrementTrashCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'trash';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()
    def IncrementWhiteGlassCount(self):
        increment_value = 1  # You can adjust this value as needed
        update_query = """
            UPDATE "trashObjects"
            SET "count" = "count" + %i
            WHERE "object" = 'white-glass';  
        """ 
        self.cursor.execute(update_query, (increment_value,))
        self.connection.commit()




if __name__ == "__main__":
    pass