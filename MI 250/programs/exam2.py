# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:22:16 2017

@author: Joe Tang
"""

def neutralityScraper(): #problem 1
    file = open("C://Users/super/Documents/stuff/school/MI 250/testcases/reddit.json","rt")
    contents = file.read()
    file.close()
    
    editedData = contents.split(",")
    count = 0
    for entry in editedData:
        tester = entry.lower()
        if "neutrality" in tester:
            count += 1
    return count

def nonNeutralityScraper(): #problem 2
    file = open("C://Users/super/Documents/stuff/school/MI 250/testcases/reddit.json","rt")
    contents = file.read()
    file.close()
    
    editedData = contents.split("{")
    count = 0
    tempCount = 0
    for entry in editedData:
        tester = entry.lower()
        if "neutrality" in tester:
            continue
        else:
            editedTester = tester.split(",")
            for index in editedTester:
                if "ups" in index:
                    tempCount= int(index[8:])
                    count += tempCount
    return count

def vowelCounter(sentance):
    count = 0
    for char in sentance:
        if char in "aeiou":
            count += 1
    return count

def sentanceSplitter(text):
    final = []
    index = 0
    start = 0
    sentance = ""
    for char in text:
        if char in ".?!":
            sentance = text[start:index]
            start = index+2
            final.append(sentance)
        index += 1
    return final

def tagSplitter(text):
    final = []
    editedText = text.split("<")
    for entry in editedText:
        if entry[0] == "p":
            text = entry[3:].strip("\n")
            final.append(text)
    return final
    

def htmlVowelCounter(): #3
    file = open("C://Users/super/Documents/stuff/school/MI 250/testcases/flatland.html","rt")
    contents = file.read()
    file.close()
    
    vowelCount = 0
    largest = 0
    sentance = ""
    text = tagSplitter(contents)
    for entry in text:
        splitParagraph = sentanceSplitter(entry)
        for index in splitParagraph:
            vowelCount = vowelCounter(index)
            if vowelCount > largest:
                sentance = index
    return sentance

def tableFinder(n,text):
    value = 0
    number = 0
    final = ""
    for entry in text:
        if "table" in entry:
            value = 1
            number += 1
        elif "/table" in entry:
            value = 0
        if value and number == n:
            final += entry
    return final

def rowFinder(text):
    print (text)
    editedText = text.split(">")
    for entry in editedText:
        if "<tr" in entry:
            position = row.index(word)
            for entry in row[position:]:
                print (entry)

def nbaSchedule():
    file = open("C://Users/super/Documents/stuff/school/MI 250/testcases/schedule.html","rt")
    contents = file.read()
    file.close()
    
    editedText = contents.split("<")
    table = tableFinder(1,editedText)
    rowFinder(table)
    
    
def main():
    #print (neutralityScraper())
    #print (nonNeutralityScraper())
    #print (vowelCounter("this is a test"))
    #text = "When I first brought my cat home from the humane society she was a mangy, pitiful animal. It cost a lot to adopt her: forty dollars. And then I had to buy litter, a litterbox, food, and dishes for her to eat out of. Two days after she came home with me she got taken to the pound by the animal warden. There's a leash law for cats in Fort Collins. If they're not in your yard they have to be on a leash. Anyway, my cat is my best friend. I'm glad I got her. She sleeps under the covers with me when it's cold. Sometimes she meows a lot in the middle of the night and wakes me up, though."
    #print (sentanceSplitter(text))
    #print (htmlVowelCounter())
    nbaSchedule()
    
main()