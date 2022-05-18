
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

    query_vectors = np.random.rand(2048)

    results = client.serach_point(conn,query_vectors)

    print(f'The results is {results}')
