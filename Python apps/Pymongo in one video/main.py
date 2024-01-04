from pymongo import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import numpy as np
if __name__ == "__main__":
    client = MongoClient("mongodb+srv://GoldarmGang:naman@cluster1.h4zwnxm.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client['NewDB']
    collection = db['Collection0']
    df = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334).astype(str))
    
    dict1 = df.to_dict('dict')
    dict1 = {str(k):v for k,v in dict1.items()}
    print(dict1['0'])
    collection.insert_one(dict1)
    