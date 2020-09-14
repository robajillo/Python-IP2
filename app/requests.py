import urllib.request,json
from .models import Articles,Sources


# Getting api key
api_key = None
# Getting the movie base url
base_url = None
#getting articles url
art_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    art_url = app.config['NEWS_ARTICLES_API_URL']

def get_sources(category):
    '''
    Function to get json response to the url request for news sources
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(source_list):
    '''
    Function  that processes the source results and transform them to a list of objects
    
    Args:
        source_list: A list of dictionaries that contain source details
    
    Returns :
        source_results: A list of source objects
    '''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        source_object = Sources(id,name,description,url,category,language,country)
        
        source_results.append(source_object)

    return source_results

def get_articles(article):

    articles_url = art_url.format(article,api_key)
    # print(art_url)
    with urllib.request.urlopen(articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    return articles_results

def process_articles(articles_list):
    articles_outcome = []

    for one_article in articles_list:
        source = one_article.get("source")
        author = one_article.get("author")
        description = one_article.get("description")
        title = one_article.get("title")
        url = one_article.get("url")
        urlToImage = one_article.get("urlToImage")
        publishedAt = one_article.get("publishedAt") 
        article_object = Articles(source, author, title, description, url, urlToImage, publishedAt)
        articles_results.append(article_object)
    
    return articles_results
    