from effect import Effect
from clockobject import ClockObject
from constants import Constants

'''
The running light effect.
'''
class RunningLightEfect(Effect):
	
	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.resetState()
		
	'''
	Rest the class attributes.
	'''
	def resetState(self):
		self.counter = 0
		self.state = 0
		
	'''
	Get the color for the current state.
	'''
	def getColorForState(self):
		if(self.state == 0):
			return [0, 255, 0]
		elif(self.state == 1):
			return [255, 0, 0]
		elif(self.state == 2):
			return [0, 0, 255]
			
	'''
	Check the state. nextModeCallback if state equals two and counter is greater glasses.
	'''
	def checkState(self):
		if(self.state == 0 and self.counter >= Constants.glasses):
			self.counter = 0
			self.state += 1
		elif(self.state == 1 and self.counter >= Constants.glasses):
			self.counter = 0
			self.state += 1
		elif(self.state == 2 and self.counter >= Constants.glasses):
			self.resetState()
			self.nextModeCallback()

	'''
	Show running light
	'''
	def show(self, plan):
		clockObject = ClockObject()
		clockObject.color = self.getColorForState()
		
		for index in range(0, Constants.ledsPerGlass):
			plan[(self.counter * Constants.ledsPerGlass) + index] = clockObject
		
		self.drawing.clockPlan(plan)
		self.counter += 1
		self.checkState()
