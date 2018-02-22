#!/Users/josh/anaconda3/bin/python
import cgi,cgitb, os
import mvc.mvccgi
import mvc.project


cgitb.enable()
v = mvc.mvccgi.BaseViewer("./default.html")
c = mvc.project.MyController(v)
method = os.environ['REQUEST_METHOD']
print(c.handle(cgi.FieldStorage(), method))
