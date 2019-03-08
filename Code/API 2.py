import json
import requests
import time



while True:

    #Make the url request
    response = requests.get("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Bras%C3%ADlia%2C%20Brazil%20%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")

    #Turn the respnse to a .json format
    info = json.loads(response.text)

    #Delare the "Path" for the information(on the json file)
    temp     = info['query']["results"]["channel"]["item"]["condition"]
    forecast = info["query"]["results"]["channel"]["item"]["forecast"][1]["text"]

    #Tomorrow = (forecast["text"])
    weather  = (temp["text"])

    #Gets the temperature in ºF
    Tf = float(temp["temp"])
    print(Tf)

    #Transforms it to ºC
    Tc = ((Tf - 32)*5)/9
    print(Tc)

    print(weather)
    print(forecast)


    #Waits 2 Seconds, then it loops again
    time.sleep(2)
