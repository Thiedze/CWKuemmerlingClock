from threading import Timer
from repeatedtimer import RepeatedTimer

from drawing import Drawing
from constants import Constants

from rainboweffect import RainbowEffect
from runninglighteffect import RunningLightEfect
from waiteffect import WaitEffect
from clockeffect import ClockEffect

class Clock():

	'''
	Init the clock object.
	Calculate also the start position of the "hours". There will be displayed at the end.
	
	Normally there are 60 kummerling glasses. Under each glass are two leds. 
	
	After the clock the hours leds start. The normal start position is 60 * 2. (Index 0 to 119, at index 120 the hours start)
	'''
	def __init__(self):
		self.programm = None
		
		self.drawing = Drawing()
		self.rainbowEffect = RainbowEffect(self.drawing, self.nextMode)
		self.runningLightEffect = RunningLightEfect(self.drawing, self.nextMode)
		self.waitEffect = WaitEffect(self.drawing, self.nextMode)
		self.clockEffect = ClockEffect(self.drawing, self.nextMode)
		
		self.mode = 3

	def clear(self):
		self.drawing.clear()

	def setColorSeconds(self, rgbColor):
		self.clockEffect.setColorSeconds(rgbColor)

	def setColorMinutes(self, rgbColor):
		self.clockEffect.setColorMinutes(rgbColor)

	def setColorHours(self, rgbColor):
		self.clockEffect.setColorHours(rgbColor)

	def setMode(self, mode):
		self.mode = mode
		self.nextMode()

	'''
	Get a new plan
	'''
	def getNewPlan(self):
		plan = list()
		for _ in range(Constants.leds):
			plan.append(None)
		return plan

	'''
	Start a timer. If any other timer exist stop it first. 
	'''
	def startTimer(self, time, function):
		if(self.programm != None):
			self.programm.stop()
		self.programm = RepeatedTimer(time, function, self.getNewPlan())

	'''
	Run mode
	'''
	def nextMode(self):
		if(self.mode == 0):
			self.startTimer(0.02, self.runningLightEffect.show)
		elif(self.mode == 1):
			self.startTimer(0.01, self.waitEffect.show)
		elif(self.mode == 2):
			self.startTimer(0.10, self.rainbowEffect.show)
		elif(self.mode == 3):
			self.startTimer(0.25, self.clockEffect.show)
		self.mode += 1
