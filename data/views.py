from django.shortcuts import render, get_object_or_404
from .models import Swimmer


def data_list(request):
    swimmers = Swimmer.objects.all()
    return render(request, 'data/data_list.html', {'swimmers': swimmers})

def swimmer_detail(request, pk):
    swimmer = get_object_or_404(Swimmer, pk=pk)
    return render(request, 'data/swimmer_detail.html', {'swimmer': swimmer})
