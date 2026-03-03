# FastAPI Test Project

A simple RESTful API built with FastAPI and PostgreSQL, containerized with Docker.

production start with command

`docker compose up -d --build`

### Production url : `https://fast-api-test-users-service.smashty.com`  
Swagger ui : `https://fast-api-test-users-service.smashty.com/docs`

## 🚀 Features

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python 3.9+.
- **PostgreSQL**: Robust open-source relational database.
- **SQLAlchemy**: Powerful SQL toolkit and Object-Relational Mapping (ORM).
- **Docker & Docker Compose**: Easy setup and deployment using containers.
- **Swagger UI**: Interactive API documentation automatically generated.

## 🛠 Tech Stack

- Python 3.9
- FastAPI
- Uvicorn
- SQLAlchemy
- Psycopg2-binary
- Python-dotenv
- Docker / Docker Compose

## 📋 Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.

## ⚙️ Installation & Setup

1. **Clone the repository** (if applicable) or navigate to the project directory.
2. **Environment Configuration**
  Create a `.env` file in the root directory with the following variables:
  > **Note:** The `DB_HOST` in `.env` is set to `localhost` for local development. When running with Docker Compose, the application container overrides this to connect to the `db` service automatically.
3. **Run with Docker Compose**
  Start the application and database containers:
  - The API will be available at: `http://localhost:8801`
  - The API documentation (Swagger UI) will be at: `http://localhost:8801/docs`
4. **Stop the containers**
  To stop and remove the containers:

## 📖 API Endpoints


| Method | Endpoint | Description                    |
| ------ | -------- | ------------------------------ |
| `GET`  | `/`      | Health check / Welcome message |
| `GET`  | `/users` | Retrieve all users             |
| `POST` | `/users` | Create a new user              |


### Request Body for Creating User (POST /users)

```json
{
  "username": "johndoe",
  "email": "john@example.com"
}
```

## 📂 Project Structure

```
fastapi-test/
├── main.py              # Application entry point and logic
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image definition for the app
├── docker-compose.yml   # Docker services configuration (App + DB)
├── .env                 # Environment variables (Git-ignored)
└── README.md            # Project documentation
```

## 🔧 Local Development (Without Docker)

If you prefer to run the application locally without Docker:

1. **Create a virtual environment**:
  ```bash
    python3 -m venv venv
    source venv/bin/activate
  ```
2. **Install dependencies**:
  ```bash
    pip install -r requirements.txt
  ```
3. **Ensure PostgreSQL is running locally** and update `.env` with your local database credentials.
4. **Run the application**:
  ```bash
    uvicorn main:app --host 0.0.0.0 --port 8801 --reload
  ```