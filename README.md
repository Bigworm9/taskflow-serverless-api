# Serverless Task API with Queue-Based Processing

**Project Date:** May 26, 2025  
**Author:** Juan (AWS Cloud Architect)

## 🚀 Project Overview

This project demonstrates how to re-architect a basic task submission API into a fully decoupled, serverless architecture using core AWS services. It highlights best practices in queue-based processing, Lambda orchestration, and event-driven workflows.

---

## 📌 Architecture

![Serverless Task Architecture](./Serverless%20Task%20Architecture2.drawio.png)

```
Client --> API Gateway --> Lambda (create_task) --> SQS --> Lambda (process_task) --> DynamoDB (TaskTable)
```

- **API Gateway**: Exposes a POST `/task` endpoint.
- **create_task Lambda**: Accepts incoming task requests, validates data, and sends messages to SQS.
- **Amazon SQS**: Buffers task messages and decouples ingestion from processing.
- **process_task Lambda**: Triggered by SQS, processes task messages and inserts them into DynamoDB.
- **DynamoDB**: Stores task records with status and metadata.
- **CloudWatch Logs**: Captures logs for both Lambda functions.

---

## 🗓️ 3-Day Execution Plan

| Day | Tasks |
|-----|-------|
| 1   | Project setup, `create_task` Lambda, API Gateway, DynamoDB |
| 2   | Add SQS, refactor `create_task` to publish to SQS, create `process_task` Lambda |
| 3   | Connect SQS to `process_task`, finalize deployment, testing, CloudWatch verification, and cleanup |

---

## 📂 Folder Structure

```
taskflow-serverless-api/
├── create_task/
│   └── lambda_function.py
├── process_task/
│   └── lambda_function.py
├── architecture.png
├── README.md
```

---

## 🧠 Environment Variables

| Function       | Variable         | Purpose              |
|----------------|------------------|----------------------|
| create_task    | `SQS_QUEUE_URL`  | Dynamically resolves queue destination |

---

## ✅ Key AWS Services Used

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SQS
- AWS IAM
- AWS CloudWatch

---

## 🔐 IAM Roles & Policies

- `create_task-role`:
  - `AmazonSQSFullAccess`
  - `AWSLambdaBasicExecutionRole`

- `process_task-role`:
  - `AmazonDynamoDBFullAccess`
  - `AmazonSQSFullAccess`
  - `AWSLambdaBasicExecutionRole`

> **Note:** Full access policies were intentionally used during this demo to avoid permission issues and streamline development. In a production environment, these would be replaced with fine-grained policies (e.g., `sqs:SendMessage`, `dynamodb:PutItem`) following the principle of least privilege.

---

## 🧪 Testing & Logs

- Test events were triggered using the Lambda Console.
- Logs verified via **CloudWatch > Log Groups** for:
  - `/aws/lambda/create_task`
  - `/aws/lambda/process_task`
- DynamoDB entries confirmed using the **Explore items** tab.

---

## 🛠️ Troubleshooting Notes

- **SQS SendMessage Access Denied**  
  During testing of the `create_task` Lambda, an `AccessDeniedException` occurred while attempting to send messages to the SQS queue.  
  ✅ **Fix:** Manually attached an inline IAM policy to the Lambda execution role allowing `sqs:SendMessage` to the specific queue ARN.  
  🔒 **Best Practice:** This approach maintains security by keeping sensitive queue ARNs and permissions out of the function code and handling them through IAM. Adding permissions directly in the script would have exposed infrastructure details and is not recommended.

---

## 🧹 Cleanup Steps (Post-Demo)

You may delete:
- Lambda functions (`create_task`, `process_task`)
- SQS queue (`taskQueue`)
- DynamoDB table (`TaskTable`)
- IAM roles created during the demo
- CloudWatch log groups (optional)

---

## 📸 Screenshots

- `cloudwatch_lambda_process_task_output.png`: Shows successful task processing
- `taskTable_final_insert_success.png`: Confirms data landed in DynamoDB

---

## 🧾 Outcome Statement

> “In 3 days, I designed and deployed a fully decoupled serverless task processor using AWS Lambda, API Gateway, SQS, and DynamoDB. This pipeline handles incoming tasks asynchronously with full observability, least-privilege access, and production-ready architecture patterns.”

---

## 🔗 License
