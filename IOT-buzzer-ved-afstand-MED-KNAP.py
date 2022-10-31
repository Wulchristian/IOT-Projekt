from hcsr04 import HCSR04
from time import sleep
from machine import  Pin
from machine import PWM

sensor = HCSR04(trigger_pin=23, echo_pin=18, echo_timeout_us=100000000)
BUZZ_PIN = 25
buzzer = PWM(Pin(BUZZ_PIN, Pin.OUT))
buzzer.duty(1)
ts = Pin(14, Pin.IN)
isTouch = False
buzzeron = False 

while True:
    if ts.value()==1:
        isTouch = not isTouch
        if isTouch == True:
            buzzeron = True
            print('Buzzer on')
        else:
            print('Buzzer off')
            buzzeron = False 
    
    distance = int(sensor.distance_cm())

    print('Distance:', distance, 'cm')    
    if distance <= 100.0 and buzzeron == True:
        buzzer.duty(600)
        buzzer.freq (500)
        
    elif distance <= 200.0 and buzzeron == True:
        buzzer.duty(600)
        buzzer.freq(1000)

    elif distance <= 300.0 and buzzeron == True:
        buzzer.duty(600)
        buzzer.freq(1500)
        
    elif distance <= 400.0 and buzzeron == True:
        buzzer.duty(600)
    #    buzzer.duty (512)
        buzzer.freq(2000)
    else:
        buzzer.duty(0)
        
    
    sleep(0.1)
        
   # else:
        # sluk buzzer kode