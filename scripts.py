import pandas as pd
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M35DF678",
    database="sakila"
)

actors = pd.read_sql("SELECT * FROM actor", database)

database.close()

print(actors)