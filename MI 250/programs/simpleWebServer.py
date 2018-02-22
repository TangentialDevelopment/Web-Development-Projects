# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:59:56 2017

@author: super
"""
#check at http://localhost:8081

from http.server import BaseHTTPRequestHandler, HTTPServer
#from datetime import datetime

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
    #    self.send_response(200)
    #    
    #    self.send_header('Content-type','text/html')
    #    self.end_headers()
    #    
    #    message1 = "<p>Hi there</p>"
    #    message2 = "<strong>hello world!</strong>"
    #    message3 = str(datetime.now())
    #    
    #    self.wfile.write(bytes(message1,"utf8"))
    #    self.wfile.write(bytes(message2,"utf8"))
    #    self.wfile.write(bytes(message3,"utf8"))
    #    
    #    return
        rootdir = 'C:/xampp/htdocs/'
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path,'rb')
            
                self.send_response(200)
            
                self.send_header('Content-type','text-html')
                self.end_headers()
            
                self.wfile.write(f.read())
                f.close()
                return
        
        except IOError:
            self.send_error(404, 'file not found')
    
def run():
    print ("starting Server...")
    server_address = ('127.0.0.1', 8081)
    
    httpd = HTTPServer(server_address, MyRequestHandler)
    
    print ('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()