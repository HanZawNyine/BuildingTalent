from logging import fatal
import time
import pyrebase
import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)  # gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)
gpio.setup(15, gpio.OUT)

firebaseConfig = {
  "apiKey": "AIzaSyD_tVzlPM3WH57oB7v_jB6iM-etO5Q9PV8",
  "authDomain": "ledblink-b7d21.firebaseapp.com",
  "databaseURL": "https://ledblink-b7d21-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "ledblink-b7d21",
  "storageBucket": "ledblink-b7d21.appspot.com",
  "messagingSenderId": "142321598197",
  "appId": "1:142321598197:web:e892f88c5e5ef9af84cfbc",
  "measurementId": "G-DBY85Y9D7H"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

while True:  
  led =db.child("blink").get()
  #print(led.val())
  global switchss
  for led in led.each():
    switchss = led.val()
  print(switchss)
  if switchss == 0:
    gpio.output(14, True)
    gpio.output(15, True)
  elif switchss == 1:
    gpio.output(14, False)
    gpio.output(15, False)
  time.sleep(3)



