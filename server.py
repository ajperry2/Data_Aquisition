# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc
from __future__ import print_function # In python 2.7
from flask import Flask, render_template
from doc2vec import *
import sys
from jinja2 import FileSystemLoader,Environment

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    template = env.get_template('articles.html')
    return(template.render(article_list = articles))




@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """

    i = 0
    for index,article in enumerate(articles):
        if article[0] == topic+'/'+filename:
            i = index
            break
    article = articles[i]
    print(article)
    text = get_text('./bbc/'+article[0])
    rec = recommended(article,articles,6)[1:]

    for re in rec:
        print(re,sys.stderr)
    loader = FileSystemLoader('templates')
    env = Environment(loader=loader)
    template = env.get_template('article.html')

    return(template.render(article = article, rec=rec,text = text))
# initialization
#i = sys.argv.index('server:app')
#glove_filename = sys.argv[i+1]
#articles_dirname = sys.argv[i+2]

glove_filename = sys.argv[1]
articles_dirname = sys.argv[2]


gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)
app.run('0.0.0.0')
