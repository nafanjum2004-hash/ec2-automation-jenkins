resource "aws_lambda_function" "ec2_creator" {

  function_name = var.lambda_function_name

  filename         = var.lambda_zip
  source_code_hash = filebase64sha256(var.lambda_zip)

  role = var.role_arn

  handler = var.lambda_handler

  runtime = var.lambda_runtime

  timeout = var.lambda_timeout

 environment {
  variables = {
    AMI_ID        = var.ami_id
    INSTANCE_TYPE = var.instance_type
    KEY_NAME      = var.key_name
    REGION_NAME   = var.aws_region
  }
}
}