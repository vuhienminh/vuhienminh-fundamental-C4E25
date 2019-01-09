from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)

db = client.get_database()
post_collection = db["posts"]
new_post = {"title": "Chúc mừng năm mới 2019", 
        "author": "H Minh",
        "content": "Chúc các bạn C4E sẽ học được nhiều điều từ Techkids :)",
        }

post_collection.insert_one(new_post)
client.close()