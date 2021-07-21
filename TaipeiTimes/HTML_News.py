"""
HTML writer

Writes the HTML header, body, end
Body consists of two parts:
(1) table of contents of each issue and issue date,
(2) the articles of each issue, separated by dividers
"""

import re #regular expression
import io #handle files
import string #handle text
from datetime import date #get dates

def write_html_head(f):
    f.writelines(["<!DOCTYPE html>", "<html>", "<body>"])
    f.write("<h1 id=toc>Table of Contents</h1>")

def write_html_end(f):
    f.writelines(["</div>", "</body>", "</html>"])

def write_metadata(f, issue):
    """Writes the title of each issue and their dates at the beginning"""
    f.write("<h2>"+ issue.filename+ "</h2>")
    f.write("<p>Date: " + issue.issuedate + "</p>")

def write_TOC(f, issue):
    """writes table of contents
     input: an issue object, calls out each article object
     output: writes titles of article objects as TOC """
    for a in issue.articles:
        ref = a.title[1-3]
        f.write("<h4><a href='#%s'>" %ref)
        f.write(a.title + "<br>")
        f.write("</a></h4>")

def write_articles(f, issue):
    """writes each article one by one
     input: issue object
     output: writes articles into HTML file """
    for a in issue.articles:
        ref = a.title[1-3]
        f.writelines(["<h3 id='%s'>" %ref, a.title, "</h3>"]) #write title
        [f.write(para) for para in a.content] #write content
        f.write("<br><a href='#toc'>Back</a><br>")

def write_issue(f, issues):
    """writes metadata, table of contents, artices
       input: list of issues"""
    f.write("<div style='columns: 2'>")
    for issue in issues:
        write_metadata(f, issue)
        write_TOC(f, issue) #write table of content
    for issue in issues:
        write_articles(f, issue) #write articles
        f.write("<hr class='rounded'><br>")
    f.write("</div>")

def create_ebook(issues):
    """creates a new html file and names it. writes the file.
    input: list of issue objects
    output: compiled html file in folder"""
    filename = "TaipeiTimes_" + date.today().strftime("%Y%m%d") +".html"
    with io.open(filename, "w+", encoding="UTF8") as f:
        write_html_head(f)
        write_issue(f, issues)
        write_html_end(f)
