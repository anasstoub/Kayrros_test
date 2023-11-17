# Kayrros_test
Kayrros Intern DevOps Technical test


# FastAPI Application on AWS with Terraform

This repository contains code for deploying a FastAPI application on an AWS EC2 instance using Terraform. The FastAPI application retrieves the latest CO2 emission data for Europe from a provided CSV file.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed on your local machine.
- AWS CLI configured with valid credentials.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/anasstoub/Technical_test.git
cd Technical_test
```

### Configure AWS Credentials
```bash
aws configure

```

### 3. Update Terraform Variables
Open the main.tf file and update the following variables:

region: Set to your preferred AWS region (e.g., "eu-west-3").
ami: Set to a suitable AMI for your region and instance type.
key_name: Set to the name of your SSH key pair.

### 4. Deploy the Infrastructure
```bash
terraform init
terraform apply
```
### 5. Connect to the EC2 Instance
After the deployment is complete, use SSH to connect to your EC2 instance

### 6. Connect to the EC2 Instance Cleanup
```bash
terraform destroy
```