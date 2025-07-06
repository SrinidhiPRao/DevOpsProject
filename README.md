\# 🚀 DevOps Final Project: CI/CD Pipeline for FastAPI App



This project demonstrates a complete DevOps workflow by building a CI/CD pipeline using Jenkins and deploying a containerized FastAPI application with observability (logging, metrics, visualization) and Kubernetes-based scaling with NGINX load balancing.



---



\## 🧰 DevOps Tools Used



| Tool           | Purpose                           |

|----------------|------------------------------------|

| \*\*Git\*\*        | Version Control                   |

| \*\*GitHub\*\*     | Remote Repository                 |

| \*\*Jenkins\*\*    | CI/CD Automation                  |

| \*\*Pip/Venv\*\*   | Dependency Management             |

| \*\*Docker\*\*     | Containerization                  |

| \*\*Pytest\*\*     | Unit Testing Framework            |

| \*\*Grafana\*\*    | Metrics \& Logs Visualization      |

| \*\*Prometheus\*\* | Application Metrics               |

| \*\*Loki\*\*       | Application Logging               |

| \*\*Kubernetes\*\* | Container Orchestration           |

| \*\*Minikube\*\*   | Local Kubernetes Cluster          |

| \*\*Kubectl\*\*    | Kubernetes CLI                    |

| \*\*NGINX\*\*      | Load Balancer                     |

| \*\*FastAPI\*\*    | Python Web Framework              |

| \*\*Uvicorn\*\*    | ASGI Server for FastAPI           |



---



\## ⚙️ Tech Stack



\- \*\*Language\*\*: Python

\- \*\*Framework\*\*: FastAPI

\- \*\*Web Server\*\*: Uvicorn

\- \*\*Data Validation\*\*: Pydantic

\- \*\*Testing\*\*: Pytest



---



\## 📁 Project Structure



```



.

├── .github/             # GitHub configuration (if any)

├── app/

│   └── main.py          # FastAPI Application

├── tests/

│   └── test\\\_main.py     # Pytest Tests

├── Dockerfile           # Docker image for FastAPI app

├── docker-compose.monitoring.yml   # Loki, Prometheus, Grafana setup

├── docker-compose.jenkins.yml      # Jenkins setup

├── prometheus.yml       # Prometheus Configuration

├── promtail-config.yml  # Promtail Configuration for Loki

├── Jenkinsfile          # Jenkins CI Pipeline

├── k8s/

│   ├── fastapi-deployment.yaml

│   ├── fastapi-service.yaml

│   ├── nginx-configmap.yaml

│   ├── nginx-deployment.yaml

│   └── nginx-service.yaml

└── requirements.txt     # Python dependencies



````



---



\## 🔧 Step-by-Step Setup



\### 1. 📁 Initialize Git Repository

```bash

git init

git remote add origin <your-repo-url>

git add .

git commit -m "Initial commit"

git push -u origin main

````



---



\### 2. 🐍 Create Python Virtual Environment



```bash

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

```



---



\### 3. 🚀 Create FastAPI App (`main.py`)



Define API endpoints using FastAPI and validate data using Pydantic.



---



\### 4. 🐳 Set Up Monitoring Stack with Docker Compose



```bash

docker-compose -f docker-compose.monitoring.yml up -d

```



\* Grafana: `http://localhost:3000`

\* Prometheus: `http://localhost:9090`

\* Loki: `http://localhost:3100`



---



\### 5. 📊 View Logs in Grafana via Loki



\* Configure Loki as a Grafana data source.

\* Visualize logs collected via Promtail from FastAPI.



---



\### 6. 📈 View Metrics in Grafana via Prometheus



\* Expose `/metrics` endpoint in FastAPI.

\* Add Prometheus as a data source in Grafana.

\* Create dashboards for request count, latency, etc.



---



\### 7. ✅ Run Unit Tests with Pytest



```bash

pytest

```



---



\### 8. 🔁 Set Up CI with Jenkins



```bash

docker-compose -f docker-compose.jenkins.yml up -d

```



\* Access Jenkins at: `http://localhost:8080`

\* Unlock with initial admin password from container logs.



\*\*Jenkinsfile Pipeline Stages:\*\*



1\. Clone repo from GitHub.

2\. Setup virtual environment.

3\. Install Python dependencies.

4\. Run unit tests.

5\. Launch FastAPI in background.

6\. Validate using `curl`.

7\. Stop the app.



---



\### 9. ☸️ Deploy with Kubernetes (Minikube)



Start minikube and apply Kubernetes manifests:



```bash

minikube start

kubectl apply -f k8s/

minikube service nginx-service

```



\* \*\*FastAPI Pods\*\*: `fastapi-deployment.yaml`

\* \*\*Internal Service\*\*: `fastapi-service.yaml`

\* \*\*NGINX Load Balancer\*\*: `nginx-deployment.yaml`, `nginx-service.yaml`

\* \*\*Routing Config\*\*: `nginx-configmap.yaml`



Access the application at the external URL provided by `minikube service`.



---



\## 📊 Observability Dashboard



Once set up, Grafana provides a unified dashboard with:



\* Logs from Loki

\* Metrics from Prometheus

\* Custom dashboards for request stats, latency, and errors



---



\## ✅ Conclusion



This project demonstrates a production-like DevOps pipeline from \*\*code commit to deployment\*\* with \*\*observability\*\* and \*\*Kubernetes orchestration\*\*. It integrates multiple DevOps tools and concepts such as:



\* CI/CD automation with Jenkins

\* Monitoring with Prometheus, Grafana

\* Logging with Loki

\* Docker + Kubernetes deployment



---



\## 📌 Author



Srinidhi Rao

📫 \[GitHub](https://github.com/SrinidhiPRao) • 🌐 \[LinkedIn](https://www.linkedin.com/in/srinidhi-p-rao-4861442b7/)





