import umqtt_robust2 as mqtt
from machine import Pin
from time import sleep

pb1 = Pin(4, Pin.IN)
    
while True:
    try:
        if pb1.value() == 0:
            mqtt.web_print("1")
            sleep(5)
            mqtt.web_print("0")

        
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(4) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()