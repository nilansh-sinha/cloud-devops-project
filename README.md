# Secure Cloud-Native Application

A production-ready cloud-native application on AWS demonstrating CI/CD, Infrastructure as Code, Containerization, and Security best practices.

## 🧱 Architecture

```mermaid
graph TD
    User[User / Browser]
    ALB[Application Load Balancer]
    ASG[Auto Scaling Group]
    Docker[Docker Container<br/>(FastAPI App)]
    DB[(RDS / DynamoDB)]
    CloudWatch[CloudWatch Logs & Metrics]

    User -->|HTTPS| ALB
    ALB --> ASG
    ASG --> Docker
    Docker -->|Read / Write| DB
    Docker -->|Logs & Metrics| CloudWatch

## 🚀 Tech Stack

- **Cloud**: AWS (EC2/ECS, ALB, Auto Scaling, CloudWatch)
- **App**: Python FastAPI
- **Containerization**: Docker
- **IaC**: Terraform
- **CI/CD**: GitHub Actions

## 📂 Repository Structure

- `app/` - Python application source code.
- `docker/` - Dockerfile and container scripts.
- `terraform/` - Infrastructure definitions.
- `.github/workflows/` - CI/CD pipelines.
- `monitoring/` - Dashboard configs and alert definitions.

## 🛡 Security Highlights

- **Least Privilege**: IAM roles restricted to minimum necessary permissions.
- **Network Isolation**: App runs in private subnets; only ALB is public.
- **Secrets Management**: No hardcoded credentials.
- **Container Security**: Non-root user execution, multi-stage builds.

## ⚡ Deployment

### Prerequisites
- AWS CLI configured
- Terraform installed
- Docker installed

### Steps
1. **Build Container**: `docker build -t cloud-app ./docker`
2. **Infrastructure**: 
    ```bash
    cd terraform
    terraform init
    terraform apply
    ```
