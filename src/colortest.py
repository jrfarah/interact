# Started by Joseph Farah on May 28, 2017. Notes go up here
# testing the git repo

from cue_sdk import *
import os
import time

Corsair = CUESDK("CUESDK_2013.dll")
Corsair.RequestControl(CAM.ExclusiveLightingControl)
Corsair.SetLedsColors(CorsairLedColor(CLK.H 255, 255,255))

time.sleep(10)