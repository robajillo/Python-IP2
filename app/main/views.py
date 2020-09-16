from ..requests import get_sources,get_source
from flask import render_template,redirect,request,url_for
from . import main

@main.route('/')
def HomePage():
    """
    Views thats renders news sources to the home page
    """
    general_news = get_sources('general')
    entertainment_news = get_sources("entertainment")
    sports_news = get_sources("sports")

    return render_template('sources.html',general=general_news,entertainment=entertainment_news,sports=sports_news )

@main.route('/article/<id>')
def article(id):

    
    article = get_source(id)


    return render_template('articles.html',article = article)
