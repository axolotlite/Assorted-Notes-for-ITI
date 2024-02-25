#### Case Study 1: 
AWS Storage Solution for a Travel Data Analytics Company
##### **Overview:**
A data analytics company specializing in the travel industry processes billions of customer events per day.
##### **Challenges:**
1. **High Data Production Rate**
2. **Scalability** 
3. **Cost Efficiency**
##### **Solution:** 
To overcome these 3 challenges, Kinesis Firehose will have to output to Amazon S3, with an added policy to move older data into a glacier archive.
##### **Benefits:**
1. **Kinesis Firehose Integration:** Amazon S3 allows for Firehose output to be directly stored in S3.
2. **Scalability:** Amazon S3 scales seamlessly.
3. **Cost Efficiency:** Low cost per GB, and life cycle policies allows for data transitioning to lower-cost storage such as glacier which further reduces costs.
##### **Conclusion:**
By leveraging Amazon S3 as their storage solution, the travel site data analytics company can efficiently manage, store, and analyze billions of customer events per day.
The scalability, durability, cost efficiency, and most importantly, the integration between Firehose and S3 makes it an ideal choice for storing the result of their data analytics pipeline.

---
#### Case Study 2: 
AWS Storage Solution for a Collaboration Software Company
##### **Overview:**
collaboration software company provides email processing services for enterprise customers, serving over 250 enterprises and more than half a million users.
##### **Challenges:**
1. **Scalability** 
2. **Performance**
3. **Cost Efficiency**
##### **Solution:** 
To overcome these 3 challenges, We can use two different Storage Solutions, EBS for data processing during transferal to the EC2 instances and S3 for storing the post processed Data. 
##### **Benefits:**
###### **Amazon EBS**:
Solves the Performance issue during data processing, since EBS is native to an EC2 Instance and has enough IO performance to allow quick processing before transferring data to S3.
###### **Amazon S3**:
Allows us to solve the Scalability and Cost Efficiency challenges by storing processed data as objects with its low cost per GB and even better pricing for Glacier Archives.
##### **Conclusion:**
By using both EBS and S3, we can allow for fast data processing, post-processing storage and access.

---
#### Case Study 3: 
AWS Storage Solution for a Data Protection Company
##### **Overview:**
Data protection company must be able to ingest and store large amounts of customer data and help their customers meet compliance requirements. They use amazon EC2 for scaleble compute and amazon dynamoDB for duplicate data and metadata lookups.
##### **Challenges:**
1. **Scalability** 
2. **Performance**
3. **Cost Efficiency**
##### **Solution:** 
To overcome these 3 challenges, We can use two different Storage Solutions, EBS for data processing and DynamoDB storage and S3 Glacier for storing the data for compliance.
##### **Benefits:**
###### **Amazon EBS**:
Increases performance when querying or added records to DynamoDB, since EBS is fast.
###### **Amazon S3 Glacier**:
Allows us to solve the Scalability and Cost Efficiency challenges by storing the data as objects cheaply within the Glacier archive, although retrieval will be slow, this is just compliance data, so it doesn't matter.
##### **Conclusion**:
By using both EBS and S3, we can allow for fast data processing and storage for compliance purposes.