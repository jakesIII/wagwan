
from flask import render_template,request,redirect,url_for
from . import main
from ..request import process_source,get_source
from ..models import Source_data

@main.route('/')
def index():
    
    the_sources = get_source('general')
    print('********the_sources************')
    print(the_sources)
    title = 'Home - For all your news update'

    return render_template('index.html', title = title, the_sources = the_sources)

@main.route('/article/<id>')
def articles(id):

    the_articles = process_source(id)
    title = 'Home - For all your news update'
    return render_template('article.html', title = title, articles = the_articles)
