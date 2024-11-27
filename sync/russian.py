# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

import logging

from os import environ
from time import sleep
from urllib.parse import urlparse

from boto3 import Session
from opensearchpy import Urllib3AWSV4SignerAuth, OpenSearch, __versionstr__

# verbose logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

print(f"Using opensearch-py {__versionstr__}")

# cluster endpoint, for example: my-test-domain.us-east-1.es.amazonaws.com
url = urlparse(environ['ENDPOINT'])
region = environ.get('AWS_REGION', 'us-east-1')
service = environ.get('SERVICE', 'es')

credentials = Session().get_credentials()

auth = Urllib3AWSV4SignerAuth(credentials, region, service)

client = OpenSearch(
    hosts=[{
        'host': url.netloc,
        'port': url.port or 443
    }],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    timeout=30
)

# TODO: remove when OpenSearch Serverless adds support for /
if service == 'es':
    info = client.info()
    print(f"{info['version']['distribution']}: {info['version']['number']}")


# create an index
index = 'кино'
client.indices.create(index=index)

try:
    # index data
    id = 'соларис@2011'
    document = {"название": "Солярис",
                "автор": "Андрей Тарковский", "год": "2011"}
    client.index(index=index, body=document, id=id)

    # wait for the document to index
    sleep(1)

    doc = client.get(index=index, id=id)
    print(doc)

    # search for the document
    results = client.search(
        body={'query': {'match': {'автор': 'Андрей Тарковский'}}})
    for hit in results['hits']['hits']:
        print(hit['_source'])

    # delete the document
    client.delete(index=index, id=id)
finally:
    # delete the index
    client.indices.delete(index=index)
