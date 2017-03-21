from effect import Effect
from constants import Constants
from clockobject import ClockObject

'''
 The appear effect class
'''
class AppearEffect(Effect):
	
	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.resetState()
	
	'''
	Reset class attributes.
	'''
	def resetState(self):
		self.rounds = 6
		self.counter = 0
		self.steps = 6
		self.maxColorValue = 255
		
	'''
	Get the color index for the specific round. 
		
	4 and 3 : 0
	6 and 5 : 1
	2 and 1 : 2
	'''
	def getColorIndexForRound(self):
		if self.rounds == 6 or self.rounds == 5:
			return 1
		elif self.rounds == 4 or self.rounds == 3:
			return 0
		elif self.rounds == 2 or self.rounds == 1:
			return 2
		
	'''
	Get the new calculated color for the specific round.
	'''
	def getColorForRounds(self, color):
		index = self.getColorIndexForRound()
	
		if self.rounds % 2 == 0:
			if color[index] + self.steps >= self.maxColorValue:
				color[index] = self.maxColorValue
				return color
			else:
				color[index] = color[index] + self.steps
				return color
		else:
			if color[index] - self.steps < 0:
				color[index] = 0
				return color
			else:
				color[index] = color[index] - self.steps
				return color

	'''
	Check the current state. Call nextModeCallback if last round reached and counter is greater glasses * leds per glass.
	'''
	def checkState(self):
		if(self.rounds <= 1 and self.counter >= (Constants.glasses * Constants.ledsPerGlass) + (self.maxColorValue / self.steps)):
			self.resetState()
			self.nextModeCallback()
			
		if(self.counter >=  ((Constants.glasses * Constants.ledsPerGlass) + (self.maxColorValue / self.steps))):
			self.counter = 0
			self.rounds -= 1

	'''
	Show appear effect
	'''
	def show(self, plan):
		self.counter += Constants.ledsPerGlass
		clockObject = ClockObject()
		clockObject.color = [0,0,0]
		
		maxIndex = 0
		if self.counter > (Constants.glasses * Constants.ledsPerGlass):
			maxIndex = Constants.glasses * Constants.ledsPerGlass
		else:
			maxIndex = self.counter
		
		for index in range(0, maxIndex):
			planObject = plan[index]
			if planObject == None:
				plan[index] = clockObject
			else:
				planObject.color = self.getColorForRounds(planObject.color)
		
		self.drawing.clockPlan(plan)
		self.checkState()
