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



def books_by_author(request):
    author_key = ""
    if 'author' in request.GET:
        author_key = get_author_key(request)
        print('hej' + author_key)
    return render(request, 'searcher/home.html', {'author_key': author_key})



def get_author_key(request):
    author = str(request.GET['author'])
    author = author.replace(' ', '+')
    url = f'https://openlibrary.org/search/authors.json?q="{author}"'
    response = requests.get(url)
    author_key = response.json()['docs'][0]['key']
    print(author_key)
    return author_key


def get_author_info(author_key):
    url = f'https://openlibrary.org/authors/{author_key}.json'
    response = requests.get(url)
    author_info = response.json()
    return author_info