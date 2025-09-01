from pymongo import MongoClient

client = MongoClient("mongodb+srv://akc972527:akc972527@clusterswati.73qfujt.mongodb.net/?retryWrites=true&w=majority&appName=ClusterSwati")
db = client.wallet

def get_db():
    return db

user_collection = db["users"]
transaction_collection = db["transactions"]


