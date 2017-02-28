from clockobject import ClockObject


class MinuteObject(ClockObject):

	def __init__(self):
		ClockObject.__init__(self)
		self.color = [50, 0, 0]
