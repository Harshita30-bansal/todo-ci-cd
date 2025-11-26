# CI/CD Pipeline – To-Do CLI for IMT2023035

This project implements a simple Python-based To-Do List CLI application for roll number **IMT2023035**.  
A complete CI/CD pipeline is built using **GitHub**, **Jenkins**, **Docker**, and **Docker Hub**.

## 🚀 Tech Stack
- Python 3
- pytest (unit testing)
- Docker (containerization)
- Jenkins (CI/CD automation)
- GitHub (source control)

## 🐳 Docker Hub Image
The Docker image built by Jenkins is available here:

👉 https://hub.docker.com/r/30301207/imt2023035-todo

## 📌 Pipeline Stages
1. Pull code from GitHub  
2. Install Python dependencies  
3. Run unit tests with pytest  
4. Build Docker image  
5. Push image to Docker Hub  

## 📁 Repository Structure
-app.py
-test_app.py
-requirements.txt
-Dockerfile
-Jenkinsfile
-README.md


## 👩‍💻 Run the container
docker run -it 30301207/imt2023035-todo
