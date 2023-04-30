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

    ##Create New DB
    db = client.LambdaNew_database

    ##New Collection for DB

    col = db.LambdaTable_collection

    ##Insert a single document
    col.insert_one({'hello':'DocumentDB'})

    ##Find the document that was previously written
    x = col.find_one({'hello':'DocumentDB'})

    ##Print the result to the screen
    print(x)
    print(client.list_database_names())
    print(db.list_collection_names())

    ##Drop Collection
    #db.drop_collection('mynewnew_democollection')
    print(client.list_database_names())
    print(db.list_collection_names())
    ###########################################old code##########################