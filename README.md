# Flask MySQL Docker App

A simple Flask web application with a page view counter stored in a MySQL database. The application is packaged in Docker containers and automatically deployed to an AWS EC2 server through a GitHub Actions CI/CD pipeline.

## Project Structure

- main.py — Flask application code
- docker-compose.yml — defines the web (Flask) and db (MySQL) services
- Dockerfile — builds the application image
- init.sql — initializes the counter table in the database
- deploy-playbook.yml — Ansible playbook for server deployment
- inventory.ini — server address used by Ansible

## How It Works

On every push to the main branch, a GitHub Actions workflow runs automatically that:

1. Builds the Docker image of the application and pushes it to DockerHub
2. Connects to the AWS EC2 server via SSH
3. Runs an Ansible playbook that copies the configuration files to the server and starts the containers with docker compose

This means a manual "docker compose up --build" run is not required in production — the application image is already built and published on DockerHub, and the server pulls the ready-made image and runs it alongside the database.

## Running Locally

To run the project locally for development, you can use: docker compose up --build

This will build the application image from source locally instead of using the image from DockerHub.

## Accessing the App

After a successful deployment, the application is available at the server's address on port 8080.
