from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):

    low_chars = [chr(i) for i in range(ord('a'), ord('z')+1)]
    up_chars = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    sp_chars = list('!@#$%^&*()')
    nums = [str(i) for i in range(10)]

    length = int(request.GET.get('length',12))
    charset = low_chars

    if request.GET.get('uppercase',False):
        charset.extend(up_chars)
    if request.GET.get('numbers',False):
        charset.extend(nums)
    if request.GET.get('special',False):
        charset.extend(sp_chars)

    thepass = ''.join(random.choice(charset) for _ in range(length))


    return render(request,'generator/password.html',{'password':thepass})

def aboutme(request):
    me = {'name': 'Zerdesht Juan',
        'school': 'Bogazici University',
        'BS': 'Computer Engineering',
        'grade':'first'}
    return render(request, 'generator/aboutme.html',me)
