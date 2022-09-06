import django.views.defaults
from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/authors', views.AuthorsViewSet)

app_name = 'searcher'
urlpatterns = [
    path('', views.books_by_author, name='home'),
    path('api/', views.api_info, name='API'),
    path('', include(router.urls)),
    path('api/author/<str:name>/', views.author_detail),
    path('about/', views.about, name='about'),
]
