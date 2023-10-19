# AWS Lambda Connectivity Checker
Simple connectivity checking Lambda that takes a URL in the input event. 

To install the packages:
`poetry install`

To build the zip file:
`bash publish.sh`

Create a lambda function in the AWS console and upload the zip file.

Change the handler of the lambda to:
`lambda_connectivity_checker.handler.lambda_handler`

Test with an event containing a URL: 

`{
  "url": "http://www.madetech.com"
}`
