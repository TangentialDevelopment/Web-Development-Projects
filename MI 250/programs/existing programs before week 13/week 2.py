#1 Program 13 shows you how to print a pyramid  Create a version of this program that takes a parameter that indicate the number of spaces to indent before the pyramid
#2 Now create a function that allows you to specify a certain number of pyramids to be printed horizontally.
#Note the space between the pyramids  This will be important in the next step
#3 Finally, write a function called buildMegaPyramid that takes as a parameter a number of rows
#Note that this is just indented pyramid on top of two adjacent pyramids You've already written the code for these
#You should be able to call build MegaPyramid with any number you want to generate truly massive pyramids  Think Egypt  Be careful
#4 Create a string manipulation function that takes a string and turns it "inside-out" The easiest way to think about this is to take the two halves of the string, flip them, and put them back together
#For instance, calling insideOut("1234567") yields 3217654 calling insideOut("123456") yields 321654

def pyramid(char):
  space = " "
  char = str(char)
  print (4*space+char)
  print (3*space+3*char)
  print (2*space+5*char)
  print (space+7*char)
  print (9*char)
  
def indentedPyramid(char,indent): #function 1
  space = " "
  char = str(char)
  intIndent = int(indent)
  print (intIndent*space+4*space+char)
  print (intIndent*space+3*space+3*char)
  print (intIndent*space+2*space+5*char)
  print (intIndent*space+space+7*char)
  print (intIndent*space+9*char)

def manyPyramids(char,count): #function 2
  space = " "
  char = str(char)
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  line5 = ""
  for index in range(0,count):
    line5 = line5 + 9*char + " "
    line4 = line4 + space + 7*char + space + " "
    line3 = line3 + 2*space + 5*char + 2*space + " "
    line2 = line2 + 3*space + 3*char + 3*space + " "
    line1 = line1 + 4*space + char + 4*space + " "
  print (line1)
  print (line2)
  print (line3)
  print (line4)
  print (line5)

def buildMegaPyramid(rows): #function 3
  space = " "
  char = "t"
  for index in range(0,rows):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    indent = 5*(rows - index)
    line5 = line5 + indent*space
    line4 = line4 + indent*space
    line3 = line3 + indent*space
    line2 = line2 + indent*space
    line1 = line1 + indent*space
    
    for count in range(0,index+1):
      line5 = line5 + 9*char + " "
      line4 = line4 + space + 7*char + space + " "
      line3 = line3 + 2*space + 5*char + 2*space + " "
      line2 = line2 + 3*space + 3*char + 3*space + " "
      line1 = line1 + 4*space + char + 4*space + " "
    print (line1)
    print (line2)
    print (line3)
    print (line4)
    print (line5)

def insideOut(number): #function 4
  if len(number)%2 == 0:
    half = (len(str(number))/2)-1
  else:
    half = len(str(number))/2
  reverse = number[::-1]
  final = ""
  counter = 0
  for index in range(0,len(number)):
    if (index > half):
      final = final + reverse[index]
  for index in range(0,len(number)):
    if (index <= half):
      final = final + reverse[index]
  print (final)
  

#pyramid("t")
#indentedPyramid("t",5)
#manyPyramids("t",3)
#buildMegaPyramid(3)
#insideOut("1234567") #yields 3217654
#insideOut("123456") #yields 3216754