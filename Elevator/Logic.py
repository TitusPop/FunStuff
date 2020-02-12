'''
The Logic module
'''

def bestLift(A,B,n):
    """This function finds the lift that will come to the selected floor 
    Input: Lift A, Lift B, the floor
    Output: The correct lift"""

    absA = abs(n-A)
    absB = abs(n-B)
    if absA<absB:
        return A
    elif absB<absA:
        return B
    elif A<B:
        return A
    else:
        return B

def printTable(matrix):
    """Prints the matrix and makes it look like a table
    Input: the matrix
    Output: prints the table"""

    dash = '-' * 20
    for i in range(len(matrix)):
        if i == 0:
            print(dash)
            print('{:<10s}{:>2s}{:>5s}'.format(matrix[i][0],matrix[i][1],matrix[i][2]))
            print(dash)
        else:
            print('{:^7s}{:>5s}{:>5s}'.format(matrix[i][0],matrix[i][1],matrix[i][2]))


def remakeMatrix(previousA,previousB,liftA,liftB,matrix):
    """Rewrites the matrix, showing the path of the elevators
    Input: previous floors, the current floors, the matrix
    Output: the new matrix"""

    for i in range(1,len(matrix)):
        if liftB == int(matrix[i][0]):
            matrix[i][2] = '*' # '*' -> the elevator is here
        else:
            matrix[i][2] = '-' # '-' -> no elevator here
        if liftA == int(matrix[i][0]):
            matrix[i][1] = '*'
        else:
            matrix[i][1] = '-'
    if previousB != 0: # if previousB is 0, it means that the elevator A is the one that's moving
        if previousB < liftB:
            for i in range(len(matrix)-previousB,len(matrix)-liftB,-1):
                matrix[i][2] = '^' # '^' -> going up
        if previousB > liftB:
            for i in range(len(matrix)-previousB,len(matrix)-liftB):
                matrix[i][2] = 'v' # 'v' -> going down
    if previousA !=0: # if previousA is 0, it means that the elevator B is the one that's moving 
        if previousA < liftA:
            for i in range(len(matrix)-previousA,len(matrix)-liftA,-1):
                matrix[i][1] = '^'
        if previousA > liftA:
            for i in range(len(matrix)-previousA,len(matrix)-liftA):
                matrix[i][1] = 'v'

