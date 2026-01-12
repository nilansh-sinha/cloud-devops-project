# Secure Cloud-Native Application

![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20ALB%20%7C%20ASG-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-Python-green)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-black)

A production-ready cloud-native application on AWS demonstrating CI/CD, Infrastructure as Code, Containerization, Monitoring, and Security best practices.

---

## Architecture

```
User
  |
  v
Application Load Balancer
  |
  v
Auto Scaling Group
  |
  v
FastAPI Application (Docker)
  |
  +--> Database (RDS / DynamoDB)
  |
  +--> Monitoring (CloudWatch / Prometheus)
```

---

## Tech Stack

### Cloud
- AWS EC2
- Application Load Balancer
- Auto Scaling Group
- CloudWatch

### Application
- Python
- FastAPI

### Containerization
- Docker

### Infrastructure as Code
- Terraform

### CI/CD
- GitHub Actions

### Monitoring
- Prometheus
- CloudWatch

---

## Repository Structure

```
cloud-devops-project/
├── app/                # FastAPI source code
├── docker/             # Dockerfile
├── terraform/          # Infrastructure as Code
├── monitoring/         # Prometheus configs
├── .github/workflows/  # CI/CD pipelines
├── local_test.sh
└── README.md
```

---

## Security Highlights

- Least privilege IAM roles
- Application runs in private subnets
- No hardcoded secrets
- Non-root Docker containers
- Secure CI/CD pipeline

---

## Run Locally

```bash
git clone https://github.com/nilansh-sinha/cloud-devops-project.git
cd cloud-devops-project

docker build -t cloud-devops-app ./docker
docker run -p 8000:8000 cloud-devops-app
```

Access the application:
```
http://localhost:8000
```

---

## Author

**Nilansh Sinha**  
B.Tech – Cyber Security  
VIT Vellore  

GitHub: https://github.com/nilansh-sinha
