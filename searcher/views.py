from django.shortcuts import render
import requests


def search(request):
    author = {}
    if 'author_id' in request.GET:
        author_id = request.GET['author_id']
        url = f'https://openlibrary.org/authors/{author_id}.json'
        response = requests.get(url)
        author = response.json()
    return render(request, 'searcher/home.html', {'author': author})
