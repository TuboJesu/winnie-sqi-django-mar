from django.shortcuts import render, get_object_or_404

from .models import Book

# Create your views here.
def all_books(request):
    return render(request, "review/all-books.html", {"books": Book.objects.all()})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "review/book-detail.html", {"book": book})
