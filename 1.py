

#read input from file

input = open("C:\code\AdventOfCode\\1\\1input.txt")
listWithElfs = []

teller = 0
while(input):

    line = input.readline()
    
    if (line) == "\n":
        listWithElfs.append(teller)
        teller = 0
        continue       
    if int(line) == 5509: #cheated a bit to check if I had read through the whole file
        break
    teller += int(line)


#print(listWithElfs)
#print(max(listWithElfs))
listWithElfs.sort(reverse= True)
print(listWithElfs) #sorted list