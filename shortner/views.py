from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        print(request.POST)
        csrf_middleware_token = request.POST.get('csrfmiddlewaretoken')
        link = request.POST.get('link')
        new_Url = Url(link = link, uuid = csrf_middleware_token[:10])
        new_Url.save()

    return HttpResponse(f"The link is localhost:8000/shortner/{csrf_middleware_token[:10]}")

def go(request, uid):
    get_url = Url.objects.get(uuid=uid)
    return redirect('https://'+get_url.link)
