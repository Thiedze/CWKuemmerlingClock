import time
from datetime import datetime
from secondobject import SecondObject
from minuteobject import MinuteObject
from hourobject import HourObject
from drawing import Drawing

glasses = 60
ledsPerPerGlass = 3
ledsPerHour = 4
startGlassesPosition = 0
startHourPositions = (glasses * ledsPerPerGlass) 
leds = (glasses * ledsPerPerGlass) + (ledsPerHour * 12)

drawing = Drawing(leds)
plan = list()

while True:
	plan = list()
	for _ in range(leds):
		plan.append(None)

	currentTime = datetime.now()
	
	for minute in range(0, currentTime.minute):
		for index in range(0, ledsPerPerGlass):
			plan[(minute * ledsPerPerGlass) + index] = MinuteObject()
	
	for index in range(0, ledsPerPerGlass):
		plan[(currentTime.second * ledsPerPerGlass) + index] = SecondObject()
		
	for index in range(0, ledsPerHour):
		if currentTime.hour >= 12:
			plan[startHourPositions + ((currentTime.hour - 12)  * ledsPerHour) + index] = HourObject()
		else:
			plan[startHourPositions + (currentTime.hour  * ledsPerHour) + index] = HourObject()

	drawing.clockPlan(plan)
	time.sleep(0.5)
	
