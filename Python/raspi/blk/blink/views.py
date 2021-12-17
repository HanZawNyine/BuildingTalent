from django.shortcuts import render
import pyrebase

# Create your views here.


def index(request):
    return render(request, 'index.html', {'value': "On"})


def switch(request):
    value = request.POST['value']
    if value == "On":
        value = "Off"
        fire(0)
        #print(f'LED Switch : {ledSwitch}')
    else:
        value = "On"
        fire(1)
    return render(request, 'index.html', {'value': value})


def fire(value:int):
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
    db.child('blink').update({"LED": value})
