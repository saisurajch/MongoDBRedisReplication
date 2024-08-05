# MongoDBRedisReplication

MongoDBRedisReplication is a Python-based tool that provides write-behind replication from Redis to MongoDB. It monitors changes in Redis and updates MongoDB collections accordingly.

## Features

- Monitor Redis keyspace changes
- Write updates to MongoDB collections
- Support for multiple collections
- Dockerized for easy deployment

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MongoDBRedisReplication.git
    cd MongoDBRedisReplication
    ```

2. Build and start the Docker containers:
    ```bash
    sudo docker-compose up --build
    ```

## Usage

The application monitors Redis for keyspace changes and replicates them to MongoDB. To use the application, ensure that your Redis and MongoDB instances are properly configured.

## Configuration

- Update the MongoDB URI and Redis configuration in `main.py` if needed.

## Contributing

We welcome contributions! Please see the [contributing guidelines](docs/contributing.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
