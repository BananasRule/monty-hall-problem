import random
# ///// CONFIG VARIABLES /////
#Number of simulations
numsim = 100000000
# //// Danger: Code below ////

#Create data save file
savedata = open("doorgamestats.txt", "w")
#Int variables
gamecounter = 0
truegamescount = 0
switchedtimes = 0
switchedwins = 0
notswitchedtimes = 0
notswitchedwins = 0
#Defining games
def game():
    switched = 0 
    #Game vars
    car = random.randint(1,3) 
    #Player makes first choice
    playerchoice = random.randint(1,3)
    #Host makes choice
    hostchoice = random.randint(1,3)
    while hostchoice == car or hostchoice == playerchoice:
        hostchoice = random.randint(1,3)

    #Choosing whether to switch doors (random) and recording choice 
    if random.randint(0,1) == 1:
        switched = 1
        oldplayerchoice = playerchoice
        while playerchoice == hostchoice or playerchoice == oldplayerchoice:
            playerchoice = random.randint(1,3)
    #Caculating if you won a car and creating the txt string
    if playerchoice == car:
        string = "1," + str(switched) + "," + str(playerchoice) + "\n"
        savedata.write(string)
    else:
        string = "0," + str(switched) + "," + str(playerchoice) + "\n"
        savedata.write(string)

#Runs games the specified number of times
while truegamescount < (numsim + 1):
    game()
    gamecounter = gamecounter + 1
    #Creates readout to see number of games and measure total games (don't remove)
    if gamecounter == 100000:
        truegamescount = truegamescount + gamecounter
        print(truegamescount)
        gamecounter = 0

savedata.close()
#Calculating Stats
savedata = open("doorgamestats.txt", "r")
#Read line and tally results
for line in savedata:
    won = line[0]
    switched = line[2]
    if switched == '1':
        switchedtimes = switchedtimes + 1
        if won == '1':
            switchedwins = switchedwins + 1
    elif switched == '0':
        notswitchedtimes = notswitchedtimes + 1
        if won == '1':
            notswitchedwins = notswitchedwins + 1
#Calculated Percentages and display
switchedpecentage = switchedwins/switchedtimes*100
notswitchedpecentage = notswitchedwins/notswitchedtimes*100 
print("Switched Percentage: " + str(switchedpecentage))
print("Not Switched Percentage: " + str(notswitchedpecentage))

        

