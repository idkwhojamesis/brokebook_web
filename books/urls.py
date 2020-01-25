from django.urls import path
from . import views
from books.views import BookCreate, BookDetail, BookList, BookSearch

app_name = 'books'
urlpatterns = [
    path('books', views.index, name='index'),
    path('books/form', BookCreate.as_view(), name='form'),
    path('books/detail/<int:pk>', BookDetail.as_view(), name='detail'),
    path('books/list', BookList.as_view(), name='list'),
    path('books/search/<str:query>/<int:page>', BookSearch.as_view(),name='search')
]