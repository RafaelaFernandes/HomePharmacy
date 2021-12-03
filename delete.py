import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbmsl"]
mycol = mydb["MedicalRecord"]

myquery = { "category": 'xarope' }

new = mycol.delete_many(myquery)

print(new.deleted_count, " documents deleted.")