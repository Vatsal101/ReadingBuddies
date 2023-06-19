from bs4 import BeautifulSoup
import requests
import random

url = "https://www.goodreads.com/shelf/show/trending"

results = requests.get(url)

doc = BeautifulSoup(results.text, "html.parser")


list = doc.find_all(class_ = "elementList")
li = []

#print(list[0].encode("utf-8"))

for x in range(3):
    num = random.randint(0,len(list)-1)
    li.append(list[num])
    list.pop(num)

authors = []
descriptions = []



for l in li:
    bok = l.find(class_ = "bookTitle", href=True)

    authors.append(bok.string)


    for x in range(len(authors)):
        if "(" in authors[x]:
            index = authors[x].index("(")
            authors[x] = authors[x][:index]




    new_url = "https://www.goodreads.com" + bok['href'] 
    result = requests.get(new_url)
    soup = BeautifulSoup(result.text, "html.parser")

    a = soup.find(class_ = "Formatted")

    print(a)



print(authors)
    
    


















# bok = doc.find_all(class_ = "bookTitle")
# books = []
# bby=[]

# for book in bok:
#     books.append(book.string)


# for x in range(len(books)):
#     if "(" in books[x]:
#         index = books[x].index("(")
#         books[x] = books[x][:index]

# for x in range(3):
#     num = random.randint(0,len(books)-1)
#     bby.append(books[num])
#     books.pop(num)
        


# authors = doc.find_all(class_ = "authorName")

# #name = authors[0].find("span")
# names = []
# for name in authors:
#     n = name.find("span")
#     names.append(n.string)

# print(names)






# with open("test.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tag = doc.title

# tags = doc.find_all("p")

# bee = tags.find_all("b")

#print(bee)



#print(tags)