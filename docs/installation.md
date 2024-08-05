# Installation

## Prerequisites

- Docker
- Docker Compose

## Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/saisurajch/MongoDBRedisReplication.git
    cd MongoDBRedisReplication
    ```

2. Copy the example environment file and fill in your own credentials:
    ```bash
    cp .env.example .env
    ```

    Open the `.env` file and update the values with your own MongoDB and Redis configuration:
    ```env
    # MongoDB configuration
    MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/dbname?retryWrites=true&w=majority
    MONGODB_DB_NAME=replication

    # Redis configuration
    REDIS_HOST=redis-16337.c212.ap-south-1-1.ec2.redns.redis-cloud.com
    REDIS_PORT=16337
    REDIS_PASSWORD=y4pKKclll2R65xyOEzhQRumEkVDNZHXR
    ```

3. Build and start the Docker containers:
    ```bash
    sudo docker-compose up --build
    ```

4. The application will start monitoring Redis changes and replicating them to MongoDB.
