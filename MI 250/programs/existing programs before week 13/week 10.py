from csv import *
from os import path

def getDbName():
  return getMediaPath("database.csv")

# The following is a python "class" - which is really
# just another complex type, like a "string" or a "pixel"
# It has a set of methods (don't worry about the "__init__")
# and a set of "fields" which are variables that are associated
# with each instance of the class
# The variables that you might care about are:
#
#     headers - a list of the headers for the database
#     data - the full database
#     filename - the name of the file used by the database 
class Db:
  def __init__(self,headers=None,autoflush = true,filename=getDbName()):
    if not path.exists(filename) and headers==None:
      raise ValueError("No headers specified and database does not exists")
    elif path.exists(filename):
      if headers == None:
        f = open(filename,"rb")
        headers = f.readline().split(",")
        f.close()
      if headers != None:
        f = open(filename)
        test = f.readline().split(",")
        f.close()
        if headers!=test:
          raise ValueError("Provided headers do not match those in dbfile")
          
    self.headers = headers
    self.filename = filename
    self.data = []
    self.dirty = false
    self.autoflush = true
    if path.exists(filename):
      self.reload()
  
  def flush(self):
    if not self.dirty:
      false
    f = open(self.filename,"wb")
    w = DictWriter(f,fieldnames=self.headers)
    w.writer.writerow(self.headers)
    for row in self.data:
      w.writerow(row)
    f.close()
    self.dirty = false
  
  def reload(self):
    f = open(self.filename,"rb")
    r = DictReader(f)
    self.data = []
    for row in r:
      self.data.append(row)
    f.close()
    self.dirty = false
  
  def checkColumns(self,fields,partial=true):
    subset = set(fields).issubset(set(self.headers))
    if subset and (partial or (len(fields)==len(self.headers))):
      return true
    else:
      raise ValueError("Invalid columns: "+str(fields))
  
  def find(self,query = None):
    if query==None:
      query = {}
    self.checkColumns(query.keys(),true)
    result = []
    for row in self.data:
      match = true
      for key,value in query.iteritems():
        if row[key]!=value:
          match = false
          break
      if match:
        result.append(row)
    return result
  
  def add(self,row):
    self.checkColumns(row.keys(),false)
    self.data.append(row)
    self.dirty = true
    if self.autoflush:
      self.flush()
      
  def delete(self,query):
    rows = self.find(query)
    ndata = []
    for r in self.data:
      if r not in rows:
        ndata.append(r)
    self.data = ndata
    self.dirty = true
    if self.autoflush:
      self.flush()
    print str(len(rows))+" rows deleted"  
    
def numberScraper(url):
  import urllib
  from csv import *
  connection = urllib.urlopen(url)
  data = connection.read()
  connection.close()
  
  final = []
  entry = []
  editedData = data.split("/n")
  boolValue = false
  for r in editedData:
    editedRow = []
    row = r.split("\n")
    
    for word in row:
      if "<tr" in word:
        boolValue = true
      if "</tr" in word:
        if entry:
          final.append(entry)
        entry = []
        boolValue = false
      if boolValue == true:
        if "<td" in word:
          editedWord = word.split(">")
          for words in editedWord:
            number = ""
            for char in words:
              if char in "0123456789":
                number += char
            if number != "":
              entry.append(number)
  
  return final
  
def output(outputFile):
  file = open(outputFile,"wt")
  final = ""
  data = numberScraper("http://www.espnfc.com/english-premier-league/23/table?season=2016")
  for row in data:
    for entry in row:
      final += entry+","
    final = final[:-1]
    final += "\n"
  file.write(final)
  file.close()
  
def main():
  output("C://Users/Joe Tang/websiteNumberCSV.txt")
  
main()