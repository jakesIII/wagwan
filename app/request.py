
import urllib.request,json
from .models import Source_data,Articles_data

api_key = None

sources_base_url = None

article_base_url = None

def configure_request(app):
    global api_key,sources_base_url,article_base_url
    api_key = app.config['API_KEY']
    sources_base_url = app.config['NEWS_SOURCES_KEY']
    article_base_url=app.config['NEWS_ARTICLE_KEY']

def process_source(source_list):
   source_results = []
   for source_item in source_list:
       id = source_item.get('id')
       name = source_item.get('name')
       url = source_item.get('url')
      
       source_object = Source_data(id,name,url)

       source_results.append(source_object)
   return source_results

def get_source(category):
   get_source_url = sources_base_url.format(category,api_key)
   print('********get_source_url***********')
   print(get_source_url)
 
   with urllib.request.urlopen(get_source_url) as url:
       get_source_data = url.read() #using the read function to get the response and store it in the variable
       get_source_response = json.loads(get_source_data) #converting JSON response to a python dictionary using the json.loads function
       source_results = None
       if get_source_response['sources']:
           source_result_list=get_source_response['sources']
           source_results=process_source(source_result_list) #process_results is a function that takes in the list of dictionary objects and returns a list of movie objects
   return source_results


# def get_news(category):

#     the_news_url = sources_base_url.format(category,api_key)
#     print('*********the_news************')
#     print(the_news_url)
#     with urllib.request.urlopen(the_news_url) as url:

#         the_news_data = url.read()
#         the_news_response = json.loads(the_news_data)

#         news_result = None
        
#         if the_news_response['sources']:

#             news_result_list = the_news_response['sources']
#             news_result = process_the_news(news_result_list)
            
#     return news_result

# def process_the_news(news_list):


#     the_news_result = []


#     for source_item in news_list:

#         id = source_item.get('id')
#         name = source_item.get('name')
#         url = source_item.get('url')

#         news_object = Source_data(id,name,url)
#         the_news_result.append(news_object)
        

#     return the_news_result



# Get Articles

def get_articles(id):
    the_articles = article_base_url.format(id,api_key)

    with urllib.request.urlopen(the_articles) as url:
        the_articles_data = url.read()
        the_articles_response = json.loads(the_articles_data)

    the_articles_result = None

    if the_articles_response['articles']:
        articles_result_list = the_articles_response['articles']
        the_articles_result = process_the_articles(articles_result_list)

    return the_articles_result

def process_the_articles(article_list):

    the_articles_result = []

    for article_item in article_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        
        articles_object = Articles_data(id, name, author, url, urlToImage, publishedAt)
        the_articles_result.append(articles_object)

    return the_articles_result
