import os
from pymongo import MongoClient
from urllib.parse import quote_plus

# my-mongodb.airflow.svc.cluster.local


def get_mongo_client(
    mongodb_host: str = os.environ["MONGODB_HOST"],
    mongodb_username: str = os.environ["MONGODB_USERNAME"],
    mongodb_passowrd: str = os.environ["MONGODB_PASSWORD"],
) -> MongoClient:
    uri = f"mongodb://{quote_plus(mongodb_username)}:{quote_plus(mongodb_passowrd)}@{mongodb_host}"
    return MongoClient(uri)


client = get_mongo_client()
db = client["hln_database"]
collection = db["my_collection"]

data = {"key1": "value1", "key2": "value2"}

inserted_id = collection.insert_one(data).inserted_id
print(f"Data inserted with ID: {inserted_id}")


if __name__ == "__main__":
