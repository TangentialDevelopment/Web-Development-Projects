#ins: 2 pictures and a file name
#out: one picture outwritten to somewhere
#fill bottom half of first picture with second picture
#have to repeat the 2nd half of picture if too small

def mixPicture1(sourcePicture,addPicture,filename): #question 1
  pixelList1 = getPixels(sourcePicture)
  pixelList2 = getPixels(addPicture)
  counter = 0
  height = getHeight(addPicture)
  for index in range(len(pixelList1)/2,len(pixelList1)):
    if counter == len(pixelList2):
      counter = 0
    pixel1 = pixelList2[counter]
    color1 = getColor(pixel1)
    pixel2 = pixelList1[index]
    setColor(pixel2,color1)
    counter += 1

  writePictureTo(sourcePicture,"T:/school/Senior Year/FS/MI 250/testcases/"+filename)
  
#alternate pixels and then loop if one of them is shorter
def mixPicture2(picture1,picture2,filename):
  pixelList1 = getPixels(picture1)
  pixelList2 = getPixels(picture2)
  if len(pixelList2) > len(pixelList1):
    pixelList1 = getPixels(picture2)
    pixelList2 = getPixels(picture1)
  index1 = 0
  counter = 0
  
  for index in range(0,len(pixelList1)):
    if counter % 2 == 0:
      counter += 1
      continue
    else:
      originalPixel = pixelList1[counter]
      changePixel = pixelList2[index1]
      color = getColor(changePixel)
      setColor(originalPixel,color)
      index1 += 1
      counter += 1
  
  writePictureTo(picture1,"T:/school/Senior Year/FS/MI 250/testcases/"+filename)

def main():
  file1 = "T:/school/Senior Year/FS/MI 250/testcases/ltayf-4.jpg"
  file2 = "T:/school/Senior Year/FS/MI 250/testcases/ltayf-6.jpg"
  picture1 = makePicture(file1)
  picture2 = makePicture(file2)
  
  #mixPicture1(picture1,picture2,"test.jpg")
  mixPicture2(picture1,picture2,"test2.jpg")
  
  
main()