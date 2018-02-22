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
  
def main():
  import os
  
  fileIn = "C:/Users/super/Documents/stuff/school/MI 250/testcases/python.txt"
  file1 = open(fileIn, encoding="utf-8")
  content = file1.read()
  file1.close()
  
  list = searcher(content)
  pythonList = extractor(list)
  text = writer(pythonList)
  
  fileOut = "C:/Users/super/Documents/stuff/school/MI 250/testcases/pythonCases.csv"
  file2 = open(fileOut, "wt")
  file2.write(text)
  file2.close()
  
main()