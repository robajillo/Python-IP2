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

# @main.route('/articles/<int:id>')
# def sources(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     article = get_source(id)
    

#     return render_template('articles.html',article = article)

# @main.route('/News-Articles')
# def NewsArticles():
#     """
#     View that would return news articles
     
#     """
#     cnn_news = get_articles('cnn')
#     return render_template('articles.html', cnn=cnn_news)

@main.route('/article/<id>')
def article(id):

    
    article = get_source(id)


    return render_template('articles.html',article = article)

# @main.route('/News-Articles')
# def NewsArticles():
#     """
#     View that would return news articles
     
#     """
#     entertainment_articles = get_articles('entertainment')
#     technology_articles = get_articles('technology')
#     google_articles = get_articles('google')
#     return render_template('articles.html',entertainment=entertainment_articles, tech =technology_articles,google=google_articles)
