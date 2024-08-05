import os
import redis
from pymongo import MongoClient
from rejson import Client, Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB configuration
mongo_uri = os.getenv('MONGODB_URI')
mongo_db_name = os.getenv('MONGODB_DB_NAME')
mongo_client = MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db_name]

# Redis configuration
redis_host = os.getenv('REDIS_HOST')
redis_port = int(os.getenv('REDIS_PORT'))
redis_password = os.getenv('REDIS_PASSWORD')
redis_client = Client(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def write_to_mongo(collection_name, key, value):
    collection = mongo_db[collection_name]
    if value is not None:
        # ReJSON already returns parsed JSON, so no need to use json.loads
        collection.update_one({'_id': key}, {'$set': value}, upsert=True)
    else:
        # Handle deletions
        collection.delete_one({'_id': key})

def monitor_redis_changes():
    pubsub = redis_client.pubsub()
    pubsub.psubscribe('__keyspace@0__:*')  # Subscribe to all key changes

    print("Monitoring Redis changes...")
    for message in pubsub.listen():
        if message['type'] == 'pmessage':
            full_key = message['channel'].split(':')[-2] + ":" + message['channel'].split(':')[-1]
            collection_name = message['channel'].split(':')[-2]
            key = message['channel'].split(':')[-1]
            event = message['data']
            
            if event in ['set', 'json.set']:
                # Use ReJSON to get the JSON value
                value = redis_client.jsonget(full_key, Path.rootPath())
                write_to_mongo(collection_name, key, value)
                print(f"Updated/Inserted: {collection_name}/{key} = {value}")
            elif event == 'del':
                write_to_mongo(collection_name, key, None)
                print(f"Deleted: {collection_name}/{key}")

if __name__ == "__main__":
    try:
        # Enable keyspace notifications for the desired events
        redis_client.config_set('notify-keyspace-events', 'KEA')
        monitor_redis_changes()
    except redis.exceptions.ConnectionError as e:
        print(f"Failed to connect to Redis: {e}")
        print("Please check your Redis connection settings and ensure the server is reachable.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
