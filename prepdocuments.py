import names
import randomdates
from datetime import date

def prepdocuments(numberofrecords = 1):
    """
    Method returns a list of Python dictionaries (MongoDB documents) that can be
    inserted into a MongoDB database.

    Takes one param, number of documents, as input.
    """
    
    documents = []

    randomNames = names.createNewNames(numberofrecords)
    randomDates = randomdates.generate_random_dates(numberofdates = numberofrecords)
    randomNamesandDates = zip(randomNames, randomDates)

    for nameanddate in randomNamesandDates:
        firstname = nameanddate[0].split(',')[1].strip()
        lastname = nameanddate[0].split(',')[0].strip()
        dob = str(nameanddate[1].year) + '-' + str(nameanddate[1].month) + '-' + str(nameanddate[1].day)
##        print firstname, lastname, dob.strip()
        document = {"firstname" : firstname,
                    "lastname" : lastname,
                    "DOB" : dob.strip()}
        documents.append(document)
    print "Documents generation completed!"
    return documents

##Uncomment lines below to test code
##print prepdocuments() #must show one name, one date
##print prepdocuments(0.5) #must show one name, one date
##print prepdocuments(-1) #must show one name, one date
##print prepdocuments(0) #must show one name, one date
##print prepdocuments(5) #must show five names, five dates
