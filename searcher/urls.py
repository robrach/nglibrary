from django.urls import path, include

from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'authors', views.AuthorsViewSet)

app_name = 'searcher'
urlpatterns = [
    path('', views.books_by_author, name='home'),
    path('api/', include(router.urls)),
]
