import umqtt_robust2 as mqtt
from machine import Pin, PWM
from gpio_lcd import GpioLcd
from time import sleep


lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
                              d4_pin=Pin(33), d5_pin=Pin(32),
                              d6_pin=Pin(21), d7_pin=Pin(22),
                              num_lines=4, num_columns=20)
lcd.clear()
lcd.putstr("Spil en sød sang")

BUZZ_PIN = 26
buzzer_pin = Pin(BUZZ_PIN, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)

def buzzer(buzzer_PWM_object, frequency, sound_duration, silence_duration):
     buzzer_PWM_object.duty(512)
     buzzer_PWM_object.freq(frequency)
     sleep(sound_duration)
     buzzer_PWM_object.duty(0)
     sleep(silence_duration)

while True:
    try:
        if mqtt.besked == "a":
            print("Spiller en melodi")
            buzzer(pwm_buzz, 440, 0.2, 0.2)
            lcd.clear()
            lcd.putstr("Spiller tonen a")


            
        mqtt.sync_with_adafruitIO()         
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()