import io
import math
import gladysSatellite as satellite
"""
	Student: Truc Nguyen
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
# read the satellite data
satellite = readSat(sat, pathToJSONDataFiles)
def readSat(sat, pathToJSONDataFiles):
	"""
		reads satellite data from a json file
	"""
def sat():
    """
    fileName = sat + "-satellite.json"
    """
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
	distance = (gpsAverage(xCurrent, yCurrent)**2 + gpsAverage(xDestination, yDestination)**2)**0.5
	return distance
"""
calling a function to calculate value from a formula
"""
xCurrent = int(input("Enter xCurrent value: "))
print("xCurrent possition: ", xCurrent)
yCurrent = int(input("Enter yCurrent value: "))
print("yCurrent possition: ", yCurrent)

xDestination = int(input("Enter xDestination value: "))
print("xDestination possition: ", xDestination)
yDestination = int(input("Enter yDestination value: "))
print("yDestination possition: ", yDestination)
#end of code by Truc Nguyen

	