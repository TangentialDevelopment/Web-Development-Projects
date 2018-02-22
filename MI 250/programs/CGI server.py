from http.server import CGIHTTPRequestHandler, HTTPServer

def runCgi():
    print('starting server...')
    # server settings
    server_address = ('127.0.0.1', 8080)
    handler = CGIHTTPRequestHandler
    
    # I can configure the directories I want to use here
    handler.cgi_directories = ['C://Users/Documents/stuff/school/MI 250/programs/super/cgi']
    httpd = HTTPServer(server_address, handler)
    print('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

#to run in console: python -m http.server --ccgi 8000