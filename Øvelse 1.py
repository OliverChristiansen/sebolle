import umqtt_robust2 as mqtt
from machine import Pin
# Her kan i placere globale varibaler, og instanser af klasser

led3 = Pin(13, Pin.OUT)

while True:
    try:

#Her tændes og slukkes Led3, ved hjælp af if og elif samt adafruit.
        if mqtt.besked == "led3 tændt":
            led3.on()
        elif mqtt.besked == "led3 slukket":
            led3.off()
        
        if len(mqtt.besked) != 0: 
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO()         
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()