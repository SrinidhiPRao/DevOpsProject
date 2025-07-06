# 🚀 DevOps Final Project: CI/CD Pipeline for a FastAPI Application

This project demonstrates a complete DevOps pipeline using **Jenkins**, **Docker**, **Kubernetes**, and **FastAPI**, complete with observability through **Prometheus**, **Loki**, and **Grafana**.

---

## 🛠️ Project Overview

This system automates the **build**, **test**, **deploy**, and **monitor** stages of a FastAPI-based microservice using modern DevOps tools and practices.

### ✨ Features
- CI/CD pipeline with Jenkins
- Unit testing with Pytest
- Containerization using Docker
- Real-time metrics with Prometheus
- Log aggregation using Loki
- Dashboards in Grafana
- Deployment using Kubernetes (via Minikube)
- NGINX as Kubernetes Load Balancer

---

## ⚙️ Tools & Technologies

| Category        | Tools / Stack                              |
|----------------|---------------------------------------------|
| **Language**    | Python, FastAPI, Uvicorn, Pydantic         |
| **CI/CD**       | Git, GitHub, Jenkins                       |
| **Testing**     | Pytest                                     |
| **Containers**  | Docker, Docker Compose                     |
| **Monitoring**  | Prometheus (metrics), Grafana (dashboard)  |
| **Logging**     | Loki, Promtail                             |
| **Orchestration** | Kubernetes, Minikube, Kubectl            |
| **Load Balancer** | NGINX (inside Kubernetes)               |

---

## 📦 Components

### 🔹 FastAPI Application
A simple web API built using FastAPI, exposing:
- Health check endpoint
- Example data model and route
- Prometheus metrics at `/metrics`

### 🔹 Jenkins CI Pipeline
Defined in `Jenkinsfile`, includes:
- Cloning from GitHub
- Virtual environment setup
- Package installation via pip
- Running tests with pytest
- Starting FastAPI server
- Validating with `curl`
- Stopping the app

### 🔹 Docker & Docker Compose
- `Dockerfile` for FastAPI app
- `docker-compose.monitoring.yml` for Loki + Prometheus + Grafana
- `docker-compose.jenkins.yml` for Jenkins

### 🔹 Kubernetes Deployment
- `fastapi-deployment.yaml` for pods
- `fastapi-service.yaml` for internal service
- `nginx-deployment.yaml` as a load balancer
- `nginx-service.yaml` to expose NGINX
- `nginx-configmap.yaml` for routing rules

---

## 📊 Observability

**Grafana Dashboards** provide:
- Real-time metrics from Prometheus
- Centralized logs via Loki
- Unified monitoring interface

---

## ✅ Status

- [x] CI/CD with Jenkins
- [x] Dockerized App & Services
- [x] Unit Testing & Linting
- [x] Kubernetes Deployment
- [x] Logs & Metrics Integration
- [x] NGINX Load Balancer

---

## 👤 Author

Srinidhi Rao  
📫 [GitHub](https://github.com/SrinidhiPRao) • 🌐 [LinkedIn](https://www.linkedin.com/in/srinidhi-p-rao-4861442b7/)

