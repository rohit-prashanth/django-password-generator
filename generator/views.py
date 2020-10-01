from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')

def password(request):

    thepassword = ''
    Characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVQXYZ')
    numbers = list('123456789')
    specials = list('@#$&*_-()')

    if request.GET.get('uppercase'):
        Characters.extend(uppercase)

    if request.GET.get('numbers'):
        Characters.extend(numbers)

    if request.GET.get('special'):
        Characters.extend(specials)

    length = int(request.GET.get('length',12))

    for x in range(length):
        thepassword += random.choice(Characters)

    return render(request, 'generator/password.html', {"password":thepassword})
