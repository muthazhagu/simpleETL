import requests
import random

def createNameList(rawdata):
    """
    Method returns a list of strings.
    Takes in a request object as raw data.

    This is a helper method. Do not call just by itself.
    """
    namesList = []
    for val in rawdata.text.split('\n'):
        if val: namesList.append(val.strip().split()[0])
    return namesList

def createNewNames(numberofnames = 1):
    """
    Method returns a list of strings of the form 'LASTNAME,[space]FIRSTNAME'.
    The names are formed at random (uniformly distributed).
    Takes in the number of names required as input parameter.
    """
    if numberofnames < 1: numberofnames = 1
    numberofnames = int(numberofnames)
    newnames = []
    for i in range(numberofnames):
        newnames.append(random.choice(lastnames) + ', ' + random.choice(maleAndfemale))
    print "Name generation completed!"
    return newnames

male_url = "http://www.census.gov/genealogy/www/data/1990surnames/dist.male.first"
female_url = "http://www.census.gov/genealogy/www/data/1990surnames/dist.female.first"
lastname_url = "http://www.census.gov/genealogy/www/data/1990surnames/dist.all.last"

male = requests.get(male_url)
female = requests.get(female_url)
lastname = requests.get(lastname_url)

malenames = createNameList(male)
femalenames = createNameList(female)
lastnames = createNameList(lastname)
maleAndfemale = malenames + femalenames

##Uncomment for debugging
##print len(malenames)
##print len(femalenames)
##print len(lastnames)
##print len(maleAndfemale)

##Uncomment lines below to verify above method.
##print createNewNames(10) # must output list with 10 names
##print createNewNames(0.5) # must output list with 1 name
##print createNewNames(-1) # must output list with 1 name

