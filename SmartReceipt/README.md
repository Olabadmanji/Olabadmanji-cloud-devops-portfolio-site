📄 Project Title

Automated Receipt Processing System on AWS

🧠 Project Overview

This project demonstrates a serverless, event-driven receipt processing pipeline built on AWS.
When a receipt is uploaded to Amazon S3, the system automatically extracts text data, processes it, and stores structured information for further analysis.

The solution is designed to simulate a real-world backend automation system commonly used in finance, accounting, and expense management platforms.

🏗️ Architecture Overview

The system follows an event-driven serverless architecture:

A receipt file is uploaded to a private Amazon S3 bucket

The upload triggers an AWS Lambda function

Lambda processes the file and sends it to Amazon Textract for OCR

Extracted data is cleaned and structured

Final data is stored in Amazon DynamoDB

Optional processed output is archived in an S3 output bucket

Logs and monitoring are handled by Amazon CloudWatch

🧩 AWS Services Used

Amazon S3 – Secure storage for receipt uploads and processed outputs

AWS Lambda – Serverless processing and orchestration

Amazon Textract – Optical Character Recognition (OCR)

Amazon DynamoDB – Storage for structured receipt data

Amazon CloudWatch – Logging and monitoring

IAM – Secure role-based access control

🔄 Workflow (Step-by-Step)

User uploads a receipt (PDF/JPG/PNG) to the input S3 bucket

S3 event notification triggers the Lambda function

Lambda validates the file and sends it to Textract

Textract extracts text and returns OCR results

Lambda parses key receipt data:

Vendor name

Date

Amount

Parsed data is stored in DynamoDB

Processed output is optionally saved as JSON in an S3 output bucket

Execution logs are captured in CloudWatch

🔐 Security Design

S3 bucket public access is disabled

IAM roles follow least privilege principle

No hardcoded credentials

Lambda execution role restricted to required services only

📊 Monitoring & Observability

CloudWatch Logs for Lambda execution

Error handling with descriptive log messages

Easily extensible for alerts via SNS

🧪 How to Test the System

Upload a receipt file to the input S3 bucket

Verify Lambda execution in CloudWatch logs

Check DynamoDB for extracted receipt data

Confirm processed output in the output S3 bucket (if enabled)

📸 Proof of Execution

Screenshots included in this repository:

S3 upload event

Lambda execution logs

DynamoDB records

Textract output

🚀 Future Enhancements

Add API Gateway for manual uploads

Integrate Amazon SNS for notifications

Build a dashboard using Amazon QuickSight

Add cost optimization and alerts

👤 Author

Olabanji
Cloud / DevOps Engineer
AWS • Serverless • Automation