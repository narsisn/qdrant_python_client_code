from qdrant_client import QdrantClient

class CreateCollection:
    def __init__(self,host="",port="",collection_name="",distance="",vector_size=""):
        self.host=host
        self.port=port
        self.collection_name=collection_name
        self.distance = distance
        self.vector_size = vector_size 
    
    def create_collection(self):
        client = QdrantClient(host=self.host, port=self.port)
        client.recreate_collection(
            collection_name=self.collection_name, 
            distance=self.distance,
            vector_size=self.vector_size
                )
        my_collection_info = client.http.collections_api.get_collection(self.collection_name)

        return my_collection_info


if __name__ == "__main__":

    host = "localhost" 
    port = 6333
    collection_name = "snapmode"
    distance = "Cosine"   # Enum: "Cosine" "Euclid" "Dot"
    vector_size = 2048
    CC = CreateCollection(host,port,collection_name,distance,vector_size)
    my_collection_info = CC.create_collection()
    print(f'creating the collection {collection_name} successfully done.')
    print(f'The Info is {my_collection_info}')


