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
    author_key = []
    author_work_count = 0
    author_info = {}
    author_books = {}
    if 'author' in request.GET:
        content = get_author_key_and_work_count(request)
        author_key = content[0]
        author_work_count = content[1]
        author_info = get_author_info(author_key)
        author_books = get_author_books(author_key, author_work_count)
    return render(request, 'searcher/home.html', {
        'author_key': author_key,
        'author_work_count': author_work_count,
        'author_info': author_info,
        'author_books': author_books,
    })


def get_author_key_and_work_count(request):
    author = str(request.GET['author'])
    author = author.replace(' ', '+')
    url = f'https://openlibrary.org/search/authors.json?q="{author}"'
    response = requests.get(url)
    content = response.json()
    author_key = content['docs'][0]['key']
    author_work_count = content['docs'][0]['work_count']
    return author_key, author_work_count


def get_author_info(author_key):
    url = f'https://openlibrary.org/authors/{author_key}.json'
    response = requests.get(url)
    author_info = response.json()
    return author_info


def get_author_books(author_key, author_work_count):
    url = f'https://openlibrary.org/authors/{author_key}/works.json?limit={author_work_count}'
    response = requests.get(url)
    author_books = response.json()
    return author_books
