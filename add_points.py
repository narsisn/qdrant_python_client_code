
''' add_point '''

from qdrant_client import QdrantClient
import numpy as np
import points 


if __name__ == '__main__':

    host = "localhost" 
    port = 6333
    collection_name = "snapmode"
    distance = "Cosine"   # Enum: "Cosine" "Euclid" "Dot"
    vector_size = 2048
    client = points.QpointClass(host,port,collection_name,distance,vector_size)
    conn = client.connect_collection()

    vectors = np.random.rand(1,2048)
    ids = ['acebc9930156548c8645d58e0c127cce']
    batch_size = 1
    parallel = 1 
    payloads = [{ "product_id" : "b75b011b772f58dd9636cba08b80f4e1" ,
    "product_category" : "Clothing",
    "main_category" : "Shirts",
    "gender" : "Men"
    }]
    client.add_point(conn,vectors,payloads,ids,batch_size,parallel)
    print(f'Adding Point Successfully Done.')
