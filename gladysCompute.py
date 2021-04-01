import io

import gladysSatellite as satellite

"""
	Student: Gabriel Solomon
	Module: gladysCompute
	Description: This module preforms the underlying calculations to figure out 
    the distance between the current position (x,y) and destination position (x,y)
"""
# Start of code by Truc Nguyen
def value(x,y):
	"""
	value = 𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑙𝑎𝑡𝑖𝑡𝑢𝑑𝑒")+𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑙𝑜𝑛𝑔𝑖𝑡𝑢𝑑𝑒")+𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑎𝑙𝑡𝑖𝑡𝑢𝑑𝑒")+𝑔𝑝𝑠𝑉𝑎𝑙𝑢𝑒(𝑥,𝑦,"𝑡𝑖𝑚𝑒")
	"""
	value = satellite.gpsAverage(x,y,"latitude") +satellite.gpsAverage(x,y,"longtitude") +satellite.gpsAverage(x,y,"alttude") + satellite.gpsAverage(x,y,"time")
	return value

"""
Calling a function from a module
"""
#path a json file 
pathToJSONDataFiles = "/Users/trucnguyen/Documents/GitHub/Group-Assignment-6/jsonFiles"
#get data and print it
data = satellite.readSat("longtitude", pathToJSONDataFiles)
#print a value from data list 
print(data = ", data)

def gpsAverage(x, y):
	"""
    	The gpsAverage formula as defined below and return the average to the gladysUserInterface module
	"""
	gpsAverage = value/4
	return gpsAverage



def distance (current, destination):
	"""
	    Computes the distance between the current position and the destination position using the following formulas. 
		Distance = square root(gpsAverage(x current, y current) square + gpsAverage(x destination, ydestination) square)
	"""
	distance = (gpsAverage(xCurrent, yCurrent)**2 + gpsAverage(xDestination, yDestinaion)**2)**0.5
	return distance
"""
calling a function to calculate value from a formula
"""
current = int(input("Enter xCurrent value: ", "Enter yCurrent value: "))
print("current possition: ", distance)

destination = int(input("Enter xDestination value: ", "Enter yDestination value: "))
print("destination possition: ", distance)

#end of code by Truc Nguyen

	
