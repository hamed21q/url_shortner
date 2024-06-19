# URL Shortener Service

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/fastapi-0.65+-brightgreen.svg)

## Overview

Welcome to the URL Shortener Service! This project provides a simple and efficient way to shorten long URLs, making them easier to share and manage. The service is built using Python and FastAPI, ensuring high performance and scalability.

## Features

- **Fast and Reliable**: Built with FastAPI for high performance.
- **Database Integration**: Supports SQLite out-of-the-box, can be extended to use other databases.
- **RESTful API**: Provides a RESTful interface for creating and managing shortened URLs.
- **Docker Support**: Easily deployable using Docker and Docker Compose.
- **Auto-Migrations**: Automatically apply database migrations using Alembic.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/url-shortener-service.git
    cd url-shortener-service
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run database migrations:**

    ```bash
    alembic upgrade head
    ```

4. **Start the application:**

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

5. **Access the API:**

    Open your browser and navigate to `http://localhost:8000/docs` to explore the API documentation.

### Docker Deployment

1. **Build and run the Docker container:**

    ```bash
    docker-compose up --build
    ```

2. **Access the API:**

    Open your browser and navigate to `http://localhost:6060/docs` to explore the API documentation.

## Usage

### Create a Short URL

```bash
POST /shorten?url=https://google.com'
```
