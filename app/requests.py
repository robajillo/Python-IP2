import urllib.request,json
from .models import Articles,Sources

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
#getting articles url
# art_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

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
        source_object = Source(id,name,description,url,category,language,country)
        
        source_results.append(source_object)

    return source_results



    