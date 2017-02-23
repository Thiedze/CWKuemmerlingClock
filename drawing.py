from neopixel import *

class Drawing():
	'''
	The drawing class.
	'''
	
	def __init__(self, leds):
		self.leds = leds
		self.stripe = Adafruit_NeoPixel(leds, 18, 800000, 5, False, 255)
		self.stripe.begin()
		self.emptyPlaceColor = [0, 0, 0]

	def clockPlan(self, plan):
		'''
		Draw the clock plan. (Send to the stripe)		
		:param plan: The clock plan to draw.
		'''
		for led in range(self.leds):
			if(plan[led] == None):
				self.stripe.setPixelColorRGB(led, self.emptyPlaceColor[0], self.emptyPlaceColor[1], self.emptyPlaceColor[2])
			else:
				self.stripe.setPixelColorRGB(led, plan[led].color[0], plan[led].color[1], plan[led].color[2])
		self.stripe.show()
		
