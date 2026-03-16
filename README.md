# Azure AKS CI/CD Platform

This project demonstrates a simple cloud-native platform using FastAPI, Docker, GitHub Actions, Kubernetes, and Terraform on Azure.

## Overview
The goal of this project is to show how an application moves from source code to a running container inside Kubernetes with autoscaling.

Code is pushed to GitHub →  
GitHub Actions runs tests and builds a Docker image →  
The application runs in Kubernetes →  
Autoscaling is handled with a Horizontal Pod Autoscaler.

## Technologies
- Python (FastAPI)
- Docker
- GitHub Actions (CI/CD)
- Kubernetes
- Terraform
- Azure

## Project Structure
.github/workflows/ → CI pipeline  
app/ → FastAPI application  
infra/terraform/ → Terraform infrastructure  
k8s/ → Kubernetes manifests  
README.md → Project documentation  

## Kubernetes Components
This project deploys the application using:

- Deployment – runs the container
- Service – exposes the application internally
- Horizontal Pod Autoscaler – scales pods based on CPU usage

## Infrastructure (Terraform)
Terraform provisions Azure resources such as:

- Resource Group
- Storage Account
- Azure Container Registry

## Future Improvements
Possible next improvements:

- Deploy automatically to Azure Kubernetes Service (AKS)
- Push images to Azure Container Registry
- Add monitoring (Prometheus/Grafana)
- Add security scanning to the CI pipeline