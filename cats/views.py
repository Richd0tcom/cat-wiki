from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from json import dumps

# Create your views here.

def catApi():
    return requests.get('https://api.thecatapi.com/v1/breeds').json()
    
res = catApi()

def getCats(request):
    if request.method == 'POST':
        
        catbreed = request.POST.get('catsearch')
        catid = request.POST.get('catid')
        
        
        return HttpResponseRedirect(f'/breeds/{catid}')

    data = dumps(res)
    return render(request, 'cats/main.html', {'cats': data})

def topten(request):
    return render(request, 'cats/topten.html')

def displayCats(request, breed):
    brd = list(filter(lambda x: x["id"] == str(breed), res))
    if brd:
        
        return render(request, 'cats/breed.html', {"catbreed": brd[0]})
    else:
        return HttpResponse('Cat breed not found')

