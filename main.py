import tkinter as tk
import requests
import time

city ='london' 
api ="openweathermap.org/data/2.5/weather?q=" + city +"&appid=976baac1ecd42c2b27a7f32340d285d8"
json_data= requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp'] - 273.15)
min_temp = int(json_data['main']['temp_min'] - 273.15)
max_temp = int(json_data['main']['temp_max'] - 273.15)
pressure= json_data['main']['pressure']
humidity= json_data['main']['humidity']
wind = json_data['wind']['speed']
sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))
        
final_info = condition +"\n" + str(temp) + "C"
final_data = "\n" + "Max Temp:" + str(max_temp) +"\n" + "Min Temp:" + str(min_temp) + "\n" + "Pressure:" + str(pressure) +"\n" + "Humidity:" + str(humidity) +"\n" +"Wind Speed:" + str(wind) + "\n" +"Sunrise:" + str(sunrise) +"\n"+"Sunset:" + str(sunset)
print('result' + final_data)
