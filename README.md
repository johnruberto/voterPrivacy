# voterPrivacy
Recent investigations about voter fraud have risen issues about voter privacy. This prototype code attempts to provide a framework to allow fraud investigation while protecting privacy. 

Some states are refusing to comply with the federal request, citing privacy concerns. https://www.wsj.com/articles/trumps-voting-commission-to-get-limited-state-data-1498884433

This respository shows a method to balance the need for voter privacy while checking for duplicate votes across states. 

1) States would encode the voting records and provide only the encoded version to a federal database. In this example, the
   voter's Date of Birth is combined with the last 4 of Social Security number. 
2) The federal database can then be searched for duplicate voters. When duplicates are found, the feds would know the states involved and an identifier of the voter (that identifier is only known to the states). 
3) The states can then proceed with the voter fraud investigation.  

This is just an afternoon prototyping session.  To use a scheme like this, there would be many changes required:
- The tokenization scheme here is too trival, a more secure method using crypto methods used in password hashing would be more appropriate
- Local storage & json files would instead be a database
- functions would be replaced by web services. 
- instead of a federal database, maybe a 3rd party would host the consolidated data, but share results of the duplicate search with all authorities


