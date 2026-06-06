variable "role_arn" {
  type = string
}

variable "lambda_function_name" {
  type = string
}

variable "lambda_handler" {
  type = string
}

variable "lambda_runtime" {
  type = string
}

variable "lambda_timeout" {
  type = number
}

variable "lambda_zip" {
  type = string
}
variable "ami_id" {
  type = string
}

variable "instance_type" {
  type = string
}

variable "key_name" {
  type = string
}

variable "aws_region" {
  type = string
}