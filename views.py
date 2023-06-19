from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, flash, make_response
from flask_login import login_required, current_user

from ReadingList.trending import get_trending_books
from ReadingList.trending import get_t_authors
from ReadingList.trending import get_t_url
from ReadingList.output import scrape
from ReadingList.models import *
views = Blueprint('views', __name__)

@views.route('/', methods=["GET","POST"])
@login_required
def home():
    if request.method == 'POST':

        books = []

        print(request.form.get("book0"))


        for x in range(4):
            box = request.form.get("book"+str(x))
            if(box!= None):
                books.append(box)

        for x in books:
            list = x.split("+")

            new_book = Books(b_title = list[0],b_author = list[2], b_read = False, b_img_src = list[1], user_id = current_user.id)
            db.session.add(new_book)
            db.session.commit()
        
        flash("Books Have been added to your list!", category='success')


    t = get_trending_books()
    a = get_t_authors()
    u = get_t_url()


    return render_template("main.html", trending_books = t, trending_authors = a, trending_urls = u, user = current_user)

@views.route("/mylist",  methods=["GET", "POST"])
@login_required
def list():
    if request.method == 'POST':

        done_books = []

        for x in range(100):
            box = request.form.get("check"+str(x))
            if(box!= None):
                done_books.append(box)

        counter = 0
        for book in current_user.books:

            if book.b_title == done_books[counter]:
                book.b_read = True
                db.session.commit()
                counter+=1
                
            

        




    name = current_user.name
    if(name.count(" ") > 0):
        ind = name.index(" ")
        name = name[0:ind]
    # for book in current_user.books:
    #     #print(book.b_title + " by "+ book.b_author)
    #     print(book.b_img_src)
    #     print(book.b_read)
    return render_template("list.html", user = current_user, name = name)

@views.route("/search", methods=["GET", "POST"])
@login_required
def search():

    if request.method == 'POST':
        
        list = []
        genres = []

        box1 = request.form.get('box1')
        list.append(box1)
        box2 = request.form.get('box2')
        list.append(box2)        
        box3 = request.form.get('box3')
        list.append(box3)
        box4 = request.form.get('box4')
        list.append(box4)
        box5 = request.form.get('box5')
        list.append(box5)
        box6 = request.form.get('box6')
        list.append(box6)
        box7 = request.form.get('box7')
        list.append(box7)
        box8 = request.form.get('box8')
        list.append(box8)
        box9 = request.form.get('box9')
        list.append(box9)
        box10 = request.form.get('box10')
        list.append(box10)
        box11 = request.form.get('box11')
        list.append(box11)
        box12 = request.form.get('box12')
        list.append(box12)
        box13 = request.form.get('box13')
        list.append(box13)
        box14 = request.form.get('box14')
        list.append(box14)
        box15 = request.form.get('box15')
        list.append(box15)
        
        for box in list:
            if box != None:
                genres.append(box)

        for x in range(0,len(genres)):
            if genres[x] == "Children's":
                genres[x] = "Childrens"


        string = ' '.join(map(str, genres))

        return redirect(url_for('views.results', user = current_user, list = string))
        
 
    return render_template("search.html", user = current_user)

@views.route("/results", methods=["GET", "POST"])
@login_required
def results():


    if request.method == 'POST':

        book_list = []

        for x in range(100):
            box = request.form.get("book"+str(x))
            if(box!= None):
                book_list.append(box)
                
        for x in book_list:
            list = x.split("+")

            new_book = Books(b_title = list[0],b_author = list[2], b_read = False, b_img_src = list[1], user_id = current_user.id)
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for('views.submit'))

    
    l = request.args.get("list")
    bean = str(request.args.get("list"))
    bean = bean.replace(" ", "+")
    l = str(l)
    li = l.split(" ")

    values = scrape(li)
    k = values.keys()

    list = []
    for x in k:
        counter = 0
        for y in values[x]["book_title"]:
            counter+=1
        list.append(counter)

    length = len(list)

    return render_template("results.html", user = current_user, dict = values, keys = k, list = list, lenz = length, b=bean)


@views.route("/submit", methods=["GET", "POST"])
@login_required
def submit():
    return render_template("submit.html", user = current_user)



@views.route("/clear", methods=["GET", "POST"])
@login_required
def clear():
    for book in current_user.books:

        db.session.delete(book)
        db.session.commit()


    print("books gone")
    return render_template("submit.html", user=current_user)
    







