
''' add_point '''

from qdrant_client import QdrantClient
import numpy as np
import points 


if __name__ == '__main__':

    host = "192.168.4.196" 
    port = 6333
    collection_name = "toobamode"
 
    client = points.QpointClass(host,port,collection_name)
    conn = client.connect_collection()

    vectors = np.random.rand(1,1024)
    print(vectors)
    ids = ['5ac33bab0ba654f9806764f0ba8e5bb1']
    batch_size = 1
    parallel = 1 
    payloads = [{ "product_id" : "b75b011b772f58dd9636cba08b80f4e1" ,
    "product_category" : "Clothing",
    "main_category" : "Shirts",
    "gender" : "Men"
    }]
    client.add_point(conn,vectors,payloads,ids,batch_size,parallel)
    print(f'Adding Point Successfully Done.')
