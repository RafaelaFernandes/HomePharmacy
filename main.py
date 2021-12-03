## Projeto Home Pharmacy ##
## Aluna: Rafaela Fernandes - 1468 ##


import pymongo
#Criação da base de dados

if __name__== "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['dbmsl']
    db.collection = db['MedicalRecord']
    # #inserindo um medicamento por vez
    dictionary = {'name': 'Omeprazol', 'category': 'comprimido', 'id': 1, 'quantity': 3}
    db.collection.insert_one(dictionary)
    #inserindo vários medicamentos
    db.collection.insert_many([
        {'name': 'Omeprazol', 'category': 'comprimido', 'id': 1, 'quantity': 3},
        {'name': 'Prozac', 'category': 'capsula', 'id': 2, 'quantity': 1},
        {'name': 'Vitamina D', 'category': 'capsula', 'id': 3, 'quantity': 2},
        {'name': 'Dipirona', 'category': 'comprimido', 'id': 4, 'quantity': 5},
        {'name': 'Maracujina', 'category': 'xarope', 'id': 5, 'quantity': 1},
        {'name': 'Nimesulida', 'category': 'dispersivel', 'id': 6, 'quantity': 4},
        {'name': 'Paracetamol', 'category': 'comprimido', 'id': 7, 'quantity': 5},
        {'name': 'Amoxicilina', 'category': 'capsula', 'id': 8, 'quantity': 2},
        {'name': 'Engov', 'category': 'gotas', 'id': 9, 'quantity': 10},
        {'name': 'Melagrião', 'category': 'xarope', 'id': 10, 'quantity': 1}
    ])