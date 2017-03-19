from effect import Effect
from constants import Constants
from clockobject import ClockObject

'''
The wait effect class.
'''
class WaitEffect(Effect):
	
	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.resetState()
	
	'''
	Reset the class attributes.
	'''
	def resetState(self):
		self.rounds = 6
		self.counter = 0

	'''
	Get the color for the current round. 
	'''
	def getColorForRounds(self):
		if(self.rounds == 6):
			return [0, 255, 0]
		elif(self.rounds == 4):
			return [255, 0, 0]
		elif(self.rounds == 2):
			return [0, 0, 255]
		else:
			return [0,0,0]

	'''
	Check the state. nextModeCallback if the rounds less than 1 and counter is greater glasses.
	'''
	def checkState(self):
		if(self.rounds <= 1 and self.counter >= Constants.glasses):
			self.resetState()
			self.nextModeCallback()
		
		if(self.counter >= Constants.glasses):
			self.counter = 0
			self.rounds -= 1

	'''
	Show wait effect
	'''
	def show(self, plan):
		clockObject = ClockObject()
		clockObject.color = self.getColorForRounds()
		
		for index in range(0, Constants.ledsPerGlass):
			plan[(self.counter * Constants.ledsPerGlass) + index] = clockObject
		
		self.drawing.clockPlan(plan)
		self.counter += 1
		self.checkState()
