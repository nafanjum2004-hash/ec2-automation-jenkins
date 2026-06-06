terraform {
  backend "s3" {
    bucket = "nafreen-terraform-state-bucket"
    key    = "ec2-automation-jenkins/terraform.tfstate"
    region = "ap-southeast-1"
  }
}