from django.shortcuts import render
from .models import Swimmer


def data_list(request):
    swimmers = Swimmer.objects.all()
    return render(request, 'data/data_list.html', {'swimmers': swimmers})

