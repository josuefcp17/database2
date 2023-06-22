from pymongo import MongoClient
from py2neo import Graph, Node, Relationship

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["libreria"]
collection = db["libreria"]

query = {"sales":{"$gte":100}}
results = collection.find(query)

# Conexión a Neo4j
graph = Graph("bolt://localhost:7687", 
auth=("neo4j", "12345678"))

for result in results:

    # Crear el nodo 
    obra_node = Node("Obra", Author=result["book"])
    graph.create(obra_node)
    #crear el nodo si no existe
    genre_node = Node("genre", genre=result["genre"])
    graph.merge(genre_node, "genre", "genre")

    # Crear la relación 
    relationship = Relationship(obra_node, "Genero", genre_node)
    graph.create(relationship)
