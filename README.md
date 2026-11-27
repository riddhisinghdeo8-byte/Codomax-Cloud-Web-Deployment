# Codomax Cloud Web Deployment

## Project Overview
A local cloud deployment simulation developed as part of the Codomax Digital Solutions Cloud Computing & DevOps Internship.

## Technologies Used
- Python and Flask
- Docker and Docker Volumes
- RustFS Object Storage
- SQLite Database
- Docker Networking
- Environment Variables

## Features
- Flask-based Cloud Task Manager
- Containerized application deployment
- Persistent database storage
- S3-compatible object storage using RustFS
- Storage bucket creation and file uploads
- Docker virtual networking
- CPU and memory resource limits
- Application and storage log monitoring
- IAM role and permission policy demonstration

## Resource Configuration
- CPU limit: 1 CPU
- Memory limit: 512 MB
- Application port: 5000
- Storage console port: 9001

## Run Locally
```bash
docker start codomax-container
```

Application: http://localhost:5000

RustFS Console: http://localhost:9001

## Project Note
This project demonstrates cloud infrastructure concepts through locally running Docker services. It is a cloud deployment simulation, not a deployment to a public cloud provider.