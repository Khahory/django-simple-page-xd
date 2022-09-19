from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    return HttpResponse('que si cameto que si')


# noinspection PyUnresolvedReferences
def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return HttpResponse(f"Book: {book.title}, publicado el {book.pub_date}")
