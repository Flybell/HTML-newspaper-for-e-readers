"""
HTML writer

Writes the HTML header, body, end

Body consists of three parts:
(1) table of contents of each issue and issue date,
(2) the articles of each issue,
(3) after each article, the comments under each blog posts

"""
import re #regular expression
import io
import string
from bs4 import BeautifulSoup #web parsing library
from datetime import date #get dates


def write_html_head(f):
    f.writelines(["<!DOCTYPE html>", "<html>", "<body>"])
    f.write("<h1 id=toc>Table of Contents</h1>") #anchor id

def write_html_end(f):
    f.writelines(["</div>", "</body>", "</html>"])

def write_TOC(f, post):
    """writes table of contents
    input: a post object
    output: writes from the title attribute of the post object """
    f.write("<h4><a href='#%s'>" %post.title[0-3]) #hyperlink
    f.write(post.title + "<br>")
    f.write("</a></h4>")

def write_articles(f, post):
    """writes each article one by one
     input: a post object
     output: writes from the content attribute of the post objecct """
    f.writelines(["<h3 id='%s'>" %post.title[0-3], post.title, "</h3>"]) #anchor ids
    [f.write(para) for para in post.content]
    f.write("<br><a href='#toc'>Back</a><br>")

def write_comments(f, post):
    """writes the comments of the article one by one
     input: a post object
     output: writes from the comments attribute of the post object """
    f.writelines(["<h3 id='%s'>Comments</h3>"])
    [f.write(para) for para in post.comments]
    f.write("<br><a href='#toc'>Back</a><br>") #hyperlink

def write_issues(f, blog):
    """ for each post in a blog, write TOC
        then for each post in a blog, write the posts and comments """
    for post in blog.posts:
        write_TOC(f, post) #write table of content
    f.write("<hr class='rounded'><br>")
    for post in blog.posts:
        write_articles(f, post) #write articles
        f.write("<hr class='dotted'>")
        write_comments(f, post)
        f.write("<hr class='rounded'><br>")

def create_ebook(filename, blog):
    """compiles a html file out of a blog object
    input: a blog object and filename
    output: compile html file"""
    filename = filename + date.today().strftime("%Y%m%d") +".html" #add today's date to name
    with io.open(filename, "w+", encoding="UTF8") as f:
        write_html_head(f)
        write_issues(f, blog)
        write_html_end(f)
