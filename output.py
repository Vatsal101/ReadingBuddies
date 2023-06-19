from bs4 import BeautifulSoup
import requests
import random


def scrape(genres):

    info_dict = { }
    gen = genres.copy()
    for x in range(len(genres)):
        string = genres[x]
        genres[x] = {
            "book_title" : None,
            "author" : None,
            "image_src": None
        }
        info_dict[str(string)] = genres[x]

    for g in gen:
        url = f"https://www.goodreads.com/genres/most_read/{g}"
        doc = requests.get(url).text
        soup = BeautifulSoup(doc, "html.parser")

        url_list = []
        new_url_list=[]



        book_title_list = []
        image_src_list = []
        author_list = []

        tops = soup.find_all("div", class_="coverRow")


        #gets urls for all books
        for y in tops:
            for x in y.find_all('a', href=True):
                url_list.append(x["href"])
                

        #chooses a random 5 books from the list
        for x in range(5):
            num = random.randint(0,len(url_list)-1)
            new_url_list.append(url_list[num])
            url_list.pop(num)

        #print(url_list)
        #gets information from the randomly chosen urls
        for urls in new_url_list:
            url2 = f"https://www.goodreads.com" + urls
            #print(url2)
            doc2 = requests.get(url2).text
            soup2 = BeautifulSoup(doc2, "html.parser")

            book_tit = soup2.find("h1", class_= "Text Text__title1")
            auth = soup2.find("span", class_ ="ContributorLink__name")

            try:
                book_title_list.append(book_tit.string)
            except AttributeError:
                
                continue

            try:
                author_list.append(auth.string)
            except AttributeError:
                continue


            image_source = soup2.find("img", class_ = "ResponsiveImage")
            image_src_list.append(image_source['src'])
        
     # appends the list of book titles with the genre as the key for the first, then book title the key for the 2nd
        info_dict[g]["book_title"] = book_title_list
        info_dict[g]["author"] = author_list
        info_dict[g]["image_src"] = image_src_list
        
    return info_dict


                