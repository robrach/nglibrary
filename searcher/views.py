from django.shortcuts import render
import requests


def search(request):
    author = {}
    if 'author_id' in request.GET:
        author_id = str(request.GET['author_id'])
        url = f'https://openlibrary.org/authors/{author_id}.json'
        response = requests.get(url)
        author = response.json()
    return render(request, 'searcher/home.html', {'author': author})


def find_author(request):
    authors = {}
    if 'author' in request.GET:
        author = str(request.GET['author'])
        author = author.replace(' ', '+')
        print(author)
        url = f'https://openlibrary.org/search/authors.json?q={author}'
        response = requests.get(url)
        authors = response.json()
        print(authors)
    return render(request, 'searcher/author_finder.html', {'authors': authors})
