from effect import Effect
from datetime import datetime
from constants import Constants

from hourobject import HourObject
from minuteobject import MinuteObject
from secondobject import SecondObject

import random
'''
The clock effect class.
'''
class ClockEffect(Effect):

	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.colorSeconds = [0, 0, 50]
		self.colorMinutes = [50, 0, 0]
		self.colorHours = [0, 255, 0]

	'''
	Set the color of the seconds.
	'''
	def setColorSeconds(self, rgbColor):
		self.colorSeconds = rgbColor

	'''
	Set the color of the minutes.
	'''
	def setColorMinutes(self, rgbColor):
		self.colorMinutes = rgbColor

	'''
	Set the color of the hours.
	'''
	def setColorHours(self, rgbColor):
		self.colorHours = rgbColor

	'''
	Reset the clock plan. 
	'''
	def resetPlan(self, plan):
		for index in range(Constants.leds):
			plan[index] = None

	'''
	Add second objects depending on the current time. 
	'''
	def addSecondObjects(self, currentTime, plan):
			for index in range(0, Constants.ledsPerGlass):
				plan[(currentTime.second * Constants.ledsPerGlass) + index] = SecondObject(self.colorSeconds)

	'''
	Add minute objects depending on the current time. 
	'''
	def addtMinuteObjects(self, currentTime, plan):
		if currentTime.minute % 5 == 0 and currentTime.second == 0:
			self.nextModeCallback(random.randint(0,5), True)
		else:
			for minute in range(0, currentTime.minute):
				for index in range(0, Constants.ledsPerGlass):
					plan[(minute * Constants.ledsPerGlass) + index] = MinuteObject(self.colorMinutes)

	'''
	Add hour objects depending on the current time. 
	'''
	def addHourObjects(self, currentTime, plan):
		for index in range(0, Constants.ledsPerHour):
			if currentTime.hour >= 12:
				plan[Constants.startHourPositions + ((currentTime.hour - 12) * Constants.ledsPerHour) + index] = HourObject(self.colorHours)
			else:
				plan[Constants.startHourPositions + (currentTime.hour * Constants.ledsPerHour) + index] = HourObject(self.colorHours)

	'''
	Displayed the normal time. 
	
	After that it start itself in a thread after 0.75 seconds. 
	'''
	def show(self, plan):
		currentTime = datetime.now()
		
		self.resetPlan(plan)
		self.addtMinuteObjects(currentTime, plan)
		self.addSecondObjects(currentTime, plan)
		self.addHourObjects(currentTime, plan)
		self.drawing.clockPlan(plan)
