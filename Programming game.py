def main():
    print("Welcome to my game")
    player_name = input("What is your name")
    print(f"Welcome, {player_name},")
    Lives = 3
    print(f"You have {Lives} lives remaining. ")

backpack = [] # initialise emply list for backpack
#this is a while ture loop to ask the user for another direction of travel
while True:
     
    direction = input("Which direction would you like to go?")

    if direction =="North":
        print("You selcted North")
        puzzle_question = input("What is 2+2")
        if puzzle_question == "4":
            print("Correct")
                        #we would need to collect something here
            backpack.append("Key 1")
        else:
            print("Incorrect")
            Lives -= 1
            print(f"You now have {Lives} lives remaining.")
    elif direction ==  "South":
        print("You selcted South")
        puzzle_question1 = input("What is 2+2")
        if puzzle_question1 == "4":
            print("Correct")
                #we would need to collect something here
       
        else:
            print("Incorrect")
            Lives -= 1
            print(f"You now have {Lives} lives remaining.")

        if direction == "East":
            print("You selcted East")
            puzzle_question2 = input("What is 2+2")
            if puzzle_question2 == "4":
                print("Correct")
                #we would need to collect something here
       
        else:
            print("Incorrect")
            Lives -= 1
            print(f"You now have {Lives} lives remaining.")

        if direction =="West":
            print("You selcted West")
        puzzle_question3 = input("What is 2+2")
        if puzzle_question3 == "4":
             print("Correct")
            #we would need to collect something here
        else:
            print("Incorrect")
            Lives -= 1
            print(f"You now have {Lives} lives remaining.")
     
    else:
        print("Not recongised")
        # if backpack is full open door win game
        if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("Key 4" in backpack):
            if Lives == 0:
                print = ("You have 0 Lives remaing")
        
exit()
main()

        
    
