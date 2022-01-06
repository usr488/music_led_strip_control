import RPi.GPIO as GPIO  ## Importieren der GPIO Bibliothek
import subprocess
from time import sleep

# Zaehler-Variable, global
Counter = 0
Pid = 0
GPIO_switch = 24 # GPIO Port where switch is attached

GPIO.setmode(GPIO.BCM) ## Verwende die Nummerierung der PINs (GPIO)
GPIO.setup(GPIO_switch, GPIO.IN)  ## Setze GPIO Pin "GPIO_switch" auf Eingangssignal (Taster)


# Callback-Funktion
def Interrupt(channel):
        global Counter
  
        if Counter == 0:
                #subprocess.call(["do 0!"])
                print("off")
                subprocess.Popen(['curl  API call....'], shell = True)
                #print(process.pid)
                #Pid = process.pid
                Counter += 1
        elif Counter == 1:
                #subprocess.call(["do 1!"])
                print("single")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/visualization.py spectrum'], shell = True)
                #print(process.pid)
                #Pid = process.pid
                Counter += 1
        elif Counter == 2:
                #subprocess.call(["do 2!"])
                print("VU_Meter")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/visualization.py energy'], shell = True)
                Counter += 1 
        elif Counter == 3:
                #subprocess.call(["do 3!"])
                print("SPectrum_Analyzer")
                subprocess.Popen(['sudo killall python3; sudo python3 /home/pi/dancyPi-audio-reactive-led/python/off.py'], shell = True)
                Counter = 0 
        else:
                print("counter error")



# Interrupt-Event hinzufuegen, steigende Flanke
GPIO.add_event_detect(GPIO_switch, GPIO.RISING, callback = Interrupt, bouncetime = 250)  

# Endlosschleife, bis Strg-C gedrueckt wird
try:
        while True:
    # nix Sinnvolles tun
                sleep(1)

except KeyboardInterrupt:
        GPIO.cleanup()
        print ("\nBye")
