from django.shortcuts import render


def data_list(request):
    return render(request, 'data/data_list.html', {})

