# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:19:08 2017

@author: super
"""

# Import the necessary methods from "twitter" library
import tweepy
def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

# Variables that contains the user credentials to access Twitter API 
login = {'consumer_key':'vKAGHgNKm3mfkw7fZSezOSIDH',
    'consumer_secret':'xqLWChs53N9CxvlfuUxIo0fvrdjA0iSTmCPo1enbpfJWcjYibm',
    'access_token':'826226955255160832-KkrI1OSvDNXL4mPdL6ZeaTRih7PpOpK',
    'access_token_secret':'5OuW8InwYFDeS8xB8iiAba8HC9ZQLSj5Ef9pzHs3lT1H6'}

api = get_api(login)

tweet = api.search(q = "net nuetrality", rpp = 1, show_user = True)

for entry in tweet:
    text = entry.id
    print(api.get_status(text).text)