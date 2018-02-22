#!C:/Users/super/Andaconda3/bin/python

import cgi, cgitb
cgitb.enable()

def useAPI(search):
    from imgurpython import ImgurClient

    client_id = '37282598175d614'
    client_secret = '0a7842f64bd16cd317c5c1e713e47e531590af59'

    client = ImgurClient(client_id, client_secret)
    
    items = client.gallery_search(search, advanced=None, sort='time', window='all', page=0)
    return items[0].link

form = cgi.FieldStorage()

search = form['search'].value
result = useAPI(search)

print("Content-type:text/html")
print()
print("<html><Head>")
print("<title>Hello CGI</title>")
print("</head>")
print("<body>")
print("<h2>searched for {}</h2>".format(search))
print('<img src="'+ result +'" alt= "image found">')
print("</body>")
print("</html>")