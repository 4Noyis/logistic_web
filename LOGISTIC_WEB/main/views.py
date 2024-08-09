from django.shortcuts import render
from order import map

def IndexView(request):
    return render(request,'index.html')

def LoginView(request):
    return render(request,'login.html')

def MapView(request):
    location=map.find_location_place("izmit kozluk mahallesi ege market") #input buraya gelecek
    lat=location[0]
    lng=location[1]
    print(lat)
    context = {
        'map_data':[{'lat':lat,
        'lng':lng}]
    }
    return render(request,'map_test.html',context=context)