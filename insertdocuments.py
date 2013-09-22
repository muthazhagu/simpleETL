import pymongo
from pymongo import MongoClient
from prepdocuments import prepdocuments

client = MongoClient()

def insertDocuments(DATABASE = 'test',
                    TABLE = 'fnlndob',
                    numberOfDocs = 1,
                    append = False):
    """
    Method inserts n number of documents into a MongoDB collection.
    Takes in the DATABASE name, TABLE (COLLLECTION) name,
    number of documents to be inserted as input.
    Setting append to TRUE appends records to an existing collection.

    Default value for append = False.

    Method returns None.
    """

    db = client[DATABASE]
    collection = db[TABLE]
    table = db.collection
    documents = prepdocuments(numberOfDocs)

    if append:
        table.insert(documents)
    else:
        table.drop()
        table.insert(documents)

    print "Done!"
    print "Number of documents inserted:", table.count()

insertDocuments(numberOfDocs = 15)
