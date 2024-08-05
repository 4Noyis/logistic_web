from django.shortcuts import render
from order import map

def IndexView(request):
    return render(request,'index.html')

def LoginView(request):
    return render(request,'login.html')

def MapView(request):
    context = {
        'list':[{'lat':map.lat,
        'lng':map.lng}]
    }
    return render(request,'map_test.html',context=context)