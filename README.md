# Infrastructure Provisioning Experiments

This repository contains practical experiments for infrastructure provisioning using **Terraform** and **Python automation with Boto3** on **AWS**.

The objective of the project is to explore different approaches to Infrastructure as Code (IaC) and programmatic cloud resource management.

---

## Overview

The repository demonstrates two methods of managing cloud infrastructure on AWS:

1. **Terraform (Infrastructure as Code)**  
   Declarative infrastructure provisioning using Terraform.

2. **Python + Boto3 (Programmatic provisioning)**  
   Imperative automation scripts using the AWS SDK for Python.

These experiments help understand how infrastructure can be provisioned, modified, and destroyed automatically.

---

## Repository Structure

System_provisioning/
│
├── exp_first_ec2.tf
│   Terraform configuration for provisioning an EC2 instance
│
├── exp_createEC2.py
│   Python script to create an EC2 instance using Boto3
│
├── exp_terminateEC2.py
│   Python script to terminate EC2 instances
│
├── exp_manageS3.py
│   Script for managing S3 buckets using Boto3
│
├── exp_iam_manage.py
│   Script for IAM resource management
│
└── infrastructure-provider-message.txt


Terraform state files and temporary artifacts are excluded from version control through `.gitignore`.

---

## Technologies Used

- Python
- Terraform
- AWS CLI
- Boto3

Cloud provider:

- AWS (Amazon Web Services)

---

## Prerequisites

Before running the experiments, ensure the following tools are installed:

- Terraform
- AWS CLI
- Python 3
- Boto3

AWS credentials must also be configured:

```bash
aws configure

```
## Terraform Workflow

The Terraform experiment provisions an EC2 instance.

Typical execution steps:

```bash
terraform init
terraform plan
terraform apply
terraform destroy
```

### Explanation

- **terraform init** – Initializes the Terraform project and downloads the required providers.
- **terraform plan** – Shows the infrastructure changes Terraform intends to perform.
- **terraform apply** – Provisions the resources defined in the configuration.
- **terraform destroy** – Removes the created infrastructure.


## Learning Objectives

This project demonstrates:

- Infrastructure as Code (IaC)
- Cloud automation practices
- AWS resource provisioning
- Terraform workflows
- AWS SDK usage with Python

---

## License

This project is intended for educational and experimental purposes.