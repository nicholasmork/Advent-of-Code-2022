input = open("C:\code\AdventOfCode\\2\\2input.txt")
#A = X  ROCK | B = Y Paper| C = Z Scissors
totalscore= 0
while(input):
    line = input.readline()
    lineToList = line.split()
    if (len(lineToList) == 0):
        break

    if(lineToList[0] == "A" and lineToList[1] == "X"): # Rock + you need to lose scissor
        totalscore += (3+0)
    if(lineToList[0] == "A" and lineToList[1] == "Y"): # Rock + you need to draw Rock
        totalscore += (1+3)
    if(lineToList[0] == "A" and lineToList[1] == "Z"): # Rock + you need to win Paper
        totalscore += (2+6)
    #Rock is handled
    if(lineToList[0] == "B" and lineToList[1] == "X"): #paper and you need to lose rock
        totalscore += (1+0)
    if(lineToList[0] == "B" and lineToList[1] == "Y"): #paper and you need to draw paper
        totalscore += (2+3)
    if(lineToList[0] == "B" and lineToList[1] == "Z"): #paper and you need to win Scissor
        totalscore += (3+6)
    #Paper is handled
    if(lineToList[0] == "C" and lineToList[1] == "X"): #Scissor and you need to lose paper
        totalscore += (2+0)
    if(lineToList[0] == "C" and lineToList[1] == "Y"): #Scissor and you need to draw Scissor
        totalscore += (3+3)
    if(lineToList[0] == "C" and lineToList[1] == "Z"): #Scissor and you need to win Rock
        totalscore += (1+6)

    """
    
    if(lineToList[0] == "A" and lineToList[1] == "Y"): #Rock paper
        totalscore += (2+6)
    if(lineToList[0] == "A" and lineToList[1] == "Z"): #Rock Scissors
        totalscore += (3+0)
    # ROCK vs x is handled
    if(lineToList[0] == "B" and lineToList[1] == "X"): # Paper ROCK
        totalscore += (1+0)
    if(lineToList[0] == "B" and lineToList[1] == "Y"): #Paper paper
        totalscore += (2+3)
    if(lineToList[0] == "B" and lineToList[1] == "Z"): #Paper Scissors
        totalscore += (3+6)
    #Paper vs x is handled
    if(lineToList[0] == "C" and lineToList[1] == "X"): #scissor rock
        totalscore += (1+6)
    if(lineToList[0] == "C" and lineToList[1] == "Y"): #scissor paper
        totalscore += (2+0)
    if(lineToList[0] == "C" and lineToList[1] == "Z"): #scissor scissors
        totalscore += (3+3)
    """
print("ferdig")
print(totalscore)