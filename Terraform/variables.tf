variable "username" {
  description = "The username for the DB master user"
  type        = string
  sensitive   = true
}
variable "password" {
  description = "The password for the DB master user"
  type        = string
  sensitive   = true
}

variable "region" {
  description = "aws region"
  default     = "us-east-2"
}

variable "account_id" {
  default = 727477891012
}

variable "environment" {
  default = "dev"
}

variable "prefix" {
  description = "objects prefix"
  default     = "de-okkus"
}

# Prefix configuration and project common tags
locals {
  prefix = var.prefix
  common_tags = {
    Environment = "dev"
    Project     = "okonomikus"
  }
}

variable "bucket_names" {
  description = "s3 bucket names"
  type        = list(string)
  default = [
    "landing-zone",
    "bronze-layer",
    "silver-layer",
    "gold-layer",
    "terraform",
    "scripts"
  ]
}

variable "year" {
  description = "year index"
  default     = "2023"
}