import csv 
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db= client["basesito"]
collection= db["basesito"]

csv_file= "/Users/josuecarpio/Downloads/data.csv"

with open(csv_file, "r") as file: 
    reader= csv.DictReader(file)
    for row in reader: 
        document = {
            "register_index": row["register_index"],
            "post_id": row["post_id"],
            "comment_id": row["comment_id"],
            "datetime": row["datetime"],
            "author": row["author"],
            "title": row["title"],
            "url": row["url"],
            "score": float(row["score"]),
            "text": row["text"],
            "author_post_karma": row["author_post_karma"]
        }
        collection.insert_one(document)
    print("Ya acabe,pasa el papel")
    client.close()

