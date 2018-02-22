# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:38:24 2017

@author: super
"""

def htmlize(word,tag):
    start = "{}{}{}".format("<",tag,">")
    end = "{}{}{}".format("<",tag,">")
    return ("{}{}{}".format(start,word,end))

def makeTableRow(word,tag="td"):
    result = []
    for i in word:
        result.append(htmlize(i,tag))
    return(htmlize("".join(result),"tr"))
    
def makeTableWithHeaders(l):
    result = ""
    headers = []
    for i in l:
        if not result:
            for h in i.keys():
                headers.append(h)
            result = result+makeTableRow(headers,"th")
        row = []
        for h in headers:
            row.append(i[h])
        result = result+makeTableRow(row)
    return (htmlize(result, "table"))

import tweepy
import twitter

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def post():
    finalList = []
    text = """<html>
    <head><title>python generated html</title>
    </head>
    <body>"""
    login = {'consumer_key':'vKAGHgNKm3mfkw7fZSezOSIDH',
    'consumer_secret':'xqLWChs53N9CxvlfuUxIo0fvrdjA0iSTmCPo1enbpfJWcjYibm',
    'access_token':'826226955255160832-KkrI1OSvDNXL4mPdL6ZeaTRih7PpOpK',
    'access_token_secret':'5OuW8InwYFDeS8xB8iiAba8HC9ZQLSj5Ef9pzHs3lT1H6'}
    
    api = get_api(login)
    
    search_text = "#MI250"
    search_number = 10
    search_result = api.search(search_text, rpp=search_number)
    for i in search_result:
        temp_dict = {"text":i.text,"name":i.user.name,"time":i.created_at}
        finalList.append(temp_dict)
    text += makeTableWithHeaders(finalList)
    text += """</body>
    </html>"""
    
    filePath = "C://Users/super/Documents/stuff/school/MI 250/testcases/twitterResults.html"
    htmlOut = open(filePath,"wt")
    htmlOut.write(text)
    htmlOut.close()
    
if __name__ == '__main__':
    post()