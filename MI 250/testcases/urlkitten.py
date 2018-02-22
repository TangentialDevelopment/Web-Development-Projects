import urllib

try:
  connection = urllib.urlopen('http://placekitten.com')
  kittens = connection.read()
  connection.close()
  print kittens[599:1000]

except URLError, e:
  print 'no kitten. got an error code:'.e