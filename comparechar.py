import hashlib
import pymongo
import sqlite
from pymongo import MongoClient

def mongohandle():
    """
    Method for getting a connection object to MongoDB.
    Takes in DB, and Collection info.
    Returns connection object.
    """
    pass

def sqlhandle():
    """
    Method for getting a cursor, and connection object from SQLite.
    Takes in DB name as input.

    Returns (cursor, connection object) as tuple.
    """
    pass

def buildsourcetext():
    """
    Method concats all char fields in source to form one big string.

    Method returns MD5 digest for the one big string.
    """
    pass

def buildtargettext():
    """
    Method concats all char fields in target to form one big string.

    Method returns MD5 digest for the one big string.
    """
    pass

def computeMD5hash(aString):
    """
    Method to compute MD5 hex digest for a string.
    Takes a string as input.

    Returns MD5 hex digest as string output.
    """
    pass

def comparehash(sourcehash, targethash):
    """
    Method returns True if sourcehash == targethash. False, if otherwise.
    Takes in two strings as input.

    Returns boolean output.
    """
    pass
