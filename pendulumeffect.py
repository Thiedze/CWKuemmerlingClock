from effect import Effect
from constants import Constants
from clockobject import ClockObject
import random

'''
The pendulum effect class.
'''
class PendulumEffect(Effect):

	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.resetState()
	
	'''
	Reset the class attributes.
	'''
	def resetState(self):
		self.color = [random.randint(0,100), random.randint(0,255), random.randint(100,255)]
		self.rounds = 60
		self.isPlanInit = False
		self.counter = 0
		self.direction = 1
		self.activeLeds = 2
		self.addLedsPerRound = 6
		
	'''
	Check the state. If rounds <= 25 call nextModeCallback.
	'''
	def checkState(self, plan):
		if self.rounds <= 1:
			self.resetState()
			self.nextModeCallback()
			return
			
		if (self.counter + self.activeLeds) >= (Constants.glasses * Constants.ledsPerGlass) or self.counter <= 0:			
			self.changeDirection(plan)
			self.rounds -= 1

	'''
	Change the direction and add ledsPerGlass to the count of active leds.
	'''
	def changeDirection(self, plan):
		if self.direction == 1:
			self.direction = -1
		elif self.direction == -1:
			self.direction = 1
		
		self.activeLeds += Constants.ledsPerGlass
		self.counter += (self.direction * Constants.ledsPerGlass)
		
	'''
	Init a new plan.
	'''
	def initPlan(self, plan):	
		self.isPlanInit = True

		for index in range(0, Constants.leds):
			clockObject = ClockObject()
			clockObject.color = [0,0,0]
			plan[index] = clockObject
			
		for index in range(0, Constants.ledsPerGlass):
			plan[index].color = self.color
			
	'''
	Get a new plan
	'''
	def getEmptyPlan(self):
		plan = list()
		for _ in range(Constants.leds):
			plan.append(None)
		return plan
			
	'''
	Show pendulum effect
	'''
	def show(self, plan):
		self.counter += (self.direction * Constants.ledsPerGlass)
		
		if self.isPlanInit == False :
			self.initPlan(plan)
		
		for led in range(0, Constants.leds):
			if plan[led] != None:
				plan[led].color = [0, 0, 0]
		
		for led in range(self.counter, self.counter + self.activeLeds):
			if plan[led] != None:
				plan[led].color = self.color

		self.drawing.clockPlan(plan)
		self.checkState(plan)