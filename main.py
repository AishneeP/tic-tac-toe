def restart_main():
    pass

def printBoard(xState, zState):
    var=[0,0,0,0,0,0,0,0,0]
    
    
    for i in range(0,9):
        var[i]='X' if xState[i] else ('O' if zState[i] else i)
    print(f"{var[0]} | {var[1]} | {var[2]}")
    print(f"--|---|----")
    print(f"{var[3]} | {var[4]} | {var[5]}")
    print(f"--|---|----")  
    print(f"{var[6]} | {var[7]} | {var[8]}")

    tie=True
    for ch in var:
        if(ch=='X' or ch=='O'):
            continue
        else:
            tie=False
            break
    
    if(tie==True):
        print(" IT'S A TIE ")
    
    return tie

def check(xState, zState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for win in wins:
        if(xState[win[0]] + xState[win[1]] + xState[win[2]]==3):
            return 1
        if(zState[win[0]] + zState[win[1]] + zState[win[2]]==3):
            return 0
    return -1
    

if __name__ == "__main__":
    print("---------------------------- NEW GAME --------------------------")   
    xState=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn=1 # for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        t=printBoard(xState,zState)
        if(t==True):
            break
        if(turn==1):
            print("X's Chance")
            value=int(input("Please enter a value between 0 to 8: "))
            if(value<0 or value>8):
                print("Invalid Number")
                break
            xState[value]=1
            
        else:
            print("O's Chance")
            value=int(input("Please enter a value between 0 to 8: "))
            if(value<0 or value>8):
                print("Invalid Number")
                break
            zState[value]=1
            
        winner=check(xState, zState)
        if(winner==1):
            printBoard(xState, zState)
            print(" X IS THE WINNER ")
            break
        elif(winner==0):
            printBoard(xState, zState)
            print(" O IS THE WINNER ") 
            break
        elif(winner==-1):
            turn=1-turn    
    print("---------------------------- GAME OVER --------------------------")    

    # playAgain= int(input("If you want to play again enter 1 else press any key: "))
    # if(playAgain==1):
    #     restart_main()
    

# There is 2 more problems --> handle the case when the index is already o or x
                        #  --> restart the game