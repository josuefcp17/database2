import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["libre"]
collection = db["libre"]

csv_file = r"/Users/josuecarpio/Downloads/best-selling-books.csv"

with open(csv_file, "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sales = row[4]
        if sales.isdigit():
            sales = int(sales)
        else:
            sales = None
        
        document = {
            "book": row[0],
            "author": row[1],
            "language": row[2],
            "Year": int(row[3]),
            "sales": sales,
            "genre": row[5],
        }
        collection.insert_one(document)

print("Proceso completado")
client.close()
