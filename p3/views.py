from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Welcome To The Project</marquee>")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"abc",'name':"Ravi"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':-100,'b':-5})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def greater(request, ab):
    Ab = list(map(int, ab.split(" ")))
    return HttpResponse(f"<h1>Greater num is: {max(Ab)}</h1>")

def vowel(request, s):
    char = 'aeiouAEIOU'
    count = 0
    consonent = 0
    for i in s:
        if i in char:
            count += 1
        else:
            consonent += 1
    return render(request, 'directory/vowel.html', {'string':s, 'vo':count, 'cons':consonent})
    
    