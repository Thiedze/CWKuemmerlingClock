from effect import Effect
from constants import Constants
from clockobject import ClockObject
import random

'''
The cycle effect class.
'''
class CycleEffect(Effect):

	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.resetState()
	
	'''
	Reset the class attributes.
	'''
	def resetState(self):
		self.leftDirectionColor = [0,255,0]
		self.rightDirectionColor = [255,0,0]
		self.rounds = 10
		self.isPlanInit = False
		self.counter = -1

	'''
	Check the state. Call nextModeCallback if last round reached and counter is greater glasses * leds per glass.
	
	If the next round reached set a random color to the left and right cycle. 
	'''
	def checkState(self, plan):
		if self.rounds <= 1 and self.counter >= (Constants.glasses * Constants.ledsPerGlass):
			self.drawing.clockPlan(self.getEmptyPlan())
			self.resetState()
			self.nextModeCallback()

		if self.counter >=  Constants.glasses * Constants.ledsPerGlass:
			self.leftDirectionColor = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
			self.rightDirectionColor = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
			self.changeDirection(plan)
			self.counter = 0
			self.rounds -= 1

	def changeDirection(self, plan):
		for led in range(0, Constants.glasses * Constants.ledsPerGlass):
			clockObject = plan[led]
			if clockObject != None:
				if clockObject.direction == 1:
					clockObject.direction = 0
					clockObject.pos = clockObject.pos - 3
				elif clockObject.direction == 0:
					clockObject.direction = 1
					clockObject.pos = clockObject.pos + 3
	'''
	Return an emopty plan.
	'''
	def getEmptyPlan(self):
		plan = []
		
		for led in range(0, Constants.leds):
			plan.append(None)
			
		return plan
		
	'''
	Init the plan. This should be called onced at the start of the effect. 
	
	Set the start objects. From this point we only move the objects. 
	'''
	def initPlan(self, plan):
		self.isPlanInit = True
		for led in range(0, Constants.glasses * Constants.ledsPerGlass):
		
			if led % 8 == 0:
				clockObject = ClockObject()
				clockObject.pos = led + 1
				clockObject.color = self.rightDirectionColor
				clockObject.direction = 0
				plan[clockObject.pos] = clockObject		
			
				clockObject = ClockObject()
				clockObject.pos = led
				clockObject.color = self.leftDirectionColor
				clockObject.direction = 1
				plan[clockObject.pos] = clockObject
		
	'''
	Show cylce effect
	'''
	def show(self, plan):
		self.counter += 3
		
		if self.isPlanInit == False :
			self.initPlan(plan)
		
		for led in range(0, Constants.glasses * Constants.ledsPerGlass):
			clockObject = plan[led]
			
			if clockObject != None:
				if clockObject.direction == 0:
					clockObject.color = self.rightDirectionColor
					if self.counter % 2 == 0:
						clockObject.pos = clockObject.pos + 1
					else:
						clockObject.pos = clockObject.pos + 3
					if clockObject.pos > Constants.glasses * Constants.ledsPerGlass:
						clockObject.pos = clockObject.pos - Constants.glasses * Constants.ledsPerGlass
				elif clockObject.direction == 1:
					clockObject.color = self.leftDirectionColor
					if self.counter % 2 == 0:
						clockObject.pos = clockObject.pos - 1
					else:
						clockObject.pos = clockObject.pos - 3
					if clockObject.pos < 0:
						clockObject.pos = clockObject.pos + Constants.glasses * Constants.ledsPerGlass
					
		tempPlan = self.getEmptyPlan()
		for led in range(0, Constants.glasses * Constants.ledsPerGlass):
			if plan[led] != None:
				tempPlan[plan[led].pos] = plan[led]

		plan = tempPlan
			
		self.drawing.clockPlan(plan)
		self.checkState(plan)