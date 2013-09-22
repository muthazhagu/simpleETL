import sqlite3
import pymongo
from pymongo import MongoClient
from datetime import date
from insertdocuments import insertDocuments

def getDbInfo(targetdb):
    conn = sqlite3.connect(targetdb)
    c = conn.cursor()
    return c, conn

def getCollection(DATABASE = 'test', COLLECTION = 'fnlndob'):
    mongoclient = MongoClient()
    db = mongoclient[DATABASE]
    collection = db[COLLECTION]
    collxn = db.collection
    return collxn

def staging(mongoc):
    """
    This method returns a list of tuples.
    This list can be fed to the SQLite cursor for a executemany operation.

    TO DO: make this method more flexible in terms of what columns get inserted.
    """
    allrecords = []
    for document in mongoc.find():
        alist = []
        alist.append(str(document["_id"]))
        alist.append(document["firstname"])
        alist.append(document["lastname"])
        alist.append(document["DOB"])
        alist.append(calcage(document["DOB"]))

        atuple = tuple(alist)
        
        allrecords.append(atuple)

    return allrecords

def calcage(datestr):
    """
    This method is for calculating a person's age.
    Takes in a string yyyy-mm-dd format.

    Returns age as a string.
    """
    datelist = datestr.split('-')
    yyyy = int(datelist[0])
    mm = int(datelist[1])
    dd = int(datelist[2])

    dob = date(yyyy, mm, dd)
    today = date.today()

    age = str(abs(today - dob).days/365)

    return age    
    
def insertRecords():
    dbinfo = getDbInfo('patientinfo.db')
    sqlc = dbinfo[0]
    conn = dbinfo[1]
    mongoc = getCollection()

    sqlc.execute("DROP TABLE IF EXISTS patientinfo")
    sqlc.execute("CREATE TABLE patientinfo (patientid text, firstname text, lastname text, dob text, age text)")

    allrecords = staging(mongoc)
    sqlc.executemany("INSERT INTO patientinfo VALUES (?, ?, ?, ?, ?)", allrecords)

    for count in sqlc.execute("SELECT count(*) FROM patientinfo"):
        print "Number of records inserted (SQLite):", count[0]

    conn.commit()
    conn.close()
