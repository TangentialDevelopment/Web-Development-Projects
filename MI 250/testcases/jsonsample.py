import simplejson as json

s = """
[ { "firstName": "Josh",
    "lastName": "Introne",
    "age":24,
    "student": false},
  {  "firstName": "Jody",
     "lastName": "schumaker",
     "age": 32,
     "student": true  } ]
"""

obj = json.loads(s)
for i in obj:
  print i["firstName"]