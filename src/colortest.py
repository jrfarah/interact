# Started by Joseph Farah on May 28, 2017. Notes go up here
# Will be used to test and make libraries for different animations, that will 
# eventually be used with other modules

# -------------- Variable Naming -------------------
# A note on variable naming: use the full name for the function argument and 
# for actual usage use abbreviations if necessary

# Last updated: May 29th, 2017

# begin module imports
from cue_sdk import *
import os
import time

# global variable definitions
tilde = 13
tab = 25
capslock = 37
shift = 49
ctrl = 61
# function definitions, mostly animations

def make_key_flash(key_number,seconds, frequency, red, green, blue):
	'''makes any key flash on the keyboard any color for any amount of time at any frequency
	key_number should be a the return of the get_num_for_key function
	seconds and RGB MUST be an integer
	frequency MUST be a floating point'''

	for counter in range(seconds):
		# this for loop is on a per-second basis, and refreshes once per second
		# key turns off, key turns on, once per second
		for hz in range(int(frequency)):
			Corsair.SetLedsColors(CorsairLedColor(key_number, red, green, blue))
			time.sleep(float(1/(2*frequency)))
			Corsair.SetLedsColors(CorsairLedColor(key_number, 0, 0, 0))
			time.sleep(float(1/(2*frequency)))

def get_num_for_key(key_name):
	'''takes any key name and returns the number value so that it can be used in other functions
	the reason this exists is because I can't figure out how to dynamically apply the CLK.id function
	without creating a giant libary for every key'''

	return Corsair.GetLedIdForKeyName(key_name)

def flash_line_of_keys(start, stop, seconds, frequency, red, green, blue):
	'''will flash row of keys up to specific key. for information on variable names, see make_key_flash function'''

	for counter in range(seconds):
		print 'test'


Corsair = CUESDK("CUESDK_2013.dll")
Corsair.RequestControl(CAM.ExclusiveLightingControl)
# Corsair.SetLedsColors(CorsairLedColor(38, 255, 255,255))
make_key_flash(get_num_for_key('M'), 5, 5.0, 0,255,255)
