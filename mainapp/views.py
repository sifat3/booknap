from django.shortcuts import render
from .models import Book


def index(request):
	return render(request, 'index.html')


def all_books(request):

	books = Book.objects.all()

	return render(request, 'all_books.html', {'books': books})


def details(request, id):
	book = Book.objects.filter(id = id).first()
	return render(request, 'details.html', {'book':book})

def borrowed(request):
	books = Book.objects.filter(borrowed=True)
	return render(request, 'borrowed.html', {'books': books})


def lent(request):
	books = Book.objects.filter(lent=True)
	return render(request, 'lent.html', {'books': books})