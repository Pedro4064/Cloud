import json
import time
import datetime
import requests
import RPi.GPIO as GPIO

#Set up the GPIO pins
White  = 22
Yellow = 16
Blue1  = 18 #Blue upper part
Blue2  = 32 #Blue lower part

GPIO.setmode(GPIO.BOARD)

GPIO.setup(White,  GPIO.OUT)
GPIO.setup(Yellow, GPIO.OUT)
GPIO.setup(Blue1,  GPIO.OUT)
GPIO.setup(Blue2,  GPIO.OUT)


#Get the current datetime and initialize the hour variable
now  = datetime.datetime.now()
hour = 0


while True:

    #make a get request and then open the file
    request = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Bras%C3%ADlia%2C%20Brazil%20%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
    jsonFile = json.loads(request.text)

    #Get the next day's Forecast
    Forecast = jsonFile["query"]["results"]["channel"]["item"]["forecast"][1]["text"]
    mornig   = jsonFile["query"]["results"]["channel"]["item"]["condition"]["text"]

    #update the hour variable
    hour = now.hour



    #Print the Forecast(next day)
    if hour > 9:

        #Set the state of the GPIO pins
        if Forecast == "Partly Cloudy" or Forecast == "Mostly Cloudy" or Forecast == "Cloudy":
            print("White LEDs on")
            #Turn on the LEDs
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
            #Maybe turn the Blue LEDs on and off (To fake Thunderstorms)


        elif Forecast == "Sunny" or Forecast == "Mostly Sunny":
            print("Yellow LEDs are on")
            #Turn on the LEDs
            GPIO.output(White,   GPIO.LOW)
            GPIO.output(Yellow,  GPIO.HIGH)
            GPIO.output(Blue1,   GPIO.LOW)
            GPIO.output(Blue2,   GPIO.LOW)

        elif Forecast == "Rain" or Forecast == "Scattered Showers" or Forecast == "Showers":
            print("Blue LEDs are on")
            #Turn on the LEDs
            GPIO.output(White,   GPIO.LOW)
            GPIO.output(Yellow,  GPIO.LOW)
            GPIO.output(Blue1,   GPIO.HIGH)
            GPIO.output(Blue2,   GPIO.HIGH)


        elif Forecast == "Breezy":
            print("Yellow and White LEDs are on")
            #Turn on the LEDs
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


        print("The forecast is:",Forecast)
        time.sleep(60)


    #Turn all the LEDs off for the night
    if hour < 5:
        GPIO.output(White,  GPIO.LOW)
        GPIO.output(Yellow, GPIO.LOW)
        GPIO.output(Blue1,  GPIO.LOW)
        GPIO.output(Blue2,  GPIO.LOW)

    #Print for the day
    if hour >=5 and hour <= 9:

        if mornig == "Partly Cloudy" or mornig == "Mostly Cloudy" or mornig == "Cloudy":
            print("White LEDs on")
            #Turn on the LEDs
            GPIO.output(White,   GPIO.HIGH)
            GPIO.output(Yellow,  GPIO.LOW)
            GPIO.output(Blue1,   GPIO.LOW)
            GPIO.output(Blue2,   GPIO.LOW)



        elif mornig == "Thunderstorms" or mornig == "Scattered Thunderstorms":
            print("Blue and White LEDs are on")
            #Turn on the LEDs
            GPIO.output(White,   GPIO.HIGH)
            GPIO.output(Yellow,  GPIO.LOW)
            GPIO.output(Blue1,   GPIO.LOW)
            GPIO.output(Blue2,   GPIO.HIGH)
            #Maybe turn the Blue LEDs on and off (To fake Thunderstorms)


        elif mornig == "Sunny" or mornig == "Mostly Sunny":
            print("Yellow LEDs are on")
            #Turn on the LEDs
            GPIO.output(White,   GPIO.LOW)
            GPIO.output(Yellow,  GPIO.HIGH)
            GPIO.output(Blue1,   GPIO.LOW)
            GPIO.output(Blue2,   GPIO.LOW)

        elif mornig == "Rain" or mornig == "Scattered Showers" or mornig == "Showers":
            print("Blue LEDs are on")
            #Turn on the LEDs
            GPIO.output(White,   GPIO.LOW)
            GPIO.output(Yellow,  GPIO.LOW)
            GPIO.output(Blue1,   GPIO.HIGH)
            GPIO.output(Blue2,   GPIO.HIGH)


        elif mornig == "Breezy":
            print("Yellow and White LEDs are on")
            #Turn on the LEDs
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


        print("The mornig is:", mornig)
        time.sleep(60)
