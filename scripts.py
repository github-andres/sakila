import pandas as pd
import mysql.connectot

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M35DF678",
    database="sakila"
)

db_tables = pd.read_sql("SHOW TABLES", database)
actors = pd.read_sql("SELECT * FROM actor", database)

database.close()

print(type(db_tables))
print(actors)
