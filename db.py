import psycopg2


# Parse the message data
# data = message.decode('utf-8')

# Connect to PostgreSQL
conn = psycopg2.connect(user='postgres', password='postgres', host='localhost', dbname='trashObjects_data')
cursor = conn.cursor()

alter_table_query = "ALTER TABLE \"trashObjects\" ADD COLUMN recyclable BOOLEAN;"
cursor.execute(alter_table_query)

cursor.execute("""INSERT INTO "trashObjects" (object, count, type, recyclable) VALUES
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

conn.commit()

cursor.close()