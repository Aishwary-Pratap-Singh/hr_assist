# hr_assist Project

## Overview
`hr_assist` is a Django-based web application designed to assist with human resources tasks. This project is containerized using Docker for easy deployment and management.

## Prerequisites
- Docker
- Docker Compose
- Python 3.x
- uv package manager

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd hr_assist
   ```

2. **Install dependencies:**
   ```
   uv install
   ```

3. **Build the Docker image:**
   ```
   docker-compose build
   ```

4. **Run the application:**
   ```
   docker-compose up
   ```

5. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000`.

## Usage
- To run migrations, use:
  ```
  docker-compose run web python manage.py migrate
  ```

- To create a superuser, use:
  ```
  docker-compose run web python manage.py createsuperuser
  ```

## Project Structure
```
hr_assist
├── hr_assist
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.