#done with MacRay Lewis
def changeLittle(fromFile,toFile,newString):
  file = open(fromFile,"rt")
  contents = file.read()
  file.close()
  
  addtext = contents.find("addText")
  firstQuote = contents.find('"',addtext)
  endQuote = contents.find('"',firstQuote+1)
  
  newFile = open(toFile,"wt")
  newFile.write(contents[:firstQuote+1])
  newFile.write(newString)
  newFile.write(contents[endQuote:])
  newFile.close()
  
def main():
  import os
  file1 = setMediaPath("C:/Users/super/Documents/stuff/school/MI 250/programs/littlePicture.py")
  file2 = setMediaPath("C:/Users/super/Documents/stuff/school/MI 250/programs/changedLittlePicture.py")
  changeLittle(file1,file2,"this is a test")
  
main()