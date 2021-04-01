import io
import jsonFiles
"""
    Student: Mercedez Tran
    Module: gladysSatellite
    Description: This module opens and reads the altitude data file from disk using the readSat function
"""

def readSat(sat, pathToJSONDataFiles):
    """
    reads satellite data from a json file
    """
    # data file path
	fileName = sat + "-satellite.json"
	filePath = pathToJSONDataFiles + "/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		It uses the satellite to pinpoint user's location and desired location to find best possible route
    
	"""

	pathToJSONDataFiles = "/Users/trucnguyen/Documents/GitHub/Group-Assignment-6/jsonFiles"


