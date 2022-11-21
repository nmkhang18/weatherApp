import urllib.request
import json
from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        city = str(request.POST['city'])
        city = city.replace(' ', '%20')
        try:
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city + '&units=metric&appid=71f55e70b92e139ce1ab496008e0b51a').read()
            list_of_data = json.loads(source)
        except:
            list_of_data = 0
        if list_of_data == 0:
            data = {
                "error": "Please insert valid city!"
            }
        else:
            data = {
                "name": str(list_of_data['name']),
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
