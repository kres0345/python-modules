import time

''' Delay23s time for a specific amount of time.
	You are the master on how long it takes
''' 

def delay(float, str="second"):
	''' Delays time for a specific amount of time.
	You are the master on how long it takes

    Command (examples):
            delay.delay(1, "minute") #Sleeps 60 seconds.

            delay.delay(0.5, "second") #Sleeps 30 seconds.

            delay.delay(10) #Sleeps 10 seconds.
        
    Time units:
            `second` Seconds.
            `minute` 60 seconds.
            `hour` 3600 seconds, 60 minutes.
            `day` 24 hours, 86.400 seconds.
            `week` 7 days, 168 hours.
            `megasecond` 1.000.000 seconds.
            `fortnite` 2 weeks.
            `month` 30 days.
            `semester` 180 days.
            `year` 365 days.
            `leapyear` 366 days.
            `gigasecond` 1.000.000.000 seconds.
            `millennium` 1.000 years.

	
'''
	if (str == "second"):
                time.sleep(float)
        elif (str == "minute"):
                time.sleep(float * 60)
        elif (str == "hour"):
                time.sleep(float * 60 * 60)
        elif (str == "day"):
                time.sleep(float * 60 * 60 * 24)
        elif (str == "week"):
                time.sleep(float * 60 * 60 * 24 * 7)
        elif (str == "megasecond"):
                time.sleep(float * 1000000)
        elif (str == "fortnite"):
                time.sleep(float * 60 * 60 * 24 * 14)
        elif (str == "month"):
                time.sleep(float * 60 * 60 * 24 * 30)
        elif (str == "semester"):
                time.sleep(float * 60 * 60 * 24 * 90 * 2)
        elif (str == "year"):
                time.sleep(float * 60 * 60 * 24 * 365)
        elif (str == "leapyear"):
                time.sleep(float * 60 * 60 * 24 * 366)
        elif (str == "gigasecond"):
                time.sleep(float * 1000000000)
        elif (str == "millennium"):
                time.sleep(float * 60 * 60 * 24 * 365 * 1000)
	time.sleep(float)
