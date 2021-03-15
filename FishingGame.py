#Add wait function to cast
#Add different fishing zone to choose
#Have different fish for different zone

import random
import time


#This function returns the user decision to quit, view the rules or cast again
def GameOptions():
    #local variables
    choice = str()

    print()
    print("Select an option from the menu")
    print()
    print("\t\tCast\t=\tC")
    print("\t\tRules\t=\tR")
    print("\t\tQuit\t=\tQ")
    print()
    print("Enter your choice: ")
    print()
    choice = input()
    choice = choice.upper()
    return choice

#asks player if theyd like to start the game
def StartGame():
     #local variables
    choice = str()

    print()
    print("Would you like to start a game?: ")
    print()
    print("\t\tEnter anything besides N to play")
    print()
    choice = input()
    choice = choice.upper()
    return choice

#this function lets the user choose where theyd like to fish
def ChooseArea(name):
    areachoice = str()
    print()
    print("Where would you like to fish,",name,"?: ")
    print()
    print("\t\tBeach | Pond")
    print()
    areachoice = input()
    areachoice = areachoice.upper()
    print()

    return areachoice

#gets the username
def UserName():
    name = input("What is your name?: ")
    return name

#this function prints out the rules
def GameRules():
    print()
    print("\tThe object of this game is to rack up as many points as you can within 5 turns")
    print("\tAfter each cast, the player gets a certain amount of points depending on which fish they catch")
    print()
    print("\t**********************************************")
    print("\t\tEmpty Liquor Bottle = 0 points\n\t\tMinnow = 1 point\n\t\tGoldfish = 2 points\n\t\tBass = 3 points\n\t\tTrout = 4 points")
    print("\t**********************************************")
    print()
    
#this function introduces the game when beach is selected
def IntroductionBeach(username):
    print()
    print("   _\/_                 |                _\/_ ")
    print("   /o\\             \       /            //o\ ")
    print("    |                 .---.                |  ")
    print("  _ |_______     --  /     \  --     ______|__")
    print("            `~^~^~^~^~^~^~^~^~^~^~^~`")
    print()
    print(username, "looks out at the vast blue sea taking in the suns warm rays and listening to the water roll in and out of the shore.", username, "takes a seat on fallen palm tree, planting their feet into the ankle high water, they ready their fishing pole.")
    print()

#this function introduces the game when pond is selected
def IntroductionPond(username):
    print()
    print("                                  >')                 ")
    print("               _   /              (\\         (W)     ")
    print("              =') //               = \     -. `|'     ")
    print("               ))////)             = ,-      \(| ,-   ")
    print("              ( (///))           ( |/  _______\|/____ ")
    print("~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-':::::::::::::: ")
    print("            _                 ,----'::::::::::::::::: ")
    print("         {><_'c   _      _.--'::::::::::::::::::::::: ")
    print("__,'`----._,-. {><_'c  _-'::::::::::::::::::::::::::: ")
    print(":.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.: ")
    print(".:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:. ")
    print("MJP.................................................. ")
    print()
    print(username, "wakes up from a short nap on the park bench that overlooks the pond. Their fishing pole stands erected by their side and tucked into the benches crevice to keep it standing. The bobber bows up and down lazily, just as it had been for the last 6 hours.",username, "begins reeling the line in and packing their fishing gear when all of sudden... SPLASH!", username, "caught only a glimpse of the beast before it descended into the murky pond. That small glimpse was all it took to reinvigorate.")

#this function generates a random number for the cast function (specific to its location)
def CastBeach(name, userpoints):
    randint = int()
    randint = random.randint(1, 5)
    fish = str()
    points = int()
    points = userpoints + points
    if randint == 1:
        fish = "a nasty pair of old boots too worn to wear."
        points = 0
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(3)
        print("...")
        time.sleep(3)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    elif randint == 2:
        fish = "a small Yellow tang."
        points = 1
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(2)
        print("...")
        time.sleep(2)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    elif randint == 3:
        fish = "a Tuna!"
        points = 2
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(2)
        print("...")
        time.sleep(2)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    elif randint == 4:
        fish = "Wow! A Blue marlin. Cant wait to tell my brother-in-law about this one!"
        points = 3
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(3)
        print("...")
        time.sleep(3)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    else:
        fish = "a diamond ring! Watch out, ladies!"
        points = 4
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(3)
        print("...")
        time.sleep(3)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    
    return points

#this function generates a random number for the cast function (specific to its location)
def CastPond(name, userpoints):
    randint = int()
    randint = random.randint(1, 5)
    fish = str()
    points = int()
    points = userpoints + points
    if randint == 1:
        fish = "an empty liquor bottle, it reminds them of their father..."
        points = 0
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(3)
        print("...")
        time.sleep(3)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    elif randint == 2:
        fish = "a duck, and it swam away with your bait... Thats 3 years good luck!"
        points = 1
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(2)
        print("...")
        time.sleep(2)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    elif randint == 3:
        fish = "a Goldfish! How'd that get in here?"
        points = 2
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(2)
        print("...")
        time.sleep(2)
        print()
        print(name, "caught ", fish, "\t", points, " points")
        print()
    elif randint == 4:
        fish = "a Catfish! Psst... Wanna hear a secret? I don't have a fishing license. ha ha, shhhhh."
        points = 3
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(3)
        print("...")
        time.sleep(3)
        print()
        print(name, "caught ", fish, "\t", points, " points")
        print()
    else:
        fish = "a big ole' Pond-Trout, wowee!"
        points = 4
        print()
        print(name, "casts the line and waits.")
        print()
        time.sleep(3)
        print("...")
        time.sleep(3)
        print()
        print(name, " caught ", fish, "\t", points, " points")
        print()
    
    return points

#this fuction shows end game score
def EndScore(totalpoints, name):
    score = totalpoints
    if score <= 5:
        print("Not a good fishing day, ",name, " goes back home depressed")
    elif score <= 10:
        print("Not a bad day for fishin', ",name, " heads home tired")
    elif score <= 15:
        print("That was a great fishing day! ",name, " feels like a new man!")
    else:
        print("The best fishing day of ",name, "'s life!", name, " quits his job and becomes a full time fisherman.")


    
def main():
        #variables
        user_choice = str()
        userpoints = int()
        totalpoints = int()
        castnum = int()
        another_game = str()
        fishing_area = str()

    #put everything in a loop so its possible to play again and again
        another_game = StartGame()
        while another_game != 'N':
            #get username, pick fishing area and start introduction
            name = UserName()
            fishing_area = ChooseArea(name)

            while fishing_area != 'BEACH' and fishing_area != 'POND':
                fishing_area = ChooseArea(name)
            if fishing_area == 'BEACH':
                #start inroduction
                IntroductionBeach(name)
       
                #Get user choice to see options
                castnum = 5
                while user_choice != 'Q' and castnum > 0:
                    user_choice = GameOptions()
        
       
                    if user_choice == 'C':
                        userpoints = CastBeach(name, userpoints)
                        totalpoints = totalpoints + userpoints
                        print()
                        print("\t\t\t\t\tYour current score is: ", totalpoints)
                        castnum = castnum - 1
                        print("\t\t\t\t\tcasts left: ",castnum)
                    
                    elif user_choice == 'R':
                        GameRules()
                    #end if
                EndScore(totalpoints, name)
                userpoints = 0
                totalpoints = 0
                another_game = StartGame()
            #end if
            #if beach is not chosen we go to the pond area
            else:
                #start inroduction
                IntroductionPond(name)
       
                #Get user choice to see options
                castnum = 5
                while user_choice != 'Q' and castnum > 0:
                    user_choice = GameOptions()
        
                    if user_choice == 'C':
                        userpoints = CastPond(name, userpoints)
                        totalpoints = totalpoints + userpoints
                        print()
                        print("\t\t\t\t\tYour current score is: ", totalpoints)
                        castnum = castnum - 1
                        print("\t\t\t\t\tcasts left: ",castnum)
                    
                    elif user_choice == 'R':
                        GameRules()
                    #end if
                EndScore(totalpoints, name)
                #reset score for next round
                userpoints = 0
                totalpoints = 0
                another_game = StartGame()

main()
            

