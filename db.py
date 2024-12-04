#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import os
from pymongo import MongoClient

password = os.getenv("MONGO_PASSWORD")
connection_string = f"mongodb+srv://bgwcpa:{password}@cluster0.wyjh9.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
client = MongoClient(connection_string)

db = client['huk5pd']
collection = db['lacrosse_players']

documents = [
    {"name": "Paul Rabil", "age": 29, "position": "Midfield", "goals": 25},
    {"name": "Matt Rambo", "age": 27, "position": "Attack", "goals": 30},
    {"name": "Rob Pannell", "age": 28, "position": "Attack", "goals": 22},
    {"name": "Kyle Harrison", "age": 30, "position": "Midfield", "goals": 18},
    {"name": "Trevor Baptiste", "age": 25, "position": "Faceoff", "goals": 5, "faceoff_wins": 150}
]

collection.insert_many(documents)
query = {"age": {"$lt": 29}}
result = collection.find(query).limit(3)

print("Query Results:")
for doc in result:
    print(doc)

client.close()
