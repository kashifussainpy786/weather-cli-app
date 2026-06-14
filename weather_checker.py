import json 
import datetime
import requests
class Weather:
	def __init__(self,city_name,timestamp, temp, feels_like, humidity, wind_speed, description):
		self.city_name = city_name
		self.timestamp = timestamp 
		self.temp = temp 
		self.feels_like = feels_like
		self.humidity = humidity 
		self.wind_speed = wind_speed
		self.description = description 
	def __str__(self):
		return(f"city_name:{self.city_name}\n"
		f"timestamp:{self.timestamp}\n"
		f"temp:{self.temp}\n"
		f"feels_like:{self.feels_like}\n"
		f"humidity:{self.humidity}\n"
		f"wind_speed:{self.wind_speed}\n"
		f"description:{self.description}\n")
history = []
def save_to_file():
    data = []
    for w in history:
        data.append(w.__dict__)
    with open("weather_update.json","w") as file:
        json.dump(data,file)

def load_from_file():
    try:
        with open("weather_update.json","r") as file:
            data = json.load(file)
            for d in data:
                w = Weather(**d)
                history.append(w)
    except FileNotFoundError:
        print("NO FILE FOUND")
load_from_file()
while True:
    city_name = input("Enter city name: ")
    if city_name == "exit":
        save_to_file()
        break
    api_key = "8bb5bd053678804aee746bd255709016"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    jsn = response.json()
    if jsn["cod"] == 200:
        temp = jsn["main"]["temp"]
        temp = temp - 273.15
        temp = round(temp,2)
        print("temperature is: ",temp) 
        feels_like = jsn["main"]["feels_like"]
        feels_like = feels_like - 273.15
        feels_like = round(feels_like,2)
        print("temperature feels like is: ",feels_like)
        humidity = jsn["main"]["humidity"]
        print("humidity is: ",humidity)
        wind_speed= jsn["wind"]["speed"]
        print("wind speed is: ",wind_speed)
        weather = jsn["weather"][0]["description"]
        print("description is:",weather)
        timestamp = datetime.datetime.now()
        w = Weather(city_name,str(timestamp),temp,feels_like,humidity,wind_speed,weather)
        history.append(w)
    else:
    	print("wrong choice...")