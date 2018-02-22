# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:17:15 2017

@author: super
"""

from http.server import CGIHTTPRequestHandler, HTTPServer

def runCgi():
    print('starting server...')
    # server settings
    server_address = ('127.0.0.1', 8080)
    handler = CGIHTTPRequestHandler
    
    httpd = HTTPServer(server_address, handler)
    print('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()