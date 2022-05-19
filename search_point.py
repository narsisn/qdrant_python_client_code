
''' add_point '''

from qdrant_client import QdrantClient
import numpy as np
import points 


if __name__ == '__main__':

    host = "localhost" 
    port = 6333
    collection_name = "snapmode"
    top = 50


    client = points.QpointClass(host,port,collection_name)
    conn = client.connect_collection()

    query_vectors = np.random.rand(1024)

    results = client.serach_point(conn,query_vectors,top)

    print(f'The results is {results}')
