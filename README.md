# mysqlbackup-lambda

_tldr;_ AWS Lambda to backup mysql database to S3

## Repo Pull:

Although, incase working with Lambda, you would need to publish this to Private ECR, in case needed, latest can be pulled from: [public.ecr.aws/letsdocoding/mysqlbackup-lambda:latest](public.ecr.aws/letsdocoding/mysqlbackup-lambda:latest).

## Setup

1. Publish to your private ECR Repo
2. Define the following ENV Variables to configure
   1. `S3_BUCKET` : Defines the target S3 Bucket
   2. `DB_HOST` : Defines the Database Host
   3. `DB_NAME` : Defines the database name
   4. `DB_USER` : Defines the database user
   5. `DB_PASS` : Defines the database password
3. Configure the triggers and good to go
