import pandas as pd
import pymongo
import os
import sys
import json
import boto3
import base64
import botocore

#########################New Update#################
username = os.environ.get("docdbUser")
password = os.environ.get("docdbPass")
clusterendpoint = os.environ.get("docdbEndpoint")

def lambda_handler(event, context):
    ##########################################New Doc DB Code###############
    client = pymongo.MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile='rds-combined-ca-bundle.pem',retryWrites='false')
    print(client.list_database_names())
    print(db.list_collection_names())
    ###########################################old code##########################
    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1.1.1')