import os
import requests
import sys
import json
import time

def main():
    os.system('cls')
print("welcome to covid deaths tool")
print("press 1 to see the number on death")
print("press 2 to leave the program")

CovidTool = input(": ")

if CovidTool == "1":
    c = requests.get("https://api.covid19api.com/summary")
data = json.loads(c.text)
covid = data['Global']['TotalDeaths']
print(f'covid-19 has taken {covid} lives around globally.')
time.sleep(10)
