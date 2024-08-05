# Usage

The application monitors Redis keyspace changes and replicates them to MongoDB. To use the application, ensure that your Redis and MongoDB instances are properly configured.

## Configuration

Update the MongoDB URI and Redis configuration in `main.py` if needed.

```python
# MongoDB configuration
mongo_client = MongoClient('your_mongodb_uri')
mongo_db = mongo_client['your_database']

# Redis configuration
redis_client = Client(host='your_redis_host', port=your_redis_port, password='your_redis_password', decode_responses=True)
