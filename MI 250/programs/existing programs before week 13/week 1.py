#project 1
#1.  The listing in problem 2.29 defines a function.  Modify this function to take as parameters the height (in stories), the feet per story, and the gravity (in meters).  
#Verify that your function gives different answers for different parameter values, and the same answer for the values in the original listing.
#2. Create a new function that converts the number of feet to the number of meters.  It should take the number of feet as a parameter.  The function should print the number of meters.
#3. Look up the equation for the volume of a sphere.  Write a function that prints out the volume of the earth in miles.
#4. Look up the conversion to convert miles to kilometers.  Write a function that takes a diameter of a sphere (in miles) and prints out the volume of that sphere in kilometers.

import math

def compute(): #1
#base data
#heightInStories = 3
#feetPerStory = 10
#gravityMeters = 9.81
#correct answer: 1.36536448741
  heightInStories = input("enter height in stories: ")
  feetPerStory = input("enter feet per story: ")
  heightInFeet = heightInStories * feetPerStory
  metersPerFoot = 0.3048
  heightInMeters = heightInFeet * metersPerFoot
  gravityMeters = input("enter gravity (in meters): ")
  timeToFall = sqrt((2*heightInMeters)/gravityMeters)
  print("time to fall (second)s:")
  print(timeToFall)

#test data
#1 feet = 0.3048 meters
#15 feet = 4.572 meters
#12.4 feet = 3.77952 meters
def convert(): #2
  feet = input("enter distance in feet: ")
  conversionFactor = 0.3048
  meterConversion = feet * conversionFactor
  print("Meters after conversion:")
  print(meterConversion)
  
#test data
#radius = 3959
#volume = ~260,000,000,000
def findEarthVolume(): #3
  radius = input("enter radius of Earth in miles: ")
  volume = float(4) / 3 * math.pi * radius ** 3
  print ("volume of earth in cubic miles: ")
  print(volume)

#test data
#1 mile = ~2.18243862694 kilometers^3
#15 mile = ~7365.73036591 kilometer^3
#6.2 mile = 520.136233081 kilometer^3
#conversion 1 mile to 1.60934 km
def convertToFindVolume(): #4
  diameter = float(input("enter radius of Earth in miles: "))
  diameterConverted = diameter * 1.60934
  print(diameterConverted)
  radius = diameterConverted / 2
  print(radius)
  volume = float(4) / 3 * math.pi * radius ** 3
  print ("volume in cubic kilometers: ")
  print(volume)

#def main(): for testing purposes
  #compute()
  #convert()
  #findEarthVolume()
  #convertToFindVolume()
#main()