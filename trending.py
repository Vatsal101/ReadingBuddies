from bs4 import BeautifulSoup
import requests
import random



url = "https://www.goodreads.com/shelf/show/trending"

results = requests.get(url)

doc = BeautifulSoup(results.text, "html.parser")


list = doc.find_all(class_ = "elementList")
li = []

for book in list:
    balls = book.find(class_ = "bookTitle")
    try:
        x = balls.string
    except AttributeError:
        list.remove(book)

for x in range(3):
    num = random.randint(0,len(list)-1)
    li.append(list[num])
    list.pop(num)


def get_trending_books():

    books = []


    for l in li:

        bok = l.find(class_ = "bookTitle")

        books.append(bok.string)


        for x in range(len(books)):
            if "(" in books[x]:
                index = books[x].index("(")
                books[x] = books[x][:index-1]

    return books

def get_t_authors():
        
    authors = []


    for l in li:

        bok = l.find(class_ = "authorName")

        authors.append(bok.string)


        for x in range(len(authors)):
            if "(" in authors[x]:
                index = authors[x].index("(")
                authors[x] = authors[x][:index]

    return authors

def get_t_url():
    
    urls = []

    for l in li:

        bok = l.find("img")
        urls.append(bok['src'])

    return urls


    
    
        

