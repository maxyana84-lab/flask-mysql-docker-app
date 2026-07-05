# Flask & MySQL Hit-Counter Application

A simple and robust web application built with Python (Flask) and MySQL database, fully containerized using Docker and Docker Compose. The application uses a custom bridge network for secure container communication and automatically increments a page view counter on every visit.

## Features

- **Flask Backend:** Serves the web interface and communicates with the database.
- **MySQL Database:** Safely stores the page view count.
- **Dockerized Environment:** Both services run in isolated containers.
- **Custom Network:** Services communicate securely using a dedicated Docker bridge network.

## Project Structure

- `main.py` - Flask web application with automatic DB connection retry logic.
- `docker-compose.yml` - Multi-container Docker orchestration file.
- `Dockerfile` - Blueprint for the Flask service image.
- `init.sql` - Database initialization script.

## How to Run

1. Make sure you have **Docker** and **Docker Compose** installed.
2. Clone this repository and navigate to the project folder.
3. Start the application by running:
   ```bash
   docker compose up --build
