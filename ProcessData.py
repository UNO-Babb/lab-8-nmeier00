#ProcessData.py
#Name: nick meier
#Date: april 6, 2025
#Assignment: lab 8

import random

def makeID(first, last, IDnum):
  """creates the user id from the first and last names and the student id"""
  idLen = len(IDnum)
  
  while len(last) < 5:
    last = last + "x"
  
  id = first[0] + last + IDnum[idLen - 3: ]

  #print(id)
  return id


def makeMajorYear(year, major):
  """takes their major and year and turns it into correct format"""
  
  yr = ""

  if year == "Freshman":
    yr = "FR"  
  elif year == "Sophomore":
    yr = "SO"
  elif year == "Junior":
    yr = "JR"
  elif year == "Senior":
    yr = "SR"
  
  majorShort = major[0:3]
  majorShort = majorShort.upper()
  majorYear = majorShort + "-" + yr
  

  return majorYear



def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    studentID = makeID(first, last, idNum)
    majorYear = makeMajorYear(year, major)
    #print(majorYear)
    output = last + "," + first + "," + studentID + "," + majorYear + "\n"
    outFile.write(output)

    


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()



if __name__ == '__main__':
  main()
