#exam 1
#question 1
def staircase(char,size,height):
  size = int(size)
  height = int(height)
  final = ""
  for x in range(0,height):
    for counter in range(0,size):
      stairSize = x + 1
      output = (char * stairSize) * 2
      if x == height - 1 and counter == size - 1:
        final += output
      else:
        final += output + "\n"
  return final

def reverseStaircase(char,size,height):
  size = int(size)
  height = int(height)
  stairHeight = height
  final = ""
  for x in range(0,height):
    stairHeight -= 1
    for counter in range(0,size):
      stairSize = stairHeight + 1
      output = (char * stairSize) * 2
      if x == height - 1 and counter == size - 1:
        final += output
      else:
        final += output + "\n"
  return final
  
#question3
def pyramid(char,size,height,number):
  final = ""
  for x in range(0,number):
    if x != 0:
      final += "\n"
    start = staircase(char,size,height)
    end = reverseStaircase(char,size,height-1)
    final += start + "\n" + end
  return final

#question 4
def replaceCharacters(stringSet,statement):
  outputString = ""
  previousChar = ""
  for x in statement:
    x = x.lower()
    if x in stringSet:
      outputString += previousChar
    else:
      previousChar = x
      outputString += previousChar
  return (outputString)

#question 5
def imageManip1(source):
  width = getWidth(source)
  height = getHeight(source)
  counterY = 0
  counterX = 0
  
  canvas = makeEmptyPicture(width,height)
  for y in range(0,height):
    counterX = 0
    for x in range(0,width,2):
      old = getPixel(source,x,y)
      color = getColor(old)
      new = getPixel(canvas,counterX,counterY)
      new2 = getPixel(canvas,counterX+(width/2),counterY)
      setColor(new,color)
      setColor(new2,color)
      counterX += 1
    counterY += 1
  return canvas

#question 6
def imageManip2(source,division):
  width = getWidth(source)
  height = getHeight(source)
  counterY = 0
  counterX = 0
  
  canvas = makeEmptyPicture(width,height)
  for y in range(0,height):
    counterX = 0
    for x in range(0,width,division):
      old = getPixel(source,x,y)
      color = getColor(old)
      for x in range(0,division):
        newX = (counterX+(width/division)*x)
        new = getPixel(canvas,newX,counterY)
        setColor(new,color)
      counterX += 1
    counterY += 1
  return canvas

#question 7
def imageManip3(source,division):
  width = getWidth(source)
  height = getHeight(source)
  counterY = 0
  counterX = 0
  
  canvas = makeEmptyPicture(width,height)
  for x in range(0,width):
    counterY = 0
    for y in range(0,height,division):
      old = getPixel(source,x,y)
      color = getColor(old)
      for y in range(0,division):
        newY = (counterY+(height/division)*y)
        new = getPixel(canvas,counterX,newY)
        setColor(new,color)
      counterY += 1
    counterX += 1
  return canvas
  
#question 8
def imageManip4(source,divisionX,divisionY):
  width = getWidth(source)
  height = getHeight(source)
  canvas = makeEmptyPicture(width,height)
  
  canvas = imageManip2(source,divisionX)
  canvas = imageManip3(source,divisionY)
  
#question 9
def marathon(runner,scene,yfrom,yto,number):
  import random
  done = 1
  w = getWidth(scene)
  h = getHeight(scene)
  canvas = makeEmptyPicture(w,h)
  for sourceY in range(0,h):
    for sourceX in range(0,w):
      px = getPixel(scene,sourceX,sourceY)
      color = getColor(px)
      tx = getPixel(canvas,sourceX,sourceY)
      setColor(tx,color)
      
    
  while done <= number:
    randY = random.randint(yfrom,yto)
    randX = random.randint(0,w)
    
    for px in getPixels(runner):
      x = getX(px)
      y = getY(px)
      if randX+x >= w or randY+y >= h:
        continue
      else:
        bgPx = getPixel(canvas,randX+x,randY+y)
        pxcol = getColor(px)
        if (distance(pxcol,white) > 15.0):
          setColor(bgPx,pxcol)
    
    done += 1
  show (canvas)
  writePictureTo(canvas,"/Users/super/Documents/stuff/school/MI 250/testcases/problem10.jpg")

def main():
  #print (staircase("#",3,5))
  #print (reverseStaircase("#",2,5))
  #print(pyramid("#",2,5,2))
  #print(replaceCharacters("ojs","Josh is a good boy"))
  file = "/Users/super/Documents/stuff/school/MI 250/testcases/problem5Input.jpg"
  picture = makePicture(file)
  #picture = imageManip1(picture)
  #picture = imageManip2(picture,5)
  #picture = imageManip3(picture,5)
  #imageManip4(picture,4,20)
  #show (picture)
  file2 =  "/Users/super/Documents/stuff/school/MI 250/testcases/problem9.input.runner.jpg"
  file3 =  "/Users/super/Documents/stuff/school/MI 250/testcases/problem9.input.scene.jpg"
  picture2 = makePicture(file2)
  picture3 = makePicture(file3)
  marathon(picture2,picture3,3,9,5)
  
main()