from effect import Effect
from constants import Constants
from clockobject import ClockObject
import random
import copy
import math 

'''
The pendulum effect class.
'''
class WaveEffect(Effect):

	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.resetState()
	
	'''
	Reset the class attributes.
	'''
	def resetState(self):
		self.rounds = 60
		self.counter = 0
		self.color = [0,0,0]
		
	'''
	Check the state. If rounds <= 25 call nextModeCallback.
	'''
	def checkState(self):
		if self.rounds <= 1:
			self.resetState()
			self.nextModeCallback()
			return
			
		if self.counter >= (Constants.glasses * Constants.ledsPerGlass):			
			self.rounds -= 1
		
	'''
	Init a new plan.
	'''
	def initPlan(self, plan):	
		self.isPlanInit = True

		for index in range(0, Constants.leds):
			clockObject = ClockObject()
			clockObject.color = [0,0,0]
			plan[index] = clockObject
			
	'''
	Show pendulum effect
	'''
	def show(self, plan):
		self.counter += Constants.ledsPerGlass

		for led in range(0, Constants.leds):
			if plan[led] != None:
				plan[led].color = [0, 0, 0]
		
		direction = 1
		step = 51
		
		for index in range(0, Constants.glasses):
			for led in range(0, Constants.ledsPerGlass):
				clockObject = ClockObject()
				clockObject.color = copy.copy(self.color)
				plan[(index * Constants.ledsPerGlass) + led] = clockObject
				
				self.color[0] = int((math.sin(index) * 127 + 128)/255)
				
			self.color[0] += (step * direction)

		self.drawing.clockPlan(plan)
		self.checkState()