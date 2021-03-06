from threading import Timer
from repeatedtimer import RepeatedTimer

from drawing import Drawing
from constants import Constants

from rainboweffect import RainbowEffect
from runninglighteffect import RunningLightEfect
from waiteffect import WaitEffect
from appeareffect import AppearEffect
from cycleeffect import CycleEffect
from pendulumeffect import PendulumEffect
from waveeffect import WaveEffect
from clockeffect import ClockEffect
from debugeffect import DebugEffect

'''
The clock class. This is the main class to control the effects. 
'''
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
		self.appearEffect = AppearEffect(self.drawing, self.nextMode)
		self.cycleEffect = CycleEffect(self.drawing, self.nextMode)
		self.pendulumEffect = PendulumEffect(self.drawing, self.nextMode)
		self.waveEffect = WaveEffect(self.drawing, self.nextMode)
		self.clockEffect = ClockEffect(self.drawing, self.nextMode)
		self.debugEffect = DebugEffect(self.drawing, self.nextMode)
		
		self.mode = 0
		self.showSingleEffect = False

	'''
	Draw a clear plan.
	'''
	def clear(self):
		self.drawing.clear()

	'''
	Set the color of the seconds.
	'''
	def setColorSeconds(self, rgbColor):
		self.clockEffect.setColorSeconds(rgbColor)

	'''
	Set the color of the minutes.
	'''
	def setColorMinutes(self, rgbColor):
		self.clockEffect.setColorMinutes(rgbColor)

	'''
	Set the color of the hours.
	'''	
	def setColorHours(self, rgbColor):
		self.clockEffect.setColorHours(rgbColor)

	'''
	Set the mode and show it. 
	'''
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
	def nextMode(self, mode = None, showSingleEffect = None):
		if mode != None:
			self.mode = mode
		
		if showSingleEffect != None:
			self.showSingleEffect = showSingleEffect

		#self.startTimer(0.02, self.debugEffect.show)
		
		if(self.mode == 0):
			self.startTimer(0.02, self.runningLightEffect.show)
		elif(self.mode == 1):
			self.startTimer(0.01, self.waitEffect.show)
		elif(self.mode == 2):
			self.startTimer(0.025, self.appearEffect.show)
		elif(self.mode == 3):
			self.startTimer(0.10, self.rainbowEffect.show)
		elif(self.mode == 4):
			self.startTimer(0.05, self.cycleEffect.show)
		elif(self.mode == 5):
			self.startTimer(0.0125, self.pendulumEffect.show)
		else:
			self.startTimer(0.25, self.clockEffect.show)

		'''
		elif(self.mode == 6):
			self.startTimer(0.05, self.waveEffect.show)
		'''
		
		if self.showSingleEffect == False:
			self.mode += 1
		else:
			self.mode = 99
