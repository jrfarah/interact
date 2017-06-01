# Started by Joseph Farah on May 28, 2017. Notes go up here
# Will be used to test and make libraries for different animations, that will 
# eventually be used with other modules

# -------------- Variable Naming -------------------
# A note on variable naming: use the full name for the function argument and 
# for actual usage use abbreviations if necessary

# Last updated: May 31th, 2017

# begin module imports
from cue_sdk import *
import os
import time
from ctypes import *

# global variable definitions
# key values were taken from the enum file in the SDK
tilde = 13
tab = 25
capslock = 37
shift = 49
ctrl = 61


# classes if necessary

class PowerClass(Structure): 
	'''yeah im not really sure what this does but apparently it helps get the current battery life'''
	_fields_ = [('ACLineStatus', c_byte),
			        ('BatteryFlag', c_byte),
			        ('BatteryLifePercent', c_byte),
			        ('Reserved1',c_byte),
			        ('BatteryLifeTime',c_ulong),
			        ('BatteryFullLifeTime',c_ulong)]



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

def flash_line_of_keys(stop, seconds, frequency, red, green, blue):
	'''will flash row of keys in sequence up to specific key. for information on variable names, see make_key_flash function'''

	# trying to avoid problems with number types (you have to use .value to get thee number from an enum)
	stop = stop.value
	# this series of if statements is for determining which row the key is on
	if stop > 61:
		beginning = ctrl
	elif stop > 49 and stop < 61:
		beginning  = shift
	elif stop > 37 and stop < 49:
		beginning = capslock
	elif stop > 25 and stop < 37:
		beginning = tab	
	elif stop > 13 and stop < 25:
		beginning = tilde

	stop = float(stop)
	beginning = float(beginning)

	for counter in range(seconds):
		for hz in range(int(frequency)):
			for key in range(int(beginning), int(stop)+1):
				Corsair.SetLedsColors(CorsairLedColor(key, red, green, blue))
				time.sleep(float(1/(frequency*((stop-beginning+1)))))
				# Corsair.SetLedsColors(CorsairLedColor(key, 0, 0, 0))
				# time.sleep(float(1/(frequency*((stop-beginning+1)))))
		for key in range(int(beginning), int(stop)+1):
			Corsair.SetLedsColors(CorsairLedColor(key, 0, 0, 0))

def get_current_battery_percentage():
	'''uses that weird class up above to get the current battery percentage to display on the keyboard'''
	powerclass = PowerClass()
	result = windll.kernel32.GetSystemPowerStatus(byref(powerclass))
	print powerclass.BatteryLifePercent


Corsair = CUESDK("CUESDK_2013.dll")
Corsair.RequestControl(CAM.ExclusiveLightingControl)

# EVERYTHING COMMENTED OUT HERE IS EXAMPLE FUNCTION USES NOT OLD CODE
# WILL BE MOVING THIS TO BE WITHIN THE FUNCTIONS THEMSELVES SOON

# Corsair.SetLedsColors(CorsairLedColor(38, 255, 255,255))
# make_key_flash(get_num_for_key('M'), 5, 5.0, 0,255,255)
# flash_line_of_keys(get_num_for_key('L'), 10, 1.5, 255,255,255)
get_current_battery_percentage()