from itertools import islice

# Allow for user input

print("Please add your input:")
input = []
stopword = ""
while True:
    line = raw_input()
    if line.strip() == stopword:
        break
    
    input.append(line)
    
#print("Here is your input:")

maxShy = input[0]
d = 0

# Add total number of people present in audience
for c in input[1:]:
    d += 1
    numList = list(c)
    sumList = numList[2:]
    count = 0
    for i in sumList:
        count += int(i)
    #print("This is the count")
    #print(count)
    
# Calculate number of people needed
    stoodUp = 0
    numNeeded = 0
    for i in range(len(sumList)):
        if stoodUp + numNeeded >= i:
            stoodUp += int(sumList[i])
        else:
            numNeeded = i - stoodUp
            stoodUp += int(sumList[i])
    
    print("Case #%d: %d" % (d, numNeeded))
