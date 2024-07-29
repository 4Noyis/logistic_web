from django.shortcuts import render

def IndexView(request):
    return render(request,'index.html')

def LoginView(request):
    return render(request,'login.html')