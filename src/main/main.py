###########
# Imports #
###########

import threading
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from RpiMotorLib.RpiMotorLib import A4988Nema

#############
# Variables #
#############

# Stages:
# 0 -> Setup Stage -> loading and setting up all values, etc.
# 1 -> Initial Stage -> Line Sensors and Line Follower
# 2 -> First cube detected -> (still act like stage 1)
# 3 -> Second cube detected -> Run final Scripted process:
#       * Close in on second cube
#       * grab cube
#       * lift cube
#       * turn cube
#       * drive back
#       * release cube
stage = 0

# Pins (Name structure PIN_[Component]_[Pin_type])
PIN_M1_DIR: 2  # Motor 1, DIR Pin
PIN_M1_STEP: 3  # Motor 1, Step Pin
PIN_M1_EN: 4  # Motor 1, Enable Pin
PIN_M2_DIR: 14
PIN_M2_STEP: 15
PIN_M2_EN: 18
PIN_M3_DIR: 17
PIN_M3_STEP: 27
PIN_M3_EN: 22
PIN_M4_DIR: 23
PIN_M4_STEP: 24
PIN_M4_EN: 25
PIN_M5_DIR: 10
PIN_M5_STEP: 9
PIN_M5_EN: 11
PIN_LS1: 0  # Line Sensor 1 Pin
PIN_LS2: 1
PIN_LS3: 5
PIN_US_TRIG: 6  # Ultra Sonic Trigger Pin
PIN_US_ECHO: 12  # Ultra Sonic Echo Pin

# Motor Usage: motor_[i].motor_go(False,"Full",200,0.0005,False,0.05)
#                      Clockwise, StepSize, StepCount, StepDelay, Verbose, InitDelay
motor_1 = None
motor_2 = None
motor_3 = None
motor_4 = None
motor_5 = None


########
# Code #
########

class TaskManager:
	def task_line_sensor_1(self):
# TODO


def init():
	GPIO.setup(PIN_M1_EN, GPIO.OUT)
	GPIO.setup(PIN_M2_EN, GPIO.OUT)
	GPIO.setup(PIN_M3_EN, GPIO.OUT)
	GPIO.setup(PIN_M4_EN, GPIO.OUT)
	GPIO.setup(PIN_M5_EN, GPIO.OUT)

	global motor_1
	motor_1: A4988Nema = RpiMotorLib.A4988Nema(PIN_M1_DIR, PIN_M1_STEP, (21, 21, 21), "DRV8825")
	global motor_2
	motor_2: A4988Nema = RpiMotorLib.A4988Nema(PIN_M2_DIR, PIN_M2_STEP, (21, 21, 21), "DRV8825")
	global motor_3
	motor_3: A4988Nema = RpiMotorLib.A4988Nema(PIN_M3_DIR, PIN_M3_STEP, (21, 21, 21), "DRV8825")
	global motor_4
	motor_4: A4988Nema = RpiMotorLib.A4988Nema(PIN_M4_DIR, PIN_M4_STEP, (21, 21, 21), "DRV8825")
	global motor_5
	motor_5: A4988Nema = RpiMotorLib.A4988Nema(PIN_M5_DIR, PIN_M5_STEP, (21, 21, 21), "DRV8825")


def end_sequence():
	GPIO.cleanup()  # clear GPIO allocations after run


def main():
	init()
	# TODO
	end_sequence()


if __name__ == "__main__":
	main()
