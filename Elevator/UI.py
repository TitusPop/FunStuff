'''
The UI module
'''
import Logic

storyes = [1,2,3,4,5,6,7]
liftA = 1
liftB = 7

matrix = [['Storyes', 'A','B'], # the default matrix
          ['7', '-','*'],
          ['6', '-','-'],
          ['5', '-','-'],
          ['4', '-','-'],
          ['3', '-','-'],
          ['2', '-','-'],
          ['1', '*','-']]

def showMenu():
    """Prints the menu
    Input: no input
    Output: the menu"""

    print ("PLEASE CHOOSE AN OPTION: ",'\n')
    print ("1.Show the elevator states ")
    print ("2.Choose your floor and call the elevator ")
    print ("0.Exit")
    
def showElevatorStates(liftA,liftB):
    """Prints the states of the elevators
    Input: no input
    Output: the states"""

    print ("Elevator A is at floor ",liftA)
    print ("Elevator B is at floor ",liftB,'\n')


def secondOption(liftA,liftB):
    """This is the second option that you can choose. You can choose a floor, the correct elevator comes to that floor,
    then you can choose the destination, and the elevator goes there;
    Input: the elevators
    Output: the states and for each floor, displays which elevator is going up/down"""

    Logic.remakeMatrix(0,0,liftA,liftB,matrix) #resets the matrix
    Logic.printTable(matrix)
    showElevatorStates(liftA,liftB)
    
    stop = False
    while stop == False: #a loop so you can choose multiple times before closing the program
        print("Call the elevator from floor: ")
        floor = int(input())
        if floor > 0 and floor < 8:
            if Logic.bestLift(liftA,liftB,floor) == liftB:
                print("The B elevator will come, from floor: ", liftB)
                prevB = liftB
                liftB = floor
                Logic.remakeMatrix(0,prevB,liftA,liftB,matrix) #prevA=0 means that the matrix is changing only for elevator B
                Logic.printTable(matrix)
                stop = True
            else:
                print("The A elevator will come, from floor: ", liftA)
                prevA = liftA
                liftA = floor
                Logic.remakeMatrix(prevA,0,liftA,liftB,matrix)
                Logic.printTable(matrix)
                stop = True
            showElevatorStates(liftA,liftB)
        else:
            print("Invalid floor")
        
    stop = False
    while stop == False: #same here
        print("Choose the destination: ")
        if floor > 0 and floor < 8: #without this line, if the floor is incorrect, previousfloor will become an incorrect floor
            previousfloor = floor
        floor = int(input())
        if floor > 0 and floor < 8:
            if liftA == previousfloor:
                liftA = floor
                Logic.remakeMatrix(previousfloor,0,liftA,liftB,matrix)
                Logic.printTable(matrix)
                stop = True
                showElevatorStates(liftA,liftB)
            if liftB == previousfloor:
                liftB = floor
                Logic.remakeMatrix(0,previousfloor,liftA,liftB,matrix)
                Logic.printTable(matrix)
                stop = True
                showElevatorStates(liftA,liftB)
        else:
            print("Invalid floor")


def start(liftA,liftB):
    """This is the start function, and the controller for the menu
    input: the lifts
    output: """

    stop = False
    while stop == False: # and here
        showMenu()
        option=int(input())
        if option == 1:
            showElevatorStates(liftA,liftB)
        elif option == 2:
            secondOption(liftA,liftB)
        elif option == 0:
            stop = True
        else:
            print("Invalid option")


start(liftA,liftB)