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

cases = input[0]
pancakesData = input[1:]

i = 0

while i+2 <= len(pancakesData):
    case = pancakesData[i:i+2]
    i += 1
    print(case)
 
