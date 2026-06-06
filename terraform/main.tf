module "iam" {
  source = "./modules/iam"

  role_name = var.role_name
}

module "lambda" {
  source = "./modules/lambda"

  role_arn = module.iam.role_arn

  lambda_function_name = var.lambda_function_name
  lambda_handler       = var.lambda_handler
  lambda_runtime       = var.lambda_runtime
  lambda_timeout       = var.lambda_timeout

  lambda_zip = "../lambda/lambda.zip"

  ami_id        = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  aws_region    = var.aws_region
}