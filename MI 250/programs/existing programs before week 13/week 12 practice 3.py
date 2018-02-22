def advanceToRow(text,start):
  counter = 0
  for line in text:
    if "<tr" in line:
      if start in line:
        return counter
      else:
      counter += 1
        continue
    else:
      counter += 1
  return -1
  
def extractRow(text,start):
  final = 0
  for line in text:
    if start in line:
      counter = 0
      for char in line:
        counter += 1
        test = char + line[counter+1]
        if test == "td":
          final += 1
    else:
      continue
  return final
  
def countSnakeBites(type,file):
  file = open(file,"rt")
  contents = file.read()
  file.close()
  
  counter = 0
  index = 0
  key = 0
  
  while advanceToRow(contents,index) != -1:
    check = []
    index = advanceToRow(contents,index)
    check = extractRow(contents[index],type)
    counter += len(check)
  