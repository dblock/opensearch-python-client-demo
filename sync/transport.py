# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

from opensearchpy import OpenSearch
from time import sleep
import logging

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('admin', 'admin'),
    use_ssl=True,
    verify_certs=False
)

info = client.transport.perform_request("GET", "/")
print(
    f"Welcome to {info['version']['distribution']} {info['version']['number']}!")

# create an index
index = 'movies'
logging.info(client.transport.perform_request("PUT", f"/{index}"))

try:
    # index data
    document = {'director': 'Bennett Miller',
                'title': 'Moneyball', 'year': 2011}
    logging.info(client.transport.perform_request(
        "POST", f"/{index}/_doc/1", body=document))

    # wait for the document to index
    sleep(1)

    # search for the document
    results = client.transport.perform_request(
        "POST", f"/{index}/_search", body={'query': {'match': {'director': 'miller'}}})
    for hit in results['hits']['hits']:
        print(hit['_source'])

    # delete the document
    logging.info(client.transport.perform_request(
        "DELETE", f"/{index}/_doc/1"))
finally:
    # delete the index
    logging.info(client.transport.perform_request("DELETE", f"/{index}"))
