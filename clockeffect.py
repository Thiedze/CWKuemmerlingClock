from effect import Effect

from datetime import datetime

from constants import Constants

from hourobject import HourObject
from minuteobject import MinuteObject
from secondobject import SecondObject

class ClockEffect(Effect):

	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)

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
			plan[(currentTime.second * Constants.ledsPerGlass) + index] = SecondObject()

	'''
	Add minute objects depending on the current time. 
	'''
	def addtMinuteObjects(self, currentTime, plan):
		for minute in range(0, currentTime.minute):
			for index in range(0, Constants.ledsPerGlass):
				plan[(minute * Constants.ledsPerGlass) + index] = MinuteObject()

	'''
	Add hour objects depending on the current time. 
	'''
	def addHourObjects(self, currentTime, plan):
		for index in range(0, Constants.ledsPerHour):
			if currentTime.hour >= 12:
				plan[Constants.startHourPositions + ((currentTime.hour - 12) * Constants.ledsPerHour) + index] = HourObject()
			else:
				plan[Constants.startHourPositions + (currentTime.hour * Constants.ledsPerHour) + index] = HourObject()

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
