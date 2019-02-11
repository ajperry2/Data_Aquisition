# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys
from jinja2 import FileSystemLoader,Environment
import netifaces as ni

ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
print("I'm at IP "+ip)
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

# initialization
glove_filename = sys.argv[1]
articles_dirname = sys.argv[2]

gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)
print(articles)
app.run('0.0.0.0',port=5000)
