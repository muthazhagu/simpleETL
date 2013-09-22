from insertdocuments import insertDocuments
from insertrecords import insertRecords
import sys

def main(args):
    """
    This method calls the insertDocuments module, and inserts n number of documents
    into MongoDB.

    Then it calls the insertRecords module to insert the documents in MongoDB in to
    SQLite.
    """
    insertDocuments(numberOfDocs = args)
    insertRecords()
    print "Done!"

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print "Usage  : python main.py <number of records>"
        print "Example: python main.py 1500"
