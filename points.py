''' Class for point operations ''' 

from qdrant_client import QdrantClient

class QpointClass:

    def __init__(self,host="",port="",collection_name="",distance="",vector_size=""):
        self.host=host
        self.port=port
        self.collection_name=collection_name
        self.distance = distance
        self.vector_size = vector_size   

    def connect_collection(self):
        client = QdrantClient(host=self.host, port=self.port)
        return client 
    
    def add_point(self,conn,vectors,payloads,ids,batch_size,parallel):
        conn.upload_collection(self.collection_name, vectors , payloads ,ids, batch_size, parallel)

        return 
    
    def retrieve_vector(self):
        return

    def serach_point(self):
        return
    

