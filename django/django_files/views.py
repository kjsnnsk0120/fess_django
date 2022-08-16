from django.shortcuts import render
from django.http import HttpResponse
from .models import Data

# Create your views here.

def index(request,id):
    data = Data.objects.get(id=id)

    params = {
        "id": id,
        "data": data
    }
    return render(request, "show/index.html", params)
