from django.urls import path

from . import views

app_name = 'searcher'
urlpatterns = [
    path('', views.books_by_author, name='home'),
    path('a/', views.find_author, name='author_finder'),
]
