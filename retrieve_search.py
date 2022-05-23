
''' add_point '''

from qdrant_client import QdrantClient
import numpy as np
import points 


if __name__ == '__main__':

    host = "0.0.0.0" 
    port = 6333
    collection_name = "snapmode"
    top = 50


    client = points.QpointClass(host,port,collection_name)
    conn = client.connect_collection()

    ids = ['f43d9f67d02c5f4093956725e6f5eb7d']

    results = client.retrieve_vector(conn,ids)

    # print(f'The retrieved point for id: {ids} is {results}')

    # for key in results.keys():
    #     if key != 'vector':
    #         print(f'The Product_id is: {results[key]["product_id"]}')
    
    query_vectors = results['vector']
    # print(query_vectors)
    results = client.serach_point(conn,query_vectors,top)

    print(f'The results is {results}')