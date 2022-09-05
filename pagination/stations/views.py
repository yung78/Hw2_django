from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', 'r', encoding='utf8', newline='\n') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [x for x in reader]
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(data, 10)
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'page': page,
        'data': page,
    }
    return render(request, 'stations/index.html', context)
