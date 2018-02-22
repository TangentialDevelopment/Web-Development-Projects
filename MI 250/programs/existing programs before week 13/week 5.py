def blend(sourcePicture, targetPicture, targetX, targetY):
  width = getWidth(sourcePicture)
  height = getHeight(sourcePicture)
  midpointX = getWidth(targetPicture)/2
  midpointY = getHeight(targetPicture)/2
  
  emptyPicture = makeEmptyPicture(width,height)
  counterX = 0
  counterY = 0
  for y in range(0,getHeight(sourcePicture)):
    if counterY == getHeight(targetPicture):
      counterY = 0
    for x in range(0,getWidth(sourcePicture)):
      if counterX == getWidth(targetPicture):
        counterX = 0
      newPixel = getPixel(emptyPicture,x,y)
      if x >= targetX-midpointX and y >= targetY-midpointY:
        if y%2 == 0:
          if x%2 == 0:
            pixel = getPixel(sourcePicture,x,y)
            newColor = getColor(pixel)
          else:
            pixel = getPixel(targetPicture,counterX,counterY)
            newColor = getColor(pixel)
            counterX += 2
        else:
          if x%2 == 0:
            pixel = getPixel(targetPicture,counterX,counterY)
            newColor = getColor(pixel)
            counterX += 2
          else:
            pixel = getPixel(sourcePicture,x,y)
            newColor = getColor(pixel)
      else:
        pixel = getPixel(sourcePicture,x,y)
        newColor = getColor(pixel)
      setColor(newPixel,newColor)
    if y >= targetY-midpointY:
      counterY += 1

  return emptyPicture
      
#def main():
#  file1 = "T:/school/Senior Year/FS/MI 250/testcases/ltayf-4.jpg"
#  picture1 = makePicture(file1)
#  file2 = "T:/school/Senior Year/FS/MI 250/testcases/ltayf-6.jpg"
#  picture2 = makePicture(file2)
  
#  picture3 = blend(picture1,picture2,250,300)
#  show(picture3)
  
#main()