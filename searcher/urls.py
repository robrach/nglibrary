from django.urls import path

from . import views

app_name = 'searcher'
urlpatterns = [
    path('', views.index, name='index')
]
