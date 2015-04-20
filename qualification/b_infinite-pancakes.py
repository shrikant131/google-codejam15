from itertools import islice

print("Please add your input:")
input = []
stopword = ""
while True:
    line = raw_input()
    if line.strip() == stopword:
        break
    
    input.append(line)
    
#print("Here is your input:")

try:
    cases = input[0]
    pancakesData = input[1:]
except:
    print "Invalid lists"

i = 0

while i+2 <= len(pancakesData):
    case = pancakesData[i].split() + pancakesData[i+1].split()
    i += 1
    print(case)

case.sort()

numPeople = case[0]
pancakePiles = case[1:]

for i in range(len(pancakePiles)):
#    while pancakePiles[i+1] is not None:
        if (int(pancakePiles[i]) + 2) <= int(pancakePiles[i+1]):
    	    max = int(pancakePiles[i+1])

print(max)

#largestPile = case[1]
#smallPile = 0

#for pile in range(len(pancakePiles)):
        
#if int(pancakePiles[pile]) >= (int(largestPile) + 2):
#            smallPile = int(largestPile)
#            largestPile = int(pancakePiles[pile])
#    print(largestPile)
#    print(smallPile)
    
#    [x for x in pancakePiles
   # largePileCount = 0
    
    
#for pile in:
#        while int(largestPile) - 2 not in a:
#	     if int(largestPile) - 1 in a:
#	         largePileCount += 1
 
