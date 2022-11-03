from pymongo import MongoClient

username = 'kwanhoon'
password = 'shk9293112'

URI = f'mongodb+srv://{username}:{password}@cluster0.xsktws7.mongodb.net/A1R?retryWrites=true&w=majority'

client = MongoClient(URI)  # 파이썬과 mongo를 연결
DATABASE = 'IT_product'

database = client[DATABASE]

COLLECTION = 'Monitor'
collection = database[COLLECTION]

data = collection.find()
for d in data:
    print(d)