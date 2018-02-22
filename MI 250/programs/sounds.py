#done with Mac Lewis

from csv import *
import urllib

# Generates a set of samples for a tone at a given frequency
#   rate - the frequency of the tone
#   seconds - the length of the tone
#   start - the position within the waveform to start at
def genStitchedTone(rate,seconds,start=0):
  result = []
  
  # this is the amount of distance to travel along the waveform
  # for each sample
  dpersample = (2 * pi)*rate/22050.0
  pos = start
  for i in range(seconds * 22050.0):
      # Use the "sin" function here to calculate the amplitude of the signal
      # at each point
      result.append(sin(pos))
      pos = (pos+dpersample) % (2*pi)
      
  # Return a dictionary, with the array of samples in "sound"
  # and the last position in the waveform at pos
  return {"sound":result,"last":pos}

# Helper function to calculate the mean of a list
def calculateMean(list):
  total = 0.0
  for l in list:
    total = total + l
  return total / len(list)

# A simple wrapper function to make sounds of a certain length
# Allows for fractions of a second
def myMakeEmptySoundSeconds(seconds):
  return makeEmptySound(int(seconds*22050))



# Generate a sound that lets us listen to the the stock market
# between 2012 - 2017
def listenToStocks(secondsPerDay = .00005,volume = 3000):
  stocksurl = "https://docs.google.com/spreadsheets/d/1y4l2d2wAi4n75BF1V7BYSN_309oVStNozq6t4tNcMp4/edit?usp=sharing" #have to export it to a csv file
  con = urllib.urlopen(stocksurl)
  csvfile = reader(con)
  #temporary storage for the stock values
  list = []
  

  #read in the stock values
  header = false
  for r in csvfile:
    if header:
      list.append(float(r[0]))
    header = true  

  #calculate mean of all the values
  mean = calculateMean(list)
 
  #make an empty sound of the correct length
  sound =myMakeEmptySoundSeconds(len(list)*secondsPerDay)
  
  #keep track of the sample index
  sidx = 0
  last = 0
  for l in list:
    # these are the values to add
    sampletoadd = genStitchedTone(((l-mean)*30)+440,secondsPerDay,last)
    
    # this is where we wound up in the waveform
    last = sampletoadd["last"]
    
    # adding the samples
    for v in sampletoadd["sound"]:
      setSampleValueAt(sound,sidx,int(v*volume))
      sidx=sidx+1    
  return(sound)
  
play(listenToStocks())