import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbmsl"]
mycol = mydb["MedicalRecord"]

myquery = { "name": 'Dipirona' } 
newvalues = { "$set": { "quantity": 5 } }

new = mycol.update_many(myquery, newvalues)

print(new.modified_count, "documents updated.")