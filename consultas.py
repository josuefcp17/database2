from pymongo import MongoClient
from py2neo import Graph,Node,Relationship

client = MongoClient("mongodb://localhost:27017/")
db= client["basesito"]
collection= db["basesito"]
#GraphDataBase
neo4j_driver= Graph.driver("bolt://localhost:7687/", 
auth=("neo4j", "12345678"))
neo4j_session = neo4j_driver.session()

query={"score":{"$gt":5}}
results= collection.find(query)

#for query in employees_col.find():
