from clockobject import ClockObject


class HourObject(ClockObject):

	def __init__(self, rgbColor):
		ClockObject.__init__(self)
		if rgbColor == None:
			self.color = [0, 255, 0]
		else:
			self.color = rgbColor
