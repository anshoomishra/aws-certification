# AWS Certification and Python SDK Practical Roadmap

This guide is a complete, project-based roadmap for learning AWS and preparing for certification with Python. It is written to support the common progression:

1. **AWS Certified Cloud Practitioner** — optional foundation
2. **AWS Certified Solutions Architect – Associate** — recommended first technical certification
3. **AWS Certified Developer – Associate** or **AWS Certified SysOps Administrator – Associate** — choose according to your role
4. **Professional or Specialty certification** — take after building real depth and operating production-like systems

AWS changes exam versions and domains periodically. Always compare this roadmap with the current exam guide and official exam page before booking an exam.

## 1. Certification paths

| Goal | Suggested path | Main emphasis |
|---|---|---|
| General AWS literacy | Cloud Practitioner | Cloud concepts, core services, security, billing, support |
| Cloud architecture | Solutions Architect – Associate → Solutions Architect – Professional | Resilient, secure, cost-effective designs |
| Application development | Developer – Associate → DevOps Engineer – Professional | Code, APIs, CI/CD, serverless, observability |
| Cloud operations | SysOps Administrator – Associate → DevOps Engineer – Professional | Deployment, monitoring, automation, incident response |
| Data and analytics | Data Engineer – Associate → Data Analytics Specialty | Ingestion, storage, transformation, governance |
| Machine learning | Machine Learning Engineer – Associate → Machine Learning Specialty | ML workloads, deployment, monitoring, responsible AI |
| Security | Security – Specialty | Identity, detection, infrastructure and data protection, incident response |
| Networking | Advanced Networking – Specialty | Hybrid connectivity, routing, DNS, multi-account networking |
| SAP workloads | SAP on AWS – Specialty | SAP architecture, migration, operations and optimization |

The associate certifications share a large foundation. Learn the common syllabus first, then add the role-specific section for your target exam.

## 2. Complete common AWS syllabus

### A. Cloud and AWS fundamentals

- Regions, Availability Zones, edge locations, Local Zones and wavelength concepts
- AWS shared responsibility model
- AWS global infrastructure and service scope: global, regional and zonal
- AWS Well-Architected Framework pillars: operational excellence, security, reliability, performance efficiency, cost optimization and sustainability
- High availability, fault tolerance, elasticity, scalability and disaster recovery
- CAP-style trade-offs, consistency models and distributed-system failure modes
- Consumption pricing, fixed versus variable cost, economies of scale and managed-service trade-offs
- AWS account structure, Organizations, organizational units, consolidated billing and account vending
- Quotas, service limits, tagging strategy and resource naming

### B. Identity, security and governance

- IAM users, groups, roles, policies, policy evaluation, explicit deny and least privilege
- Identity-based, resource-based, permissions-boundary, session and service-control policies
- IAM Access Analyzer, credential reports, MFA, root-user protection and temporary credentials
- AWS IAM Identity Center, federation, SAML/OIDC and workforce versus workload identity
- AWS Organizations, SCPs, Control Tower concepts, AWS Config and resource compliance
- KMS keys, key policies, grants, envelope encryption, rotation and multi-Region keys
- Secrets Manager, Systems Manager Parameter Store and safe secret rotation
- CloudTrail, CloudWatch, GuardDuty, Security Hub, Inspector, Macie and Detective
- WAF, Shield, Firewall Manager, Network Firewall and DDoS-aware architecture
- Encryption in transit and at rest; TLS certificates with ACM
- VPC security groups, network ACLs, private subnets, VPC endpoints and egress control
- Data classification, retention, logging, auditability and incident-response runbooks

### C. Networking and content delivery

- VPCs, CIDR planning, subnets, route tables, internet gateways and NAT gateways
- Public, private and isolated subnet design across multiple Availability Zones
- Security groups versus network ACLs; stateful versus stateless filtering
- Elastic IPs, ENIs, DNS resolution and DHCP options
- VPC peering, Transit Gateway, PrivateLink, Site-to-Site VPN and Direct Connect
- Client VPN, hybrid DNS, Route 53 Resolver endpoints and split-horizon DNS
- Route 53 hosted zones, records, routing policies, health checks and failover
- CloudFront distributions, origins, caching, invalidation, signed URLs/cookies and Origin Access Control
- Elastic Load Balancing: Application, Network and Gateway Load Balancers
- Global Accelerator and choosing between DNS, CDN, acceleration and load balancing
- IPv4/IPv6, dual-stack design, MTU, flow logs and network troubleshooting

### D. Compute and containers

- EC2 instance families, sizing, user data, AMIs, EBS, instance store and placement groups
- On-Demand, Reserved Instances, Savings Plans, Spot Instances and capacity planning
- Auto Scaling groups, launch templates, scaling policies, health checks and warm pools
- Elastic Beanstalk and managed application deployment concepts
- Lambda runtimes, handlers, layers, environment variables, versions, aliases, concurrency, timeouts and event sources
- Lambda permissions, destinations, retries, dead-letter queues, idempotency and cold starts
- ECS on Fargate and EC2, task definitions, services, deployments, service discovery and autoscaling
- ECR image lifecycle, image scanning and immutable tags
- EKS concepts: control plane, nodes, pods, services, ingress, IAM roles for service accounts and autoscaling
- Batch, Lightsail and serverless versus instance-based trade-offs

### E. Storage

- S3 buckets, objects, keys, prefixes, versioning, lifecycle rules and storage classes
- S3 durability/availability concepts, replication, Object Lock, retention and legal holds
- S3 encryption, bucket policies, Block Public Access, access points and presigned URLs
- S3 event notifications, EventBridge integration, multipart upload and transfer acceleration
- EBS volume types, snapshots, encryption, resizing and performance characteristics
- EFS, FSx variants and choosing shared file storage
- Storage Gateway, DataSync, Transfer Family and Snow Family
- Backup, archive, restore testing, RPO/RTO and cross-Region protection

### F. Databases and caching

- RDS engines, parameter/option groups, Multi-AZ, read replicas, backups and maintenance
- Aurora architecture, reader endpoints, global databases, Serverless v2 and failover
- DynamoDB partition keys, sort keys, indexes, capacity modes, autoscaling and consistency
- DynamoDB conditional writes, transactions, streams, TTL, global tables and single-table design
- ElastiCache for Redis/Valkey and Memcached; cache invalidation and session storage
- Redshift, OpenSearch and the difference between OLTP, OLAP, search and key-value workloads
- Database Migration Service, Schema Conversion Tool and migration patterns
- Database security, encryption, subnet groups, parameter tuning and connection pooling

### G. Integration, messaging and event-driven systems

- SQS standard and FIFO queues, visibility timeout, long polling, deduplication and DLQs
- SNS topics, subscriptions, filtering and fan-out
- EventBridge buses, rules, schedules, schemas and cross-account events
- Step Functions state machines, retries, catches, parallel/map states and human approval
- API Gateway HTTP, REST and WebSocket APIs, stages, throttling, authorizers, usage plans and caching
- AppSync and GraphQL concepts
- Amazon MQ and choosing managed brokers versus cloud-native messaging
- Event-driven design, at-least-once delivery, ordering, idempotency and poison-message handling

### H. Monitoring, operations and deployment

- CloudWatch metrics, logs, alarms, dashboards, Logs Insights and embedded metric format
- CloudTrail management/data events, organization trails and audit log protection
- AWS Config rules, conformance packs and remediation
- Systems Manager: Session Manager, Run Command, Automation, Patch Manager, Inventory and Parameter Store
- X-Ray tracing, correlation IDs and distributed troubleshooting
- AWS Health, Personal Health Dashboard, Trusted Advisor and service quotas
- Infrastructure as code with CloudFormation, CDK and Terraform concepts
- CodeCommit/Git alternatives, CodeBuild, CodeDeploy, CodePipeline and CodeArtifact concepts
- Blue/green, canary, rolling and immutable deployments
- Change management, runbooks, operational readiness reviews and post-incident reviews

### I. Data, analytics and AI

- Lake formation concepts, data lakes, cataloging, permissions and governance
- Glue crawlers, Data Catalog, ETL jobs and workflows
- Athena, EMR, Redshift, Kinesis Data Streams, Firehose and Managed Service for Apache Flink
- QuickSight, OpenSearch dashboards and basic BI architecture
- Batch versus streaming ingestion, partitioning, compression, schema evolution and data quality
- Bedrock, SageMaker and responsible use of generative AI/ML services at a conceptual level
- Data privacy, masking, lineage, retention and cross-account data sharing

### J. Migration, resilience, cost and sustainability

- AWS migration strategies: rehost, replatform, refactor, repurchase, retain and retire
- Migration Hub, Application Migration Service, DMS, DataSync and discovery/assessment
- Backup and restore, pilot light, warm standby, multi-site active/active and recovery testing
- RTO/RPO selection and dependency mapping
- Cost Explorer, AWS Budgets, Cost and Usage Reports, Billing alarms and tagging
- Compute rightsizing, Savings Plans, Spot, storage lifecycle, serverless economics and data-transfer costs
- Cost allocation tags, chargeback/showback and FinOps controls
- Carbon-aware architecture, efficient data processing, autoscaling and resource cleanup

## 3. Certification-specific additions

### Cloud Practitioner

Focus on AWS vocabulary, the shared responsibility model, core services and use cases, pricing/billing, basic security, support plans, cloud benefits and the Well-Architected pillars. Hands-on depth is useful but not required.

### Solutions Architect – Associate

Practice selecting services and explaining trade-offs for secure, highly available, fault-tolerant, decoupled, performant and cost-aware architectures. Be able to interpret requirements, diagrams, metrics and failure scenarios.

### Developer – Associate

Add SDK/API usage, application configuration, DynamoDB access patterns, Lambda and API Gateway, event-driven applications, CI/CD, testing, deployment strategies, observability and troubleshooting.

### SysOps Administrator – Associate

Add provisioning, automation, monitoring, patching, backups, networking, scaling, incident response, deployment operations, troubleshooting and cost controls.

### DevOps Engineer – Professional

Add multi-account governance, advanced CI/CD, deployment safety, observability, incident response, resiliency, automation at scale and organizational operating models.

### Solutions Architect – Professional

Add complex multi-Region and hybrid architectures, migration portfolios, organizational governance, cross-account design, workload decomposition, business continuity and architectural trade-offs at scale.

### Security – Specialty

Go deeper on IAM, KMS, logging, detection, incident response, data protection, network security, application security, governance and continuous compliance.

### Data Engineer – Associate / Data Analytics – Specialty

Go deeper on ingestion, transformation, data lakes, catalogs, streaming, warehouses, governance, query performance, data security and analytical workload design.

### Machine Learning Engineer – Associate / Machine Learning – Specialty

Go deeper on data preparation, feature engineering, model selection, training, deployment, MLOps, monitoring, bias, drift, security and responsible AI.

### Advanced Networking – Specialty

Go deeper on hybrid connectivity, routing, Transit Gateway, Direct Connect, VPN, DNS, IPv6, network security, automation and troubleshooting at scale.

## 4. Twelve-week study plan

Adjust the pace to your target exam. A realistic minimum is 8–12 hours per week plus regular hands-on time.

| Weeks | Study focus | Required output |
|---|---|---|
| 1 | Cloud concepts, AWS global infrastructure, IAM, billing | Account secured; notes and flashcards |
| 2 | VPC, routing, security groups, NACLs, DNS | Multi-AZ network diagram and lab |
| 3 | EC2, EBS, AMIs, Auto Scaling, load balancing | Highly available web tier |
| 4 | S3, EFS, backup, lifecycle, encryption | Secure data lake bucket |
| 5 | RDS, Aurora, DynamoDB, caching | HA relational and NoSQL comparison |
| 6 | Lambda, API Gateway, SQS, SNS, EventBridge | Event-driven API |
| 7 | ECS/Fargate, ECR, deployment patterns | Containerized service |
| 8 | CloudWatch, CloudTrail, Config, Systems Manager | Monitored and auditable workload |
| 9 | IaC, CI/CD, testing and automation | Repeatable deployment pipeline |
| 10 | Resilience, migration, DR, cost and sustainability | Architecture review and DR test |
| 11 | Target-certification deep dive | Two timed practice exams; error log |
| 12 | Revision and exam simulation | Final weak-area labs and exam readiness check |

For every topic, use this loop: learn the concept, draw the architecture, implement a small lab, break it deliberately, observe the failure, clean up the resources, and explain the design in your own words.

## 5. Python and boto3 practical curriculum

### Setup and safety first

Use a dedicated AWS account or sandbox, never the root user for daily work, and enable MFA. Create a least-privilege IAM role or IAM Identity Center permission set for labs. Set a billing budget and alerts, choose one lab Region, tag every resource, and delete resources after each lab.

Recommended local setup:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install boto3 botocore pytest moto python-dotenv
aws configure sso
```

Prefer temporary credentials from IAM Identity Center, roles or federation. Do not store access keys, passwords or secrets in source code. Configure a default Region and use environment variables or a local ignored `.env` file only for non-secret configuration.

Suggested repository layout:

```text
aws-python-labs/
├── README.md
├── pyproject.toml
├── src/aws_labs/
│   ├── config.py
│   ├── clients.py
│   ├── tagging.py
│   ├── retry.py
│   └── labs/
├── tests/
├── infrastructure/
└── scripts/
```

### Boto3 skills to master

- Sessions, clients and resources; explicit Region selection
- Credential provider chain and role assumption with STS
- Request parameters, response parsing and typed helper functions
- Waiters, paginators, retries, exponential backoff and throttling handling
- Idempotency tokens, safe retries and eventual consistency
- Dry-run modes, confirmation prompts and resource ownership tags
- Structured logging, CloudWatch-compatible JSON logs and correlation IDs
- Error handling with `botocore.exceptions.ClientError`
- Unit testing with `pytest` and service mocks with `moto`
- Integration tests in a sandbox account with strict cleanup
- Async/concurrent calls only when service limits and ordering requirements are understood
- Packaging reusable clients as a small Python module or CLI

### Twelve practical boto3 projects

1. **Account inventory CLI** — list Regions, enabled services, EC2 instances, S3 buckets, Lambda functions and tags. Add pagination, retries and JSON/CSV output.
2. **Secure S3 uploader** — upload with encryption, metadata and checksums; generate a short-lived presigned URL; verify object existence; add lifecycle and cleanup commands.
3. **VPC inspection tool** — describe VPCs, subnets, route tables, gateways and security groups; produce a readable network report without changing resources.
4. **EC2 lifecycle manager** — start/stop only instances with an approved tag, support dry-run, wait for state transitions, log actions and refuse untagged resources.
5. **Automated backup tool** — create and tag EBS/RDS snapshots, enforce retention, report failures and never delete snapshots outside its ownership tag.
6. **DynamoDB application** — build a table with a deliberate partition key, conditional writes, pagination, TTL and a query path; measure consumed capacity.
7. **Serverless API** — deploy a Lambda function behind API Gateway using IaC, write logs and metrics, and test retries/idempotency.
8. **Queue worker** — publish to SNS/SQS, process batches, handle visibility timeouts, send poison messages to a DLQ and implement graceful shutdown.
9. **Event-driven workflow** — emit EventBridge events and orchestrate validation, persistence and notification with Step Functions.
10. **Observability dashboard** — create CloudWatch log groups, metric filters, alarms and a dashboard; correlate request IDs across services.
11. **Compliance scanner** — inspect public S3 exposure, unencrypted storage, open security-group rules and missing tags; report findings without auto-remediation first.
12. **Cost and cleanup assistant** — find unattached EBS volumes, old snapshots, idle load balancers and untagged resources; require an explicit approval step before deletion.

### Required implementation pattern

Each project should include:

- A short problem statement and architecture diagram
- A `README` with prerequisites, permissions and estimated cost
- A `plan` or dry-run mode before mutation
- Least-privilege IAM policy documentation
- Input validation and clear error messages
- Retries for transient failures and pagination for list APIs
- Unit tests for success, validation failure and AWS error paths
- Structured logs and a cleanup command
- Resource tags such as `Project`, `Owner`, `Environment`, `CreatedBy` and `ExpiresAt`
- A post-lab review covering security, reliability, performance, cost and sustainability

## 6. Capstone project

Build a **serverless order-processing platform**:

```text
Client → API Gateway → Lambda → DynamoDB
                         │
                         └→ EventBridge → Step Functions → SQS worker → S3
                                                        │
                                                        └→ CloudWatch / SNS alert
```

Implement it with Python and boto3, preferably provisioning infrastructure with AWS CDK or CloudFormation:

- Authentication and authorization with IAM or Amazon Cognito
- Input validation, idempotency and conditional writes
- DynamoDB partition-key design and a secondary index
- EventBridge events and a Step Functions retry/catch policy
- SQS visibility timeout, DLQ and worker metrics
- S3 encryption, lifecycle and restricted bucket policy
- CloudWatch logs, alarms, dashboards and trace/request IDs
- CloudTrail auditing and least-privilege execution roles
- Unit tests with mocks and a small sandbox integration test suite
- Load, failure-injection, backup/restore and cost tests
- A written Well-Architected review and a disaster-recovery runbook

## 7. Exam preparation and evidence of readiness

- Read the current official exam guide, task statements and sample questions.
- Complete at least two timed practice exams and keep an error log by domain.
- For every wrong answer, write why the selected service was wrong and what requirement would make it correct.
- Practice eliminating distractors using security, reliability, operational, performance and cost constraints.
- Review service limits, pricing models, integration behavior and failure modes—not just service definitions.
- Be able to explain each capstone design without notes and modify it when requirements change.
- Schedule the exam only after practice scores are consistently above your chosen safety margin and weak domains have been lab-tested.

## 8. Quick reference: questions to ask for every AWS design

1. Who or what is allowed to access each resource?
2. What happens when an Availability Zone, dependency or message consumer fails?
3. Which data is encrypted, where are the keys, and how is access audited?
4. What is the RTO/RPO and how is recovery tested?
5. How does the system scale and what are its service limits?
6. How are retries, duplicates, ordering and idempotency handled?
7. How will operators detect, diagnose and remediate a failure?
8. What is the expected monthly cost and which resources must be cleaned up?
9. Which parts should be managed services, serverless, containers or instances—and why?
10. How will the architecture be deployed, changed and rolled back safely?
