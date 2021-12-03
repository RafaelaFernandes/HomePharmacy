import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbmsl"]
mycol = mydb["MedicalRecord"]

for x in mycol.find():
  print(x)