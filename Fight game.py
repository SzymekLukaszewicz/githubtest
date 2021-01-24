import random

opponent_last_move = 0
def fighting_game():
    print("Welcome in my extraordinary fighting game !\nType help for information")
    logic = True
    fighting = False
    blocking = False
    command = ""
    while logic:
        opponent_mov()
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
            elif(opponent_last_move == 1):
                print("But he hit you back")

        elif command == "block":
            if fighting:
                print("You cannot throwing punches, and block at the same time")
            elif blocking:
                print("You already have your guard up !")
            elif not fighting:
                blocking = True
                print("You blocking incoming punches")

            if(opponent_last_move == 1):
                print("You blocked opponent")
            elif(opponent_last_move == 2):
                print("But no punches came!")
                #hp = hp - 1
        elif command == "stop":
            if not fighting:
                print("You stopped already, gather your energy !")
            else:
                fighting = False
                blocking = False
                print("You stopped throwing punches...")
            if(opponent_last_move == 3):
                print("But opponent run away!")
        elif command == "quit":
            break
        else:
            print("I don't understand this command :<")


def opponent_mov():
    rand_num = random.choice(range(1,3))
    global opponent_last_move
    opponent_last_move = rand_num
    return rand_num
    # if(rand_num == 1):
    #     print("opponent attacked")
    # elif(rand_num == 2):
    #     print("opponent blocked")
    # else:
    #     print("opponent run away")

fighting_game()
