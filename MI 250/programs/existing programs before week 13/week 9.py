#done with Mac Lewis

from csv import *
def scraper(url,outputfile):
  import urllib
  connection = urllib.urlopen(url) #reads the data
  data = connection.read()
  connection.close()
  
  final = [] #THIS IS A LIST at the end, go through the list and print everything out orderly to an output file
  editedData = data.split("/n") #separates by line
  for r in editedData: #goes through every line
    row = r.split(" ") #takes out the spaces at the start/end i think
    for word in row:
      if "<link" in word: #searches for whereever there is a link tag
        position = row.index(word) #notes where that link is
        for entry in row[position:]: #prints the rest of the line in the link tag
          if "href" in entry: #makes sure it is a redirect
            if "http://" in entry or "https://" in entry: #makes sure it is a targeted resource
              finalEntry = [url,entry,"link"] #list final format
              final.append(finalEntry) #addes to the end of the list final
  for r in editedData: #goes through every line
    row = r.split(" ") #takes out the spaces at the start/end i think
    for word in row:
      if "<img" in word: #searches for whereever there is a link tag
        position = row.index(word) #notes where that link is
        for entry in row[position:]: #prints the rest of the line in the link tag
          if "src" in entry: #makes sure it is a redirect
            if "http://" in entry or "https://" in entry: #makes sure it is a targeted resource
              finalEntry = [url,entry,"img"] #list final format
              final.append(finalEntry) #addes to the end of the list final
  for r in editedData: #goes through every line
    row = r.split(" ") #takes out the spaces at the start/end i think
    for word in row:
      if "<a" in word: #searches for whereever there is a link tag
        position = row.index(word) #notes where that link is
        for entry in row[position:]: #prints the rest of the line in the link tag
          if "href" in entry: #makes sure it is a redirect
            if "http://" in entry or "https://" in entry: #makes sure it is a targeted resource
              finalEntry = [url,entry,"a"] #list final format
              final.append(finalEntry) #addes to the end of the list final
  file = open(outputfile,"wt")
  content = ""
  for set in final:
    line = ""
    for data in set:
      line += data + ","
    line = line.rstrip(",")
    content += line+"\n"
  file.write(content)
  file.close()

def main():
  scraper("http://comartsci.msu.edu","C://Users/Joe Tang/websiteCSV.txt")
  
main()
  