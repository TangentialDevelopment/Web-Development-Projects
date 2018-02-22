from http.server import CGIHTTPRequestHandler, HTTPServer

class MvcCgiHandler(CGIHTTPRequestHandler):

    controller_path = "controller.py"
    def is_cgi(self):

        original = self.path
        self.path=self.controller_path
        params_idx = original.find("?")
        if params_idx > -1:
            self.path += original[params_idx:]+"&_orig_url="+original[:params_idx]
        else:
            self.path +="?_orig_url="+original

        print(self.path)
        return super().is_cgi()



def runMvcCgi():
    print('starting server...')
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8080)
    handler = MvcCgiHandler
    handler.cgi_directories=['/']
    handler.controller_path = "controller.py"
    # I can configure the directories I want to use here
    httpd = HTTPServer(server_address, handler)
    print('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__=="__main__":
    runMvcCgi()