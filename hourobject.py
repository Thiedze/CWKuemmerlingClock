from clockobject import ClockObject

class HourObject(ClockObject):

	def __init__(self):
		ClockObject.__init__(self)
		self.color = [0,255,0]
