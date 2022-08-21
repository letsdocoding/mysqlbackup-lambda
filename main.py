import subprocess
import os
import time
import json

S3_BUCKET = os.environ['S3_BUCKET']

timestamp = time.strftime('%Y-%m-%d-%I:%M')


def backup(event, context):
    print("Function started")

    dbHost = os.environ['DB_HOST']
    dbName = os.environ['DB_NAME']
    dbUser = os.environ['DB_USER']
    dbPass = os.environ['DB_PASS']
    print(dbHost)
    print("%s %s ".format(dbHost, dbName))

    command = "mysqldump --host %s --user %s -p%s %s | gzip -c | aws s3 cp - s3://%s/%s.gz" % (
        dbHost, dbUser, dbPass, dbName, S3_BUCKET, dbName + "_" + timestamp)
    #print (command)
    subprocess.Popen(command, shell=True).wait()
    print("MySQL backup finished")
    return "backup finished"