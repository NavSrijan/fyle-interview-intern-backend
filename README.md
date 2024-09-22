# Running the Flask App with Docker

This section describes how to run the Flask application using Docker after cloning the repository.

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started) (including Docker Compose)

## Cloning the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/NavSrijan/fyle-interview-intern-backend
cd https://github.com/NavSrijan/fyle-interview-intern-backend
```

## Building the Docker Image

1.  Navigate to the project directory (if you haven’t already):

```bash
cd <repository-directory>
```

2. Build the Docker image without using the cache to ensure you have the latest changes:

```bash
    docker-compose build 
```

## Running the Application

To start the application, run:


```bash
docker-compose up
```

This command will:

- Start the Flask server on port 7755.
- Run the application using the run.sh script defined in the Dockerfile.

## Accessing the Application

Once the containers are running, you can access the Flask application in your web browser at:

```bash
http://0.0.0.0:7755
```

## Stopping the Application

To stop the running application, you can press CTRL+C in the terminal where docker-compose up is running. Alternatively, you can run:

```bash
docker-compose down
```

This will stop and remove the containers.
