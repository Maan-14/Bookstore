from django.views.generic import ListView, DetailView

from .models import Book

class BookListView(ListView):
    model = Book
    #using book_list to replace object_list in looping in the template
    context_object_name = "book_list"
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"