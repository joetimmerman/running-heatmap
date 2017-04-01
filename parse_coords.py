#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File: pard_coords.py
Original author: Joe Timmerman (https://github.com/joetimmerman)
Date: April 1, 2017

Description:	This script parses out a directory of .gpx files into 
"""


from lxml import etree
import glob
from random import randrange
import os

def getCoordinates(activitiesDir, lowLat=None, highLat=None, lowLon=None, highLon=None):
	# Use arguments to define a range of allowed lat/lon coordinates
	# Google heatmap algorithm seems to have issues with coords spread across
	# multiple regions, so you may need to restrict to a smaller region to
	# get good results. 
	path = os.path.join(activitiesDir, '*.gpx')
	#path = "C:/Users/joe/Documents/running-heatmap/2017-03-31_garmin_connect_export/*.gpx"
	lats = []
	lons = []
	i = 0 

	for f in glob.glob(path):
			try:
				tree = etree.parse(f)
			except:
				a = 'b'
			root = tree.getroot()
			trk = root[1]
			trkseg = trk[2]
			for trkpt in trkseg:
				if isInRange(trkpt, lowLat, highLat, lowLon, highLon):
					lats.append(round(float(trkpt.get('lat')),7))
					lons.append(round(float(trkpt.get('lon')),7))
	return zip(lats, lons)



def isInRange(trkpt, lowLat, highLat, lowLon, highLon):
	lat = float(trkpt.get('lat'))
	lon = float(trkpt.get('lon'))
	if lowLat is not None: 
		if lat < lowLat:
			return False
	if highLat is not None:
		if lat > highLat:
			return False
	if lowLon is not None:
		if lon < lowLon:
			return False
	if highLon is not None:
		if lon > highLon:
			return False
	return True


