from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django import forms
from books.models import Book

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the books index.")

class BookSearch(ListView):
    template_name='books/book_results.html'
    def get_queryset(self, **kwargs):
        # I forgot to reference self lol
        query = self.kwargs['query']
        titleResults = Book.objects.filter(book_title__icontains=query)
        classResults = Book.objects.filter(class_subject__icontains=query)
        profResults = Book.objects.filter(professor__icontains=query)
        mergedResults = titleResults | classResults | profResults
        mergedResults = mergedResults.order_by('-date_created')
        return mergedResults
    paginate_by = 5

class BookDetail(DetailView):
    template_name='books/book_detail.html'
    model = Book

class BookList(ListView):
    template_name='books/book_list.html'
    model = Book

class BookCreate(CreateView):
    template_name='books/book_form.html'
    model = Book
    fields = [
        'post_type', 
        'book_title',
        'campus', 
        'professor', 
        'class_subject', 
        'class_section', 
        'semester', 
        'year', 
        'online_code', 
        'edition', 
        'condition',
        'contact_info',
        ]