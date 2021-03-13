#Program that read in a dict object from file.

import json
filename="testdict.json"

def readDict ():
    # This will throw an error if the file does not exist
    # it should realy just return an empty dict 
    
    with open (filename) as f:
        return json.load(f)

# test the function 
somedict = readDict()
print(somedict)
