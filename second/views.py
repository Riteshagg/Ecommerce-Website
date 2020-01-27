from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'second/index.html')

def about(request):
    email = request.POST.get('hello','not')
    check = request.POST.get('check','off')
    counters = request.POST.get('counter','off')
    hello = ""
    if check == "on":
         punc = '''[].',";'''
         for char in email:
             if char not in punc:
                hello = hello + char
    elif(counters =="on"):
        hello = len(email)
        # count = 0
        # for char in email:
        #     count +=1
        #     hello = count            
    else:
        hello = email            
    params = {'email':hello}
    return render(request,'second/aboutform.html',params)
