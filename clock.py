from datetime import datetime
from threading import Timer

from drawing import Drawing
from clockobject import ClockObject
from hourobject import HourObject
from minuteobject import MinuteObject
from secondobject import SecondObject
from repeatedtimer import RepeatedTimer


class Clock():

	'''
	Init the clock object.
	Calculate also the start position of the "hours". There will be displayed at the end.
	
	Normally there are 60 kummerling glasses. Under each glass are two leds. 
	
	After the clock the hours leds start. The normal start position is 60 * 2. (Index 0 to 119, at index 120 the hours start)
	'''
	def __init__(self):
		self.programm = None
		self.glasses = 60
		self.ledsPerPerGlass = 1
		self.ledsPerHour = 1
		self.startGlassesPosition = 0
		self.startHourPositions = (self.glasses * self.ledsPerPerGlass) 
		self.leds = (self.glasses * self.ledsPerPerGlass) + (self.ledsPerHour * 12)
		
		self.drawing = Drawing(self.leds)
		self.counter = 0

	'''
	Add second objects depending on the current time. 
	'''
	def addSecondObjects(self, currentTime, plan):
		for index in range(0, self.ledsPerPerGlass):
			plan[(currentTime.second * self.ledsPerPerGlass) + index] = SecondObject()

	'''
	Add minute objects depending on the current time. 
	'''
	def addtMinuteObjects(self, currentTime, plan):
		for minute in range(0, currentTime.minute):
			for index in range(0, self.ledsPerPerGlass):
				plan[(minute * self.ledsPerPerGlass) + index] = MinuteObject()

	'''
	Add hour objects depending on the current time. 
	'''
	def addHourObjects(self, currentTime, plan):
		for index in range(0, self.ledsPerHour):
			if currentTime.hour >= 12:
				plan[self.startHourPositions + ((currentTime.hour - 12) * self.ledsPerHour) + index] = HourObject()
			else:
				plan[self.startHourPositions + (currentTime.hour * self.ledsPerHour) + index] = HourObject()

	'''
	Reset the clock plan. 
	'''
	def resetPlan(self, plan):
		for index in range(self.leds):
			plan[index] = None

	'''
	Get a new plan
	'''
	def getNewPlan(self):
		plan = list()
		for _ in range(self.leds):
			plan.append(None)
		return plan

	'''
	Displayed the normal time. 
	
	After that it start itself in a thread after 0.75 seconds. 
	'''
	def displayTime(self, plan):
		plan = self.getNewPlan()
		
		currentTime = datetime.now()
		
		self.resetPlan(plan)
		self.resetPlan(plan)
		self.addSecondObjects(currentTime, plan)
		#self.addtMinuteObjects(currentTime, plan)
		#self.addHourObjects(currentTime, plan)
		self.drawing.clockPlan(plan)

	'''
	Displayed the initialization of the clock.
	'''
	def displayInitialization(self, plan):
		
		for index in range(0, self.ledsPerPerGlass):
			plan[(self.counter * self.ledsPerPerGlass) + index] = SecondObject()
		
		self.drawing.clockPlan(plan)
		self.counter += 1
		
		if(self.counter >= self.glasses):
			self.counter = 0
			self.runMode(1)

	'''
	Run rainbow effect
	'''
	def displayRainbow(self, plan):
		
		for index in range(0, self.ledsPerPerGlass):
			clockObject = ClockObject()
			plan[(self.counter * self.ledsPerPerGlass) + index] = clockObject
		
		self.drawing.clockPlan(plan)
		self.counter += 1
		
		if(self.counter >= self.glasses):
			self.counter = 0
			self.runMode(99)

	'''
	Start a timer. If any other timer exist stop it first. 
	'''
	def startTimer(self, time, function):
		if(self.programm != None):
			self.programm.stop()
		self.programm = RepeatedTimer(time, function, self.getNewPlan())

	'''
	Run mode
	'''
	def runMode(self, mode):
		if(mode == 0):
			self.startTimer(0.10, self.displayInitialization)
		elif(mode == 1):
			self.startTimer(0.10, self.displayRainbow)
		elif(mode == 99):
			self.startTimer(0.25, self.displayTime)
