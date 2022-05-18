
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

    ids = ['acebc9930156548c8645d58e0c127cce']

    results = client.retrieve_vector(conn,ids)

    print(f'The retrieved point for id: {ids} is {results}')

    for key in results.keys():
        if key != 'vector':
            print(f'The Product_id is: {results[key]["product_id"]}')