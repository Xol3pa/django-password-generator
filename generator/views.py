from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuioplkjhgfdsazxcvbnm')

    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*._')

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword}) 
     
def aboutme(request):
    return render(request, 'generator/aboutme.html')
