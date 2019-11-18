import os

class Config():

    NEWS_ARTICLE_KEY='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

    NEWS_SOURCES_KEY = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True
# 'https://newsapi.org/v2/everything?sources={}&apiKey={}

config_options = {
'development':DevConfig,
'production':ProdConfig
}