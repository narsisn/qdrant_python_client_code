
''' add_point '''

from qdrant_client import QdrantClient
import numpy as np
import points 


if __name__ == '__main__':

    host = "localhost" 
    port = 6333
    collection_name = "snapmode"


    client = points.QpointClass(host,port,collection_name)
    conn = client.connect_collection()

    ids = ['b75b011b772f58dd9636cba08b80f4e1']

    results = client.retrieve_vector(conn,ids)

    print(f'The retrieved point for id: {ids} is {results}')

    for key in results.keys():
        if key != 'vector':
            print(f'The Product_id is: {results[key]["product_id"]}')