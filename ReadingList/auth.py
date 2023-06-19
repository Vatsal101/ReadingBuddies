from flask import Blueprint, render_template, request, flash, session, redirect, url_for
from ReadingList.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email')
        psswrd = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, psswrd):
                flash('Logged in Successfully', category='success')
                login_user(user, remember=True)    
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, please try again', category="danger")
        else:
            flash('Email does not exist', category="danger")

    return render_template("login.html", user=current_user)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        psswrd = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email Already exists', category='danger')
        elif email == "":
            flash("Please Provide an Email", category='danger')
        elif name == "":
            flash("Please Provide a Name", category='danger')
        elif ("@" in email) == False:
            flash("Please Provide a real Email", category='danger')
        elif len(name) < 1:
            flash("Please Provide a name with more than one character", category='danger')
        elif len(psswrd) < 7:
            flash("Your Password is too short. Must at least be 7 characters", category='danger')
        else:
            new_user = User(email = email, name = name, password = generate_password_hash(psswrd, method = "sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Account has been created", category='success')
            return redirect(url_for('auth.login'))

            
    return render_template("signup.html",user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been Logged Out", category='warning')
    return redirect(url_for('auth.login'))
