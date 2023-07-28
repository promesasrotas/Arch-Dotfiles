import requests

city = "4012176"
api_key = "b7b864c3dd3669816e2fc168a1ed94e1"
units = "Metric"
unit_key = "C"

def weather():
    req = requests.get ("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units={}".format(city, api_key,units,unit_key))
    try:
        if req.status_code == 200:
            current = req.json()["weather"][0]["description"].capitalize()
            temp = int(float(req.json()["main"]["temp"]))
            if current == 'Broken clouds':
                print ("󰖕 {}, {} °{}".format(current,temp, unit_key))
            elif current == 'Light rain':
                print (" {}, {} °{}".format(current,temp, unit_key))
            elif current == 'Moderate rain':
                print (" {}, {} °{}".format(current,temp, unit_key))
            elif current == 'Scattered clouds':
                print (" {}, {} °{}".format(current,temp, unit_key))
            else:
                print (" {}, {} °{}".format(current,temp, unit_key))
        else:
            print (" 󰼷 ")
    except (ValueError, IOError):
        print (" 󱓤 ")

if __name__ == '__main__':
    try:
        weather()
    except KeyboardInterrupt:
        print ("Try again")