from effect import Effect
from clockobject import ClockObject

from constants import Constants

class RainbowEffect(Effect):
		
	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)
		self.rgbMaxValue = 255
		self.resetState()
		
	def resetState(self):
		self.counter = 0
	
	'''
	Get the color for the position
	'''
	def getRainbowColorForPosition(self, position):
		green = 0
		red = 0
		blue = 0

		tempPosition =  position / self.rgbMaxValue
		if tempPosition == 0:
			green = position % self.rgbMaxValue
			red = (self.rgbMaxValue - 1) - position % self.rgbMaxValue
			blue = 0
		elif tempPosition == 1:
			green = (self.rgbMaxValue - 1) - position % self.rgbMaxValue
			red = 0
			blue = position % self.rgbMaxValue
		elif tempPosition == 2:
			green = 0
			red = position % self.rgbMaxValue
			blue = (self.rgbMaxValue - 1) - position % self.rgbMaxValue

		return [green, red, blue]

	'''
	Show rainbow effect
	'''
	def show(self, plan):
		clockObject = ClockObject()
		if(self.counter == 0):
			clockObject.color = self.getRainbowColorForPosition(0)
		else:
			clockObject.color = self.getRainbowColorForPosition(((self.counter * (self.rgbMaxValue * 3) / Constants.glasses) % (self.rgbMaxValue * 3)) )
		
		for index in range(0, Constants.ledsPerGlass):
			plan[(self.counter * Constants.ledsPerGlass) + index] = clockObject

		self.drawing.clockPlan(plan)
		self.counter += 1
		
		if(self.counter >= Constants.glasses):
			self.resetState()
			self.nextModeCallback()
