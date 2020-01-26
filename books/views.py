from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from datetime import datetime

from books.models import Book
from .forms import SearchForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            q = form.cleaned_data.get('user_query')
            if q:
                return HttpResponseRedirect(reverse_lazy('books:search', args=[q]))
    else:
        form = SearchForm()
    return render(request, 'books/book_home.html', {'form': form})

class BookSearch(ListView):
    template_name='books/book_results.html'
    def get_queryset(self, **kwargs):
        # I forgot to reference self lol
        query = self.kwargs['query']
        if query=='ALLBOOKS':
            allResults = Book.objects.all().order_by('-date_created')
            return allResults
        elif query:
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

class BookCreate(CreateView):
    #template_name='books/book_form.html'
    template_name='books/book_form.html'
    model = Book
    fields = [
        'post_type', 
        'book_title',
        'book_author',
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