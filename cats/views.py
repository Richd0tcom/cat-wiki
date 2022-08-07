from django.shortcuts import render
from django.http import HttpResponse
import requests
from json import dumps

# Create your views here.

def catApi():
    return requests.get('https://api.thecatapi.com/v1/breeds').json()
    
res = catApi()

def getCats(request):
    data = dumps(res)
    return render(request, 'cats/main.html', {'cats': data})

def displayCats(request, breed):
    brd = list(filter(lambda x: x["name"] == str(breed), res))
    if brd:
        print(list(filter(lambda x: x["name"] == breed, res)))
        return render(request, 'cats/breed.html', {"catbreed": brd[0]})
    else:
        return HttpResponse('Cat breed not found')