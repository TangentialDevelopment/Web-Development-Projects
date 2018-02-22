# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:05:58 2017

@author: super
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class FileRequestHandler(BaseHTTPRequestHandler):
    #handle GET command
    def do_GET(self):
        #send code 200 response
        self.send_response(200)
        
        #send header first
        self.send_header('Content-type','text-html')
        self.end_headers()
        
        message = """<html>
<head><title>python generated html</title>
</head>
<body><h1>printed image</h1>
"""
        search = self.path[1:]
        text = useAPI(search)
        message += '<img src="'+ text +'" alt= "image found">'
        message += """
</body>
</html>"""
        self.wfile.write(bytes(message,"utf8"))
        
        return
            
def useAPI(search):
    from imgurpython import ImgurClient

    client_id = '37282598175d614'
    client_secret = '0a7842f64bd16cd317c5c1e713e47e531590af59'

    client = ImgurClient(client_id, client_secret)
    
    items = client.gallery_search(search, advanced=None, sort='time', window='all', page=0)
    return items[0].link
    
        
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