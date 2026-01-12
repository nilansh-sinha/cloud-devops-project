variable "aws_region" {
  description = "AWS Region to deploy to"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project Name"
  default     = "cloud-native-app"
}

variable "ami_id" {
  description = "AMI ID for EC2 instances (Amazon Linux 2023)"
  # Amazon Linux 2023 AMI in us-east-1
  default     = "ami-0230bd60aa48260c6" 
}
