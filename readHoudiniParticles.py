# Coder : Jim Bae
# Data : 2015.08.27

# read particleName.geo or particleName.bgeo
# particle attributes : P, v, id, age, life

import json
import simplejson as json
import hjson

filePathName  = 'data/particle_4Attributes.geo'
geo = hjson.load(open(filePathName, 'r'))

isBGEO = False
if ".bgeo" in filePathName:
	isBGEO = True

#================
# Read Header 
#================

gNumPoint = 0
gNumAttr = 0

print "======================================================"

for i in range(len(geo)):

	if geo[i] == "fileversion":
		print ">>> file version			: ", geo[i+1]
	if geo[i] == "pointcount":
		gNumPoint = geo[i+1]
		print ">>> point count			: ", gNumPoint
	if geo[i] == "vertexcount":
		print ">>> vertex count			: ", geo[i+1]
	if geo[i] == "primitivecount"
		print ">>> primitive count		: ", geo[i+1]
	if geo[i] == "info"
		infoValue = geo[i+1]
		print ">>> artist				: ", infoValue['artist']
		attrSum = infoValue['attribute_summary']
		attrSplit = attrSum.split(",")
		attrList = list()
		for a in range(len(attrSplit)):
			if a == 0:
				firstAttr = attrSplit[a].split("\t")
				attrList.append(fistAttr[1])
			else a == len(attrSplit)-1:
				lastAttr = attrSplit[a].split("\n")
				attrList.append(lastAttr[0])
			else:
				attrList.append(attrSplit[a])
		gNumAttr = len(attrList)
		print ">>> # of attributes 		: ", gNumAttr
		print ">>> attributes list 		: ", attrList

print "======================================================"

#================
# Read Values
#================

for i in range(len(geo)):

	if geo[i] == "attributes":
		geoListDepth1 = geo[i+1]
		geoListDepth2 = geoListDepth1[1]

		for a in range(len(geoListDepth2)):
			geoListDepth3 = geoListDepth2[a]

			nameList  = geoListDepth3[0]
			valueList = geoListDepth3[1]

			# get 'P' values
			for n in range(len(nameList)):
				if( nameList[n] == "name") and (nameList[n+1] == "P"):
					print "================================================"
					print ">>> Having \'P\' attributes in pointattribute"
					print "================================================"

					for k in range(len(valueList)):
						if valueList[k] == "values":
							values = valueList[k+1][len(valueList[k+1])-1]
							#print value
							pValueList = list()
							if isBGEO:
								for pIdx in range(gNumPoint):
									onePointList = list()
									onePointList.append(values[pIdx*3])
									onePointList.append(values[pIdx*3+1])
									onePointList.append(values[pIdx*3+2])
									onePoint.append(1)
									pValueList.append( onePointList )
							else:
								pValueList = values

							for pIdx in range(len(pValueList)):
								print pValueList[pIdx]

			# get 'V' values
			for n in range(len(nameList)):
				if( nameList[n] == "name") and (nameList[n+1] == "v"):
					print "================================================"
					print ">>> Having \'v\' attributes in pointattribute"
					print "================================================"

					for k in range(len(valueList)):
						if valueList[k] == "values":
							values = valueList[k+1][len(valueList[k+1])-1]
							#print value
							pValueList = list()
							if isBGEO:
								for pIdx in range(gNumPoint):
									onePointList = list()
									onePointList.append(values[pIdx*3])
									onePointList.append(values[pIdx*3+1])
									onePointList.append(values[pIdx*3+2])
									pValueList.append( onePointList )
							else: # is geo
								pValueList = values

							for pIdx in range(len(pValueList)):
								print pValueList[pIdx]

			# get 'id' values
			for n in range(len(nameList)):
				if( nameList[n] == "name") and (nameList[n+1] == "id"):
					print "================================================"
					print ">>> Having \'id\' attributes in pointattribute"
					print "================================================"

					for k in range(len(valueList)):
						if valueList[k] == "values":
							values = valueList[k+1][len(valueList[k+1])-1]
							pValueList = list()

							if isBGEO:
								for vIdx in range(len(values)):
									pValueList.append( values[vIdx] )
							else: # is geo
								for v in range(len(values)):
									if type(values[v]) == list:
										pValueList = values[v]

							for pIdx in range(len(pValueList)):
								print pValueList[pIdx]

			# get 'age' values
			for n in range(len(nameList)):
				if( nameList[n] == "name") and (nameList[n+1] == "age"):
					print "================================================"
					print ">>> Having \'age\' attributes in pointattribute"
					print "================================================"

					for k in range(len(valueList)):
						if valueList[k] == "values":
							values = valueList[k+1][len(valueList[k+1])-1]
							pValueList = list()

							if isBGEO:
								for vIdx in range(len(values)):
									pValueList.append( values[vIdx] )
							else: # is geo
								for v in range(len(values)):
									if type(values[v]) == list:
										pValueList = values[v]
										
							for pIdx in range(len(pValueList)):
								print pValueList[pIdx]

			# get 'life' values
			for n in range(len(nameList)):
				if( nameList[n] == "name") and (nameList[n+1] == "life"):
					print "================================================"
					print ">>> Having \'life\' attributes in pointattribute"
					print "================================================"

					for k in range(len(valueList)):
						if valueList[k] == "values":
							values = valueList[k+1][len(valueList[k+1])-1]
							pValueList = list()

							if isBGEO:
								for vIdx in range(len(values)):
									pValueList.append( values[vIdx] )
							else: # is geo
								for v in range(len(values)):
									if type(values[v]) == list:
										pValueList = values[v]
										
							for pIdx in range(len(pValueList)):
								print pValueList[pIdx]

		break





