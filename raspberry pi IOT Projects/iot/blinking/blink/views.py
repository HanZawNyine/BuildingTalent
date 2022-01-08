from django.http import request
from django.shortcuts import render
import RPi.GPIO as gpio
# Create your views here.


def index(request):
    return render(request, 'index.html', {'value': "on"})


def on(request):
    pin = request.POST['pin']
   # bb(14,False)
    print(f"pin : {int(pin)}")
    value = request.POST['value']
    print(f'value : {value}')
    if value == 'on':
        value = 'off'
        bb(int(pin), True)
    elif value == 'off':
        value = 'on'
        bb(int(pin), False)
    return render(request, 'index.html', {'value': value, 'pin': pin})


def bb(pin, value):
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.OUT)
    try:
        gpio.output(pin, value)
    except:
        gpio.cleanup()
