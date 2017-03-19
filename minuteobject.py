from clockobject import ClockObject

'''
The minute class.
'''
class MinuteObject(ClockObject):

	def __init__(self, rgbColor):
		ClockObject.__init__(self)
		if rgbColor == None:
			self.color = [255, 0, 0]
		else:
			self.color = rgbColor
		
