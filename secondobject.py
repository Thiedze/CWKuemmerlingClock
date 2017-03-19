from clockobject import ClockObject

'''
The second class.
'''
class SecondObject(ClockObject):

	def __init__(self, rgbColor):
		ClockObject.__init__(self)
		if rgbColor == None:
			self.color = [0, 0, 255]
		else:
			self.color = rgbColor
