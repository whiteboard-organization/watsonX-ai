# EKS Cluster Infrastructure as Code (IaC)

This repository contains Terraform configuration files to create and manage an Elastic Kubernetes Service (EKS) cluster on AWS. The IaC defines the infrastructure components, including VPC, subnets, security groups, EKS cluster, and managed node groups.

## Prerequisites

- Terraform installed and configured
- AWS CLI and AWS credentials set up
- AWS account with Elastic Kubernetes Service (EKS) enabled

## Resources

- `main.tf`: Defines the EKS cluster and its components
- `provider.tf`: Provides the AWS provider configuration
- `backend.tf`: Configures the backend storage (S3) for storing the Terraform state

## Configuration

The main.tf file contains the configuration for the EKS cluster, including the name, region, public and private subnets, tags, and managed node groups.

1. Locals block: Defines the name and region for the EKS cluster.
2. Public and private subnets: Specify the subnets for the control plane and worker nodes.
3. Tags: Add custom tags to the EKS cluster and managed node groups.

The `eks_managed_node_groups` block defines the managed node groups with desired size, instance types, and capacity type.

## Example Usage

To create an EKS cluster using this IaC, run the following command:

```bash
terraform init
terraform apply
```

This will initialize the Terraform workspace, apply the changes to your AWS account, and create the EKS cluster.

## Cleanup

To destroy the EKS cluster, run the following command:

```bash
terraform destroy
```

## Notes

- This IaC creates a single-cluster setup with one control plane and multiple worker nodes.
- You can customize the configuration to meet your specific requirements, such as adding more managed node groups, adjusting instance types, or modifying the VPC and subnet settings.

For more information, consult the [Terraform EKS documentation](https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest) and the [AWS EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).