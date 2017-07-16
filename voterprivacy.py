# Voter Privacy - a demonstration to balance our right of privacy
# with our right to free and fair elections
# Copyright 2017, John Ruberto
#
# the scheme has 3 components: 
# 1 - Encoding state voting records to protect our privacy
# 2 - Aggregating the state records into a single database
# 3 - Checking for duplicates across the various states
# 
# The private voting records remain with the states. Only a tokenized verion of the vote 
# is sent to the central (federal) database. Even better, if a private entity could host the database
# then the federal government need not have access to any of the voter data.  The federal government 
# can receive the results of the queries - not the underlying data itself. 

import json   # The test database will use json. For a real implementation, this would be a DB connection
import datetime

# Global variables. In reality these should be in a database, and not global state. 

fedDatabase = {}  # a dictionary, in reality this would be a database
states = ["CA", "ID", "IN"]  #small test set

duplicates = {}  # container with duplicate voters


#############
#
# tokenize will take state data and import into a federal database
# the federal database only stores the state, the state voter id, and a "tokenized" version of the voter
# the tokenization, here, is a simple prototype - multiplying the DOB with last 4 of SSN.  This should 
# provide an error rate of less than 1 in 150 million.  
# for true privacy, a more involved hashing algorithm should be used.  I'm not trying to roll my own crypto here, just
# start with a prototype. 
#
def tokenize( stateVoterRecords ):
	votes = stateVoterRecords["votes"]
	state = stateVoterRecords["state"]
	for v in votes :
		token = int(v["voterDOB"][0:2] + v["voterDOB"][3:5] + v["voterDOB"][6:10]) * v["voterSSN"]
		fedDatabase[state + str(v["voterId"])] = token
	return


#################
#
# Pulls in individual state data and invokes the tokenization service that builds a federal dabase. 
#
# In a real system, each state will tokenize ther own data and publish only the tokenized data to the federal database
#
def importStateData ():
	
	for state in states :
	    
		with open(state + '.json') as data_file :
			data = json.load(data_file)
			tokenized = tokenize(data)
	return 
		
	
#########################
#
# Check for duplicate voters will scan the federal database looking for the same person (represented by the token) voting in multiple
# states. These duplicate voters will be put into a list for further investigation.
#
def checkForDuplicateVoters() :
	
	listDups = []
	
	for key, value in fedDatabase.items() :
		duplicates.setdefault(value, set()).add(key)
		
	listDups = [key for key, values in duplicates.items() if len(values) > 1]
		
	
	return listDups 
	
	

importStateData()   #imports all state data into the federal database, but the data is not identifiable to an individual

d =  checkForDuplicateVoters()  # checks to see if the same person voted in multiple states

print "duplicate voters are: "
print "voter hash, list of states and the state voter id"
for v in d : 
	print v, duplicates[v]
	
	

	
	