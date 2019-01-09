from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to mlab server
client = MongoClient(uri)
# 2. get a database
db = client.get_database()
# 3. get a collection
customer_collection = db["customers"]
print("Total:",db.customers.estimated_document_count())

events = db.customers.count_documents( {"ref": "events"} )
print("Events:", events)
ads = db.customers.count_documents(({"ref": "ads"}))
print("Ads:", ads)

wom = db.customers.count_documents(({"ref": "wom"}))
print("WOM:", wom)

client.close()

import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

ref_counts = [events, ads, wom]
ref_names = ["Events", "Ads", "WOM"]
pyplot.title("Events vs Ads vs WOM usage")
pyplot.pie(ref_counts, labels = ref_names, autopct="%.1f%%", shadow = True)
pyplot.axis("equal")

pyplot.show()