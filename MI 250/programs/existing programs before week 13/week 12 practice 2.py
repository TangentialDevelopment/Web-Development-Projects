def searcher(text):
    masterList = []
    entry = []
    counter = 0
    for char in text:
        if char not in ".?!":
            entry.append(char)
        else:
            text = ""
            counter += 1
            masterList.append(counter)
            for char in entry:
                text += char
                counter += 1
            text = text.strip("\n")
            text = text.strip("\n\t")
            masterList.append(text)
            masterList.append(counter)
            entry = []
    
    return masterList
    
def extractor(list):
    finalList = []
    for entry in list:
        if isinstance(entry, int):
            continue
        elif "python" in entry:
            position = list.index(entry)
            finalList.append(entry)
            finalList.append(list[position-1])
            finalList.append(list[position+1])
    
    return finalList
    
def writer(list):
    final = ""
    iterator = 0
    for entry in list:
        entry = str(entry)
        if iterator != 2:
            final += entry + ","
            iterator += 1
        else:
            final += entry + "\n"
            iterator = 0
    return final
  
def markupTableCell(text):
  return "<td>"+text+"</td>"

def markupTableRow(text):
  return "<tr>"+text+"</tr>"
  
def createTableRow(list):
  final = ""
  counter = 0
  while counter < len(list):
    text = ""
    for index in range(0,2):
      text += markupTableCell(list[index+counter])
      counter += 3
      final += markupTableRow(text)
      
  return final

def HTMLGenerator(list):
  newList = list.split(",")
  text = """<html>
<head><title>simple generated html</title>
</head>
<body>
<h1>generated html</h1><table>"""

  text += createTableRow(newList)
    
  text += """</table></body>
</html>"""

  return text
  
def main():
  import os
  
  fileIn = "T:/school/Senior Year/FS/MI 250/testcases/python.txt"
  file1 = open(fileIn, "rt")
  content = file1.read()
  file1.close()
  
  list = searcher(content)
  pythonList = extractor(list)
  text = writer(pythonList)
  
  HTMLRaw = "T:/school/Senior Year/FS/MI 250/testcases/generatedHome.html"
  HTMLOut = open(HTMLRaw,"wt")
  finalOutput = HTMLGenerator(text)
  HTMLOut.write(finalOutput)
  HTMLOut.close()
  
  fileOut = "T:/school/Senior Year/FS/MI 250/testcases/pythonCases.csv"
  file2 = open(fileOut, "wt")
  file2.write(text)
  file2.close()
  
main()