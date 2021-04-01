import io
import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin
"""
    Student: Thu Ngo
    Module: gladysUserInterface
    Description: This module does This gladysUserInterface that should present a text-based menu for users to do the operations.
"""
def runTests():
    """
        tests some module functions
    """
    print("running a few tests")
    average = compute.gpsAverage(4, 5)
    print("average = ", average)
    # delete the remaining code *in this function* and replace it with
    # your code. add more code to do what the assignment asks you to do.
    # add 3 more tests of different functions in different modulesprint("hello!")

def start():
    userName = userLogin.login()
    runApp(userName)
 def runApp(userName):
     # loop until user types q
     userQuit = False
 while (not userQuit):
    #menu
    print("\n")
    print("-------------------------------")  
    print("Welcome to Gladys West Map App")
    print("-------------------------------")
    print("Current position     : x = 56 , y = 13")
    print("Destination position : x = 98 , y = 2")
    print("Distance             : 607.87")
    print("\n")
    print("[c] to set current position")
    print("[d] to set destination position")
    print("[m] to map - which tells the distance")
    print("[t] to run module tests")
    print("[q] to quit")
    print()
        # get first character of input
    userInput = input("Enter a command:")
    lowerInput = userInput.lower()
    firstChar = lowerInput[0:1]
        # menu choices, use a switch-like if-elif control structure
    if firstChar == 'c':
        xCurrent = int(input("Enter a x position: "))
        yCurrent = int(input("Enter a y position: "))

        xDestination = 98
        yDestination = 2
    print("\n")
    print("-------------------------------")
    print("Welcome to Gladys West Map App")
    print("-------------------------------")
    print("Current position     : x = ", xCurrent, ", y = ", yCurrent)
    print("Destination position : x = 98 , y = 2")
    print("Distance             :",distance)
    print("\n")
    print("[c] to set current position")
    print("[d] to set destination position")
    print("[m] to map - which tells the distance")
    print("[t] to run module tests")
    print("[q] to quit")
    print()       
    break
 elif firstChar == 'd':
    xDestination = int(input("Enter a x position: "))
    yDestination = int(input("Enter a y position: "))
    xCurrent = 56
    yCurrent = 13

    print("\n")
    print("-------------------------------")
    print("Welcome to Gladys West Map App")
    print("-------------------------------")
    print("Current position       : x = ", xCurrent,", y = ", yCurrent)
    print("Destination position   : x = ", xDestination, ", y = ",  yDestination)
    print("Distance               :",distance) 
    print("\n")
    print("[c] to set current position")
    print("[d] to set destination position")
    print("[m] to map - which tells the distance")
    print("[t] to run module tests")
    print("[q] to quit")
    print()       
    break
 elif firstChar == 'm':
    print("Distance: " , distance)
    break

    # quit
    if firstChar == 'q':
        userQuit = True
        # run some tests (this is part 1 of 2)
elif firstChar == 't':
    runTests()
else :
    print("ERROR: " + firstChar + " is not a valid command")
print("\n")
print("Thank you for using the Gladys West Map App!")
print("\n")

