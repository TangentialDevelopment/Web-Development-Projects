# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:38:24 2017

@author: super
"""

import tweepy

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def post():
    login = {'consumer_key':'vKAGHgNKm3mfkw7fZSezOSIDH',
    'consumer_secret':'xqLWChs53N9CxvlfuUxIo0fvrdjA0iSTmCPo1enbpfJWcjYibm',
    'access_token':'826226955255160832-KkrI1OSvDNXL4mPdL6ZeaTRih7PpOpK',
    'access_token_secret':'5OuW8InwYFDeS8xB8iiAba8HC9ZQLSj5Ef9pzHs3lT1H6'}
    
    message = "test this is posted by python #MSU #MI250"
    
    api = get_api(login)
    
    status = api.update_status(status=message)
    
if __name__ == '__main__':
    post()