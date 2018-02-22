#This week, I'd like you to create a csv-based database for storing album info.
#Your database will reside in a csv file with four columns:
#Artist
#Album
#Release Date
#Label
#You can easily open, modify, and save CSV files using spreadsheet software.
#I have attached a csv in the Week 8 folder that you can use.
#For your programming assignment, please implement the following functions:

def add(artist,album,date,label):
# This function should add a new row to the csv
# It should only add a the row if artist and album do not already exist
# Make sure that this function saves the file after it updates!
  import os
  
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  file.close()
  artistBool = contents.find(artist)
  albumBool = contents.find(album)
  if artistBool == -1 and albumBool == -1:
    bool = true
  else:
    bool = false
  
  if bool:
    file = open(file1,"wt")
    text = artist+","+album+","+date+","+label
    file.write(contents)
    file.write(text+"\n")
    file.close()
    return

  else:
    return    

def update(artist, album, field,value):
# This function should update a row that exists
# If a row with artist and album does not exist, 
#the function should return and do nothing
# If the row exists, the function should update the indicating field with the new value
# The valid values for the parameter "field" are "artist","album","date","label"
  import os
  import csv
  
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  file.close()
  artistBool = contents.find(artist)
  albumBool = contents.find(album)
  if artistBool == -1 and albumBool == -1:
    return
  else:
    file = open(file1,"wt")
    editedContents = contents.split("\n")
    del editedContents[-1]    
    test = ""
    counter = 0
    for line in editedContents:
      line = line.split(",")
      if line[0] == artist and line[1] == album:
        if field == "artist":
          editingList = value+","+editedContents[counter].split(",")[1]+","+editedContents[counter].split(",")[2]+","+editedContents[counter].split(",")[3]
          del editedContents[counter]
          editedContents.append(editingList)
        elif field == "album":
          editingList = editedContents[counter].split(",")[0]+","+value+","+editedContents[counter].split(",")[2]+","+editedContents[counter].split(",")[3]
          del editedContents[counter]
          editedContents.append(editingList)
        elif field == "date":
          editingList = editedContents[counter].split(",")[0]+","+editedContents[counter].split(",")[1]+","+value+","+editedContents[counter].split(",")[3]
          del editedContents[counter]
          editedContents.append(editingList)
        elif field == "label":
          editingList = editedContents[counter].split(",")[0]+","+editedContents[counter].split(",")[1]+","+editedContents[counter].split(",")[2]+","+value
          del editedContents[counter]
          editedContents.append(editingList)
        else:
          return
      counter += 1
   
    final = ""
    for line in editedContents:
      final += line+"\n"    
    text = final
    file.write(text)
    file.close()

def find(artist, album):
# This function should find and print any matching entry
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  test = contents.find("test")
  file.close()
  
  editedContents = contents.split("\n")
  del editedContents[-1]
  for line in editedContents:
    editedLine = line.split(",")
    if editedLine[0] == artist and editedLine[1] == album:
      print line

def findByArtist(artist):
# This function should find and print any entries by this artist
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  test = contents.find("test")
  file.close()
  
  editedContents = contents.split("\n")
  del editedContents[-1]
  for line in editedContents:
    editedLine = line.split(",")
    if editedLine[0] == artist:
      print line

def findByLabel(label):
# This function should find and print any entries matching this label
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  test = contents.find("test")
  file.close()
  
  editedContents = contents.split("\n")
  del editedContents[-1]
  for line in editedContents:
    editedLine = line.split(",")
    if editedLine[3] == label:
      print line

def findByDate(date):
# This function should find and print any entries matching this date
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  test = contents.find("test")
  file.close()
  
  editedContents = contents.split("\n")
  del editedContents[-1]
  for line in editedContents:
    editedLine = line.split(",")
    if editedLine[2] == date:
      print line

def showAll():
# This function should find and print all of the entries in the database
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  test = contents.find("test")
  file.close()
  
  editedContents = contents.split("\n")
  for line in editedContents:
    print line

def delete(artist, album):
# This function should delete any matching entry in the database
  import os
  import csv
  
  file1 = "C://Users/Joe Tang/testCSVFile.txt"
  file = open(file1,"rt")
  contents = file.read()
  file.close()
  artistBool = contents.find(artist)
  albumBool = contents.find(album)
  if artistBool == -1 and albumBool == -1:
    del editedContents[-1]
    return
  else:
    file = open(file1,"wt")
    editedContents = contents.split("\n")
    del editedContents[-1]    
    test = ""
    counter = 0
    for line in editedContents:
      line = line.split(",")
      if line[0] == artist and line[1] == album:
        del editedContents[counter]
  
  final = ""
  for line in editedContents:
    final += line+"\n"    
  text = final
  file.write(text)
  file.close()

#def main():
#  var = "test"
#  var1 = "what"
#  add("test",var,var,var)
#  add("nope","nope",var1,var1)
#  add("test",var1,var1,var1)
#  update(var,var,"album",var1)
#  find(var,var1)
#  findByArtist("nope")
#  delete(var,var1)
#  print
#  showAll()
#  
#main()