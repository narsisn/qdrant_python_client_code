''' Class for point operations ''' 

from qdrant_client import QdrantClient

class QpointClass:

    def __init__(self,host="",port="",collection_name=""):
        self.host=host
        self.port=port
        self.collection_name=collection_name
    

    def connect_collection(self):
        client = QdrantClient(host=self.host, port=self.port)
        return client 
    
    def add_point(self,conn,vectors,payloads,ids,batch_size,parallel):
        conn.upload_collection(self.collection_name, vectors , payloads ,ids, batch_size, parallel)

        return 
    
    def retrieve_vector(self,conn,ids):
        result = conn.get_payload(self.collection_name,ids)

        return result

    def serach_point(self,conn,qvec):
        result = conn.search(self.collection_name,qvec)
        return result
    

