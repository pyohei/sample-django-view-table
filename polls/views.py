from django.shortcuts import render
from django.http import HttpResponse

from .models import Books

# Create your views here.


def index(request):
    book_list = Books.objects.values_list('category', 'count')
    return HttpResponse(book_list)