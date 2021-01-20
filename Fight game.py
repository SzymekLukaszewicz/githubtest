import random

def fighting_game():
    print("Welcome in my extraordinary fighting game !\nType help for information")
    logic = True
    fighting = False
    blocking = False
    command = ""
    opponent_last_move = 0
    while logic:
        command = input("> ")
        if command == "help":
            print("""
    start - to start a fight
    block - to start blocking
    stop - to stop a fight
    quit - to quit fight
            """)
        elif command == "start":
            if fighting:
                print("You already fighting, focus on that !")
            else:
                fighting = True
                print("You started throwing punches !")
                if(opponent_last_move == 2):
                    print("But he blocked you!!")
        elif command == "block":
            if fighting:
                print("You cannot throwing punches, and block at the same time")
                if(opponent_last_move == 1):
                    print("You blocked opponent")
            elif blocking:
                print("You already have your guard up !")
            elif not fighting:
                blocking = True
                print("You blocking incoming punches")
        elif command == "stop":
            if not fighting:
                print("You stopped already, gather your energy !")
            else:
                fighting = False
                blocking = False
                print("You stopped throwing punches...")
        elif command == "quit":
            break
        else:
            print("I don't understand this command :<")

        rand_num = random.choice(range(1,3))
        opponent_last_move = rand_num
        if(rand_num == 1):
            print("opponent attacked")
        elif(rand_num == 2):
            print("opponent blocked")
        else:
            print("opponent run away")

fighting_game()
