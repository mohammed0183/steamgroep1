
import time

import GPIO as GPIO

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )
print( "servo wave" )

def pulse( pin, delay1, delay2 ):
   # copieer hier je implementatie van de pulse functie
   GPIO.output(pin, GPIO.HIGH)   #lamp gaat aan
   time.sleep(delay1)            #lamp brandt voor een bepaalde tijd
   GPIO.output(pin, GPIO.LOW)    #lamp gaat uit
   time.sleep(delay2)            #lamp brandt uit voor een bepaalde tijd


def servo_pulse( pin_nr, position ):
   """
   Send a servo pulse on the specified gpio pin
   that causes the servo to turn to the specified position, and
   then waits 20 ms.
   The position must be in the range 0 .. 100.
   For this range, the pulse must be in the range 0.5 ms .. 2.5 ms

   Before this function is called,
   the gpio pin must be configured as output.
   """
   # implementeer deze functie
   delay1 = (0.5 + (0.02 * position)) /1000 #0.5 is de pulse lengte in miliseconden. 0.02 is de pauze. 1000/ om seconden te krijgen.
   pulse( pin_nr, delay1, 0.02) #delay 1 geeft aan hoelang hij aan blijft.


servo = 25
GPIO.setup( servo, GPIO.OUT )
while True:
   for i in range( 0, 100, 1 ):
      servo_pulse( servo, i )
   for i in range( 100, 0, -1 ):
      servo_pulse( servo, i )