
'''
The effect class
'''
class Effect():

	'''
	@param glasses glasses count
	@param ledsPerGlass leds per glass
	@param drawing draw the plan to the stripe
	@param nextModeCallback calls the next mode
	'''
	def __init__(self, drawing, nextModeCallback):
		self.drawing = drawing
		self.nextModeCallback = nextModeCallback
