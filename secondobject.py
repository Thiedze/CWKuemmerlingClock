from clockobject import ClockObject


class SecondObject(ClockObject):

	def __init__(self):
		ClockObject.__init__(self)
		self.color = [0, 0, 50]
