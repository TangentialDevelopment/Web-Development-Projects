#!C:/Users/super/Andaconda3/bin/python
# -*- coding: utf-8 -*-

import cgi,cgitb, os, tweepy
from mvc import mvccgi
from mvc.mvccgi import BaseController, BaseModel

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def searchTwitter(search):
    login = {'consumer_key':'vKAGHgNKm3mfkw7fZSezOSIDH',
             'consumer_secret':'xqLWChs53N9CxvlfuUxIo0fvrdjA0iSTmCPo1enbpfJWcjYibm',
             'access_token':'826226955255160832-KkrI1OSvDNXL4mPdL6ZeaTRih7PpOpK',
             'access_token_secret':'5OuW8InwYFDeS8xB8iiAba8HC9ZQLSj5Ef9pzHs3lT1H6'}

    api = get_api(login)
    
    tweet = api.search(q = search, lang = "en", rpp = 1)
    final = []

    for entry in tweet:
        text = entry.id
        final.append(api.get_status(text).text)
    return final

def markupTableCell(text):
    return "<td>"+str(text)+" "+"</td>"

def markupTableRow(text):
    return "<tr>"+text+"</tr>"

def createTable(list):
    final = ""
    text = ""
    for index in list:
        text += markupTableCell(index)
    final += markupTableRow(text)
        
    return final

def makeString(list):
    final = ""
    for entry in list:
        final += entry
    return final

class MyController(BaseController):
    model = BaseModel("session.json", ["search", "found"])
    

    def home_POST(self, params):

        if 'myname' in params:
            name = params['myname'].value
            results = searchTwitter(name)
            self.model.updateOrAdd({"search":name},{"found":results})

        elif 'logout' in params:
            self.model.clear()

        return self.home_GET(params)


    def home_GET(self, params):

        if 'myname' in params:
            name = params['myname'].value
            found = self.model.find({"search":name})
            query = found[0]["search"]
            
            results = found[0]["found"]
            endList = []
            for entry in results:
                endList.append(entry.encode("utf-8"))
            table = createTable(endList)
            
            history = ""
            history = self.model.storage["data"][0]
            past = createTable(history)
            
            return self.viewer.getPage("results.html", {"query":query,
                                                        "tweet":table, 
                                                        "past":past})

        else:
            return self.viewer.getPage("search.html")
        

cgitb.enable()
v = mvccgi.BaseViewer("./default.html")
c = MyController(v)
method = os.environ['REQUEST_METHOD']

c.respond(cgi.FieldStorage(), method)
