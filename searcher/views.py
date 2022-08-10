from django.shortcuts import render
import requests


def books_by_author(request):
    author_key = []
    author_work_count = int
    author_info = {}
    books = {}
    searching_result = 1
    if 'author' in request.GET:
        content = get_author_key_and_work_count(request)
        if content:
            author_key = content[0]
            author_work_count = content[1]
            author_info = get_author_info(author_key)
            books = get_author_books(author_key, author_work_count)
        else:
            searching_result = 0
    return render(request, 'searcher/home.html', {
        'author_key': author_key,
        'author_work_count': author_work_count,
        'author_info': author_info,
        'books': books,
        'searching_result': searching_result,
    })


def get_author_key_and_work_count(request):
    author = str(request.GET['author'])
    author = author.replace(' ', '+')
    url = f'https://openlibrary.org/search/authors.json?q="{author}"'
    response = requests.get(url)
    content = response.json()
    if content['numFound'] > 0:
        author_key = content['docs'][0]['key']
        author_work_count = content['docs'][0]['work_count']
        return author_key, author_work_count
    else:
        return None


def get_author_info(author_key):
    url = f'https://openlibrary.org/authors/{author_key}.json'
    response = requests.get(url)
    author_info = response.json()
    return author_info


def get_author_books(author_key, author_work_count):
    url = f'https://openlibrary.org/authors/{author_key}/works.json?limit={author_work_count}'
    response = requests.get(url)
    author_books = response.json()['entries']
    books = {}
    for book in author_books:
        title = book['title']
        openlibrary_url = f"https://openlibrary.org{book['key']}"
        books[title] = openlibrary_url
    return books
