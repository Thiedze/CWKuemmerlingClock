from datetime import datetime
from threading import Timer

from drawing import Drawing
from hourobject import HourObject
from minuteobject import MinuteObject
from secondobject import SecondObject


class Clock():
    
    '''
    Init the clock object.
    Calculate also the start position of the "hours". There will be displayed at the end.
    
    Normally there are 60 kummerling glasses. Under each glass are two leds. 
    
    After the clock the hours leds start. The normal start position is 60 * 2. (Index 0 to 119, at index 120 the hours start)
    '''
    def __init__(self):
        self.glasses = 60
        self.ledsPerPerGlass = 2
        self.ledsPerHour = 2
        self.startGlassesPosition = 0
        self.startHourPositions = (self.glasses * self.ledsPerPerGlass) 
        self.leds = (self.glasses * self.ledsPerPerGlass) + (self.ledsPerHour * 12)
        
        self.drawing = Drawing(self.leds)
        self.plan = list()
        for _ in range(self.leds):
            self.plan.append(None)
            
        self.mode = 0

    '''
    Add second objects depending on the current time. 
    '''
    def addSecondObjects(self, currentTime):
        for index in range(0, self.ledsPerPerGlass):
            self.plan[(currentTime.second * self.ledsPerPerGlass) + index] = SecondObject()

    '''
    Add minute objects depending on the current time. 
    '''
    def addtMinuteObjects(self, currentTime):
        for minute in range(0, currentTime.minute):
            for index in range(0, self.ledsPerPerGlass):
                self.plan[(minute * self.ledsPerPerGlass) + index] = MinuteObject()

    '''
    Add hour objects depending on the current time. 
    '''
    def addHourObjects(self, currentTime):
        for index in range(0, self.ledsPerHour):
            if currentTime.hour >= 12:
                self.plan[self.startHourPositions + ((currentTime.hour - 12) * self.ledsPerHour) + index] = HourObject()
            else:
                self.plan[self.startHourPositions + (currentTime.hour * self.ledsPerHour) + index] = HourObject()

    '''
    Reset the clock plan. 
    '''
    def resetPlan(self):
        for index in range(self.leds):
            self.plan[index] = None

    '''
    Displayed the normal time. 
    
    After that it start itself in a thread after 0.75 seconds. 
    '''
    def displayTime(self):
        currentTime = datetime.now()
        self.resetPlan()
        self.addSecondObjects(currentTime)
        self.addtMinuteObjects(currentTime)
        self.addHourObjects(currentTime)
        self.drawing.clockPlan(self.plan)

    '''
    Displayed the initialization of the clock.
    '''
    def displayInitialization(self):
        self.plan[0] = HourObject()

    '''
    Start a timer. If any other timer exist stop it first. 
    '''
    def startTimer(self, time, function):
        if(self.programm != None):
            self.programm.cancel()
        self.programm = Timer(time, function)
        self.programm.start()

    '''
    Run 
    '''
    def run(self):
        if(self.mode == 0):
            self.startTimer(0.50, self.displayInitialization)
        elif(self.mode == 1):
            self.startTimer(0.75, self.displayTime)
            
    
