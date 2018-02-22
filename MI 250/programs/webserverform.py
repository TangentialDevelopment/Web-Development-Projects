# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:30:14 2017

@author: super
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class FileRequestHandler(BaseHTTPRequestHandler):
    #handle GET command
    def do_GET(self):
        #directory to serve
        rootdir = '/Users/super/Documents/stuff/school/MI 250/testcases/'
        try:
            if self.path.endswith('.html'):
                #self.path is the requested file
                f = open(rootdir + self.path,'rb')
            
                #send code 200 response
                self.send_response(200)
                
                #send header first
                self.send_header('Content-type','text-html')
                self.end_headers()
                
                #send file content to client
                self.wfile.write(f.read())
                f.close()
                
                # Send message back to client
                message = "Hello "+getParameters(self.path)[1]["data"]
                self.wfile.write(bytes(message,"utf8"))
                
                return
            else:
                self.send_error(400,"could not serve "+self.path)
        except IOError:
            self.send_error(404, 'file not found')

def getParameters(path):
    data = path.split("?")
    result = {}
    if (len(data)>1):
        for p in data[1].split("&"):
            kv = p.split("=")
            result[kv[0]]=kv[1]
    return ([data[0],result])
            
def run():
    print ("starting Server...")
    server_address = ('127.0.0.1', 8081)
    
    httpd = HTTPServer(server_address, FileRequestHandler)
    
    print ('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()