from ..requests import get_sources
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
    technology_news = get_sources("technology")
    return render_template('sources.html',general=general_news,entertainment=entertainment_news,sports=sports_news )

