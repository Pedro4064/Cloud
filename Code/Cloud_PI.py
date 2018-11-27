import json
import time
import requests
import RPi.GPIO as GPIO

#Set up the GPIO pins
White  = 22
Yellow = 16
Blue1  = 18 #Blue upper part
Blue2  = 32 #Blue lower part


GPIO.setmode(GPIO.BOARD)

while True:

    #make a get request and then open the file
    request = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Bras%C3%ADlia%2C%20Brazil%20%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
    jsonFile = json.loads(request.text)

    #Get the next day's Forecast
    Forecast = jsonFile["query"]["results"]["channel"]["item"]["forecast"][1]["text"]


    if Forecast == "Partly Cloudy" or Forecast == "Mostly Cloudy" or Forecast == "Cloudy":
        print("White LEDs on")
        Turn on the LEDs
        GPIO.output(White,   GPIO.HIGH)
        GPIO.output(Yellow,  GPIO.LOW)
        GPIO.output(Blue1,   GPIO.LOW)
        GPIO.output(Blue2,   GPIO.LOW)



    elif Forecast == "Thunderstorms" or Forecast == "Scattered Thunderstorms":
        print("Blue and White LEDs are on")
        #Turn on the LEDs
        GPIO.output(White,   GPIO.HIGH)
        GPIO.output(Yellow,  GPIO.LOW)
        GPIO.output(Blue1,   GPIO.LOW)
        GPIO.output(Blue2,   GPIO.HIGH)
        Maybe turn the Blue LEDs on and off (To fake Thunderstorms)


    elif Forecast == "Sunny" or Forecast == "Mostly Sunny":
        print("Yellow LEDs are on")
        Turn on the LEDs
        GPIO.output(White,   GPIO.LOW)
        GPIO.output(Yellow,  GPIO.HIGH)
        GPIO.output(Blue1,   GPIO.LOW)
        GPIO.output(Blue2,   GPIO.LOW)

    elif Forecast == "Rain" or Forecast == "Scattered Showers" or Forecast == "Showers":
        print("Blue LEDs are on")
        Turn on the LEDs
        GPIO.output(White,   GPIO.LOW)
        GPIO.output(Yellow,  GPIO.LOW)
        GPIO.output(Blue1,   GPIO.HIGH)
        GPIO.output(Blue2,   GPIO.HIGH)


    elif Forecast == "Breezy":
        print("Yellow and White LEDs are on")
        Turn on the LEDs
        GPIO.output(White,   GPIO.HIGH)
        GPIO.output(Yellow,  GPIO.HIGH)
        GPIO.output(Blue1,   GPIO.LOW)
        GPIO.output(Blue2,   GPIO.LOW)

    else:
        print("Shit, update the code for the current weather")
        #Turn on the LEDs
        GPIO.output(White,   GPIO.LOW)
        GPIO.output(Yellow,  GPIO.LOW)
        GPIO.output(Blue1,   GPIO.LOW)
        GPIO.output(Blue2,   GPIO.LOW)


    print("The forecast is:", Forecast)
    time.sleep(60)

    #print(Forecast)
