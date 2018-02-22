def scraper(url,outputfile):
  import urllib
  from csv import *
  connection = urllib.urlopen(url)
  data = connection.read()
  connection.close()
  
  final = []
  editedData = data.split("/n")
  for r in editedData:
    print r
    
def main():
  scraper("http://comartsci.msu.edu","x.csv")
  
main()
  