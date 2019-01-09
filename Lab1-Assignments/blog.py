from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds149491.mlab.com:49491/c4e25"

# 1. Connect to mlab server
client = MongoClient(uri)
# 2. get a database
db = client.get_database()
# 3. get a collection
post_collection = db["posts"]

#4. create a document


new_post = {"title": "Hom nay troi nhiều mây", #field title
        "content": "Tôi ra đường, à mà thôi, Tôi vẫn ở nhà code",
        }
#lazy loading
post_list = post_collection.find() #cursor 
# first_post = post_list[0]
# print(first_post)
#5. insert document
# post_collection.insert_one(new_post)
# for post in posts.find({"$oid": "5c31c9adb2b5dcef717e57b6"}):
#     pprint.pprint(post)

#6. Close connection
for p in post_list:
    print(p)
client.close()