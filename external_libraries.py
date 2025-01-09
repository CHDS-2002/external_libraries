import os
import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.system('COLOR B')

url = "http://api.openweathermap.org/data/2.5/minute/weatherforecast/minute/weatherforecast/minute/weatherforecast.json?lat=56.13,56.08,50.79&lon=30.61,29.25,52.66&hour=18:00-19:00&minutely:
response = requests.get(url)
json_response = response.json()

print(json.dumps(json_response, indent=4))

df = pd.read_csv("file.csv")
mean_age = df["age"].mean()

print(mean_age)

x = np.arange(0, 20)
y = x ** 2

plt.plot(x, y, label="Quadratic Function")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Simple Plotting Example")
plt.legend(["Blue"], loc="upper left")
plt.grid(True)
plt.show()

try:
    os.system('PAUSE')
except:
    os.system('CLS')