# Started by Joseph Farah on May 28, 2017. Notes go up here
# will be used to test and make libraries for different animations, that will 
# eventually be used with other modules
#
# Last updated: May 29th, 2017

# begin module imports
from cue_sdk import *
import os
import time

# function definitions, mostly animations

def make_key_flash(key_number,time, frequency):
	'''makes any key flash on the keyboard for any amount of time at any frequency'''


def get_num_for_key(key_name):
	'''takes any key name and returns the number value so that it can be used in other functions
	the reason this exists is because I can't figure out how to dynamically apply the CLK.id function
	without creating a giant libary for every key'''
	
	return Corsair.GetLedIdForKeyName(key_name)

Corsair = CUESDK("CUESDK_2013.dll")
Corsair.RequestControl(CAM.ExclusiveLightingControl)
Corsair.SetLedsColors(CorsairLedColor(38, 255, 255,255))
