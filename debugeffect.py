from effect import Effect
from clockobject import ClockObject
from constants import Constants

'''
The debug effect class.
'''
class DebugEffect(Effect):

	def __init__(self, drawing, nextModeCallback):
		Effect.__init__(self, drawing, nextModeCallback)

	'''
	Show debug effect 
	'''
	def show(self, plan):
		clockObject = ClockObject()
		clockObject.color = [50, 50, 50]
		
		for index in range(0, Constants.leds):
			plan[index] = clockObject

		self.drawing.clockPlan(plan)
