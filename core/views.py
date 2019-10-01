from django.shortcuts import render
import requests
from .forms import WheatherForm
from django.http import JsonResponse


def home(request):
    """latitude = 89
    longitude = 12
    selected = []"""

    if request.method == 'POST':

        form = WheatherForm(request.POST)

        if form.is_valid():
            latitude = form.cleaned_data['latitud']
            longitude = form.cleaned_data['longitud']
            selected = form.cleaned_data['services']

            URL1 = "http://127.0.0.1:5000/accuweather"
            URL2 = "http://127.0.0.1:5000/noaa?latlon="
            URL3 = "http://127.0.0.1:5000/weatherdotcom"

            PARAMS1 = {'latitude': latitude, 'longitude': longitude}
            r1 = requests.get(url=URL1, params=PARAMS1)
            data1 = r1.json()
            result1 = data1['simpleforecast']['forecastday'][0]['current']['fahrenheit']

            latitude = str(latitude)
            longitude = str(longitude)
            URL2si = URL2 + latitude + ',' + longitude
            r2 = requests.get(url=URL2si)
            data2 = r2.json()
            result2 = data2['today']['current']['fahrenheit']

            longitudefloat = float(longitude)
            latitudefloat = float(latitude)
            PARAMS3 = {"lat": latitudefloat, "lon": longitudefloat}
            r3 = requests.post(url=URL3, json=PARAMS3)
            data3 = r3.json()
            result3 = data3['query']['results']['channel']['condition']['temp']

            if 'Accuweather' in selected:
                selected[selected.index('Accuweather')] = result1
            if 'Weather.com' in selected:
                selected[selected.index('Weather.com')] = result3
            if 'NOAA' in selected:
                selected[selected.index('NOAA')] = result2

            suma = 0
            for i in range(len(selected)):
                sumando = int(selected[i])
                suma = sumando + suma
            result = suma / len(selected)

            data = {'average current temperature in Farenheit': result}

            return JsonResponse(data)

    else:
        form = WheatherForm()

        return render(request, 'home.html', {'form': form})
