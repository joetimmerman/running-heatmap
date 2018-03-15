#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File: heatmap.py
Original author: Joe Timmerman (https://github.com/joetimmerman)
Date: April 1, 2017

Description:	This script, called by gcexport.py, geneartes a heatmap of activities
				using a .gpx export. 
"""
import parse_coords
import os
import sys

outFP = os.path.join(sys.path[0], 'map.html')
inFP = os.path.join(sys.path[0], 'outline.html' )

def createHeatmap(activitiesDir):

	searchText = '~@~\n'

	coords = parse_coords.getCoordinates(activitiesDir)
	"""
	with open (outFP, 'w') as f:
		f.write('<!DOCTYPE html>\n')
		f.write('<html>\n\t<head>\n')
		f.write('\t\t<title>Simple Map</title>\n')
		f.write('\t\t<meta name="viewport" content="initial-scale=1.0">\n\t\t<meta charset="utf-8">\n\t\t<style>\n')
		f.write('\t\t\t#map {\n\t\t\t\theight: 100%;\n\t\t\t}\n')
		f.write('\t\t\thtml, body {\n\t\t\t\theight: 100%;\n\t\t\t\tmargin: 0;\n\t\t\t\tpadding: 0;\n\t\t\t}\n')
		f.write('\t\t</style>\n\t</head>\n\t<body>\n')
		f.write('\t\t<div id=\"map\"></div>\n')
		f.write('\t\t<script>\n\t\t\tvar map, heatmap;\n\t\t\tfunction initMap() {\n')
		f.write('\t\t\t\tmap = new google.maps.Map(document.getElementById(\'map\'), {\n\t\t\t\t\tcenter: {lat: 40.79, lng: -73.95},\n\t\t\t\t\tzoom: 14,\n\t\t\t\t\tzoom: 14,\n\t\t\t\tmapTypeId: \'satellite\'\n});\n')
		f.write('\t\t\t\theatmap = new google.maps.visualization.HeatmapLayer({\n\t\t\t\t\tdata: getPoints(),\n\t\t\t\t\tmap: map,\n\t\t\t\t\tradius: 15\n\t\t\t\t});\n\t\t\t\theatmap.setmap(map)\n\t\t\t}\n')
		f.write('\t\t\tfunction getPoints() {\n')
		f.write('\t\t\t\treturn [\n')
		for (lat, lon) in coords:
			f.write('\t\t\t\t\tnew google.maps.LatLng('+str(lat)+', '+str(lon)+'),\n')
		f.write('\t\t\t\t];\n\t\t\t}\n')
		f.write('\t\t\t</script>\n')
		f.write('\t\t<script async defer\n\t\t\tsrc="https://maps.googleapis.com/maps/api/js?key=AIzaSyDC1F2XP97GBu2-uJRtJhBGMIXw6u96uyU&libraries=visualization&callback=initMap">\n\t\t</script>\n')
		f.write('\t</body>\n</html>')
	"""

	with open(inFP, 'r') as inFile:
		lines = inFile.readlines()
		i = lines.index(searchText)
		for (lat, lon) in coords:
			lines.insert(i, '\t\t\t\t\tnew google.maps.LatLng('+str(lat)+', '+str(lon)+'),\n')
		del lines[i]
		lines.remove(searchText)
	with open(outFP, 'w') as outFile:
		outFile.writelines(lines)













