from effect import Effect

from constants import Constants

from clockobject import ClockObject

class AppearEffect(Effect):
	
	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.rounds = 6
		self.counter = 0
		self.steps = 6
		
	def getColorForRounds(self, color):
		if(self.rounds == 6):
			if color[1] + self.steps >= 255:
				return [0, 255, 0]
			else:
				color[1] = color[1] + self.steps
				return color
		elif(self.rounds == 4):
			if color[0] + self.steps >= 255:
				return [255, 0, 0]
			else:
				color[0] = color[0] + self.steps
				return color
		elif(self.rounds == 2):
			if color[2] + self.steps >= 255:
				return [0, 0, 255]
			else:
				color[2] = color[2] + self.steps
				return color
		else:
			if(self.rounds == 5):
				if color[1] - self.steps < 0:
					return [0, 0, 0]
				else:
					color[1] = color[1] - self.steps
					return color
			elif(self.rounds == 3):
				if color[0] - self.steps < 0:
					return [0, 0, 0]
				else:
					color[0] = color[0] - self.steps
					return color
			elif(self.rounds == 1):
				if color[2] - self.steps < 0:
					return [0, 0, 0]
				else:
					color[2] = color[2] - self.steps
					return color

	def checkState(self):
		if(self.rounds <= 1 and self.counter >= (Constants.glasses * Constants.ledsPerGlass) + self.steps * 2):
			self.nextModeCallback()
			
		if(self.counter >= (Constants.glasses * Constants.ledsPerGlass) + self.steps * 2):
			self.counter = 0
			self.rounds -= 1

	'''
	Show wait effect
	'''
	def show(self, plan):
		self.counter += 2
		
		clockObject = ClockObject()
		clockObject.color = [0,0,0]
		
		for index in range(0, self.counter):
			planObject = plan[index]
			if planObject == None:
				plan[index] = clockObject
			else:
				planObject.color = self.getColorForRounds(planObject.color)
		
		self.drawing.clockPlan(plan)
		self.checkState()
