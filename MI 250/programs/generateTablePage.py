def markupTableCell(text):
  return "<td>"+text+"</td>"
  
def markupTableRow(text):
  return "<tr>"+text+"</tr>"
  
def createTableRow(list):
  text = ""
  final = ""
  counter = 0
  bool = false
  while counter <= len(list):
    for t in range(0,4):
      if counter == len(list):
        bool = true
        break
      else:
        text += markupTableCell(list[counter])
        counter += 1
        final += markupTableRow(text)
  
    if bool:
      break
  return final

def makePage():
  import os
  
  fileIn = "C:/Users/super/Documents/stuff/school/MI 250/testcases"
  fileOut = "C:/Users/super/Documents/stuff/school/MI 250/programs/generatedHome.html"
  
  outputFile = open(fileOut,"wt")
  outputFile.write("""<html>
  <head><title>simple generated html</title>
  </head>
  <body>
  <h1>this is all the pictures i have</h1>
  """)
  
  list = []
  for file in os.listdir(fileIn):
    if file.endswith(".jpg"):
      img = "<img src="+"C:/Users/super/Documents/stuff/school/MI&nbsp250/testcases/"+file+" width=100px height=100px>"
      list.append(img)
      
  outputFile.write(createTableRow(list))
  outputFile.write("""</body>
  </html>""")
  
  outputFile.close()
  
def main():
  makePage()
  
main()