from flask import Flask, render_template, request, redirect, session, url_for, json, flash
from ReadingList import create_app

app = create_app()

if __name__ == '__main__':
    # @app.route('/')
    # def homescreen():
    #     return render_template("main.html")
    app.run(debug=True, host="0.0.0.0")
    

