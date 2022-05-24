from qdrant_client import QdrantClient
import points 
import pysolr 

from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests import Session
import requests

import numpy as np
import uuid
import json
import os 



TEMP_IMG_DIR = 'temp_img/'


def solr_connection():

    solr_url = "http://192.168.104.100:8983/solr/Product_Core/"
    solr_conn = pysolr.Solr(solr_url, timeout=10, always_commit=True)
    
    return solr_conn

def qdrant_connection():
    host = "192.168.4.196" 
    port = 6333
    collection_name = "snapmode"
    client = points.QpointClass(host,port,collection_name)
    conn = client.connect_collection()
    return client, conn 

def image_download(image_url,session):
    img_name = image_url.split("/")[-1]
    data_img = session.get(image_url,timeout=50,headers={'x-test2': 'true'}) 
    with open(TEMP_IMG_DIR+img_name, 'wb') as fobj:
        fobj.write(data_img.content) 


    return TEMP_IMG_DIR+img_name

def create_session():
    session = requests.Session()
    retry_strategy = Retry(
                        total=15,
                        backoff_factor=0.1,
                        )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    adapter.max_retries.respect_retry_after_header = False
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session 

def get_spec(res):
    payloads = [{
        "product_id": res['product_id'][0],
        "product_category" : res['product_category'][0],
        "main_category" : res['main_category'][0],
        "gender" : res['gender'][0]
    }]
    image_url = res['url']
    ids =  [uuid.uuid5(uuid.NAMESPACE_URL, res['url'] ).hex ]

    return ids,payloads,image_url

def remove_image(image_path):
    os.remove(image_path)
    return


if __name__ == '__main__':

    # constant 
    start = 0
    rows = 1000 
    batch_size = 1 
    parallel = 1

    # model address
    model_name = 'ViT'
    toechserve_host = '192.168.4.196'
    toechserve_port = '8080'
    model = "http://"+ toechserve_host + ":" + toechserve_port + "/predictions/" + model_name

    # request session
    session = create_session()

    # qdrant connection 
    client, qdrant_conn = qdrant_connection()

    # solr connection 
    solr_conn = solr_connection()
    
    counter = 0

    while(1):
        print(f'**** The start is :{start} ****')
        result = solr_conn.search("business_type:Instagram", start=start, rows=rows)
        for res in result:
            try:
                # get product specs
                print("the counter is :", counter)
                ids,payloads,image_url = get_spec(res)
                print(image_url)
                # download the  image
                image_path = image_download(image_url,session)
                # embedd the image 
                res = requests.post(model, files={'data': open(image_path, 'rb')}).text
                remove_image(image_path)
                res = json.loads(res)
                vectors = np.array(res).reshape(1,1024)
                # index at qdrant
                print(ids)      
                client.add_point(qdrant_conn,vectors,payloads,ids,batch_size,parallel)
            except:
                print(f'Error on image : {image_url}')
                continue
            counter+=1
        
        start = start + rows
        if len(result) == 0 :
            break

 
 
    print(f'Adding Points Successfully Done.')

