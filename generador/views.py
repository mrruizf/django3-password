from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generador/home.html')

def acerca(request):
    return render(request,'generador/acerca.html')


def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Mayusculas'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numeros'):
        characters.extend(list('0123456789'))
    if request.GET.get('Car_especial'):
        characters.extend(list('!#$%&/()=?¿¡°|@'))
    leng=int(request.GET.get('length'))
    thepassword=''
    for i in range(leng):
        thepassword+=random.choice(characters)
    return render(request,'generador/password.html',{'password':thepassword})


