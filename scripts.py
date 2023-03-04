import pandas as pd
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M35DF678",
    database="sakila"
)

db_tables = pd.read_sql("SHOW TABLES", database)

database.close()
print(db_tables)