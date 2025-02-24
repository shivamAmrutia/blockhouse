# Blockhouse work trial
# name: shivam amrutia (sa8572@nyu.edu)

This project is a simple trade order management backend built with FastAPI. It supports REST APIs for submitting and retrieving trade orders, WebSocket support for real-time order updates, and deployment using Docker on AWS EC2 with a CI/CD pipeline via GitHub Actions.

## Features
- REST API for submitting and retrieving trade orders.
- WebSocket support for real-time order status updates.
- SQLite for lightweight database storage.
- Containerized using Docker.
- CI/CD pipeline with GitHub Actions for automated deployment on AWS EC2.

## Installation

### Prerequisites
- Python 3.10+
- Docker
- Git

### Setup
```sh
git clone <repository-url>
cd <repository-folder>
```

### Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies
```sh
pip install -r requirements.txt
```

### Run database migrations
```sh
python -m app.models  # This ensures tables are created
```

### Start the FastAPI server
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### Orders API
- **POST /orders**: Submit a new order.
- **GET /orders**: Retrieve all submitted orders.

### WebSocket
- **/ws**: Subscribe for real-time order status updates.

## Running with Docker

### Build and Run Container
```sh
docker build -t fastapi-tradeservice .
docker run -d -p 8000:8000 --name fastapi-container fastapi-tradeservice
```

## Deployment on AWS EC2
1. Launch an Ubuntu EC2 instance and install Docker.
2. Set up SSH access and configure GitHub Actions secrets.
3. Use the provided GitHub Actions workflow for automatic deployment on push to `main`.

## CI/CD Pipeline
- Runs tests on pull requests.
- Deploys the latest version to AWS EC2 on merge to `main`.


