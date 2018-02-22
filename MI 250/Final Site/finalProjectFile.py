#!/Users/josh/anaconda3/bin/python
import cgi,cgitb, os
from mvc import mvccgi
from mvc.mvccgi import BaseController, BaseModel

try:
   import json
except ImportError:
   import simplejson as json
   
class MyController(BaseController):
   model = BaseModel("session.json", ["user", "Ntweets"])

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '352844557-6wyW8pcr5dU3sMFuwoUpAyHSBqI5vE16jSI8Wuiu'
ACCESS_SECRET = 'fRKDTSxTx3gzEZf9nkOCHFDeql2iL4VZ0hIfBolm9vlfc'
CONSUMER_KEY = '0GKBnjePEePEPwlR8uFSUPU5CEY'
CONSUMER_SECRET = ' CA2hCOhVEzXdWZGYBhxLPgIUKYmoMzwrk891peuGpctfGqamBe'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting the number amount of tweets the user request. 
tweet_count = "Ntweets"
for tweet in iterator:
   tweet_count -= 1
   # Twitter Python Tool wraps the data returned by Twitter 
   # as a TwitterDictResponse object.
   # We convert it back to the JSON format to print/score      
      
   if tweet_count <= 0:
       break
   
def markupTableCell(text):
    return "<td>"+text+"</td>"

def markupTableRow(text):
    return "<tr>"+text+"</tr>"

def createTable(list):
    final = ""
    counter = 0
    while counter < len(list):
        text = ""
        for index in list:
            if counter < 5:
                text += markupTableCell(index)
                if counter == 4:
                    final += markupTableRow(text)
                    text = ""
                counter += 1
            else:
                text += markupTableCell(index)
    final += markupTableRow(text)
        
    return final

def HTMLGenerator(location,list):
    text = """<html>
<head>
    <title>Table</title>
</head>
<body>
<p>
    <a href='/home.html'>Home</a>&nbsp;<a href='/about.html'><b>About</b></a>
</p>
"""
    text += createTable(list)
    text += """</body>
</html>"""

    htmlout = location
    printHTML = open(htmlout,"wt")
    printHTML.write(text)
    printHTML.close()
    