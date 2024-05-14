## pip install requests
## pip install win10toast

import requests
from win10toast import ToastNotifier
import time

text = ""

def update():
  # url = 'https://coronavirus-19-api.herokuapp.com/all'
  url = 'https://disease.sh/v3/covid-19/historical/mg?lastdays=all'
  r = requests.get(url)
  data = r.json()
  # text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

  last_date = list(data["timeline"]["cases"])[-1]
  text = f'{last_date} : \n\tConfirmed Cases : {data["timeline"]["cases"][last_date]} \n\tDeaths : {data["timeline"]["deaths"][last_date]} \n\tRecovered : {data["timeline"]["recovered"][last_date]}'
  # print(text)

  while True:
    toast = ToastNotifier()
    toast.show_toast("Covid-19 Updates", text, duration=20)
    time.sleep(30)

update()

