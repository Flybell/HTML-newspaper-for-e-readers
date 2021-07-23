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

def write_html_head(f, issue_date):
    f.writelines(["<!DOCTYPE html>", "<html>", "<body>"])
    f.write("<p>Issue date: " + issue_date + "</p>")

def write_html_end(f):
    f.writelines(["</div>", "</body>", "</html>"])

def write_TOC(f, section):
    """writes table of contents
     input: an issue object, calls out each article object
     output: writes titles of article objects as TOC """
    f.write("<h1 id=toc>Table of Contents</h1>")
    f.write("<h2>"+ section.title+ "</h2>")
    for a in section.articles:
        f.write("<h3><a href='#%s'>" %a.ref)
        f.write(a.title + "<br>")
        f.write("</a></h3>")

def write_articles(f, section):
    """ writes each article one by one.
    input: issue object; output: writes articles into HTML file """
    f.write("<h2>"+ section.title+ "</h2>")
    for a in section.articles:
        f.writelines(["<h3 id='%s'>" %a.ref, a.title, "</h3>"]) #write title
        [f.write(para) for para in a.content] #write content
        f.write("<br><a href='#toc'>Back</a><br>")
        f.write("<hr class='rounded'><br>")

def write_issue(f, paper):
    """writes metadata, table of contents, artices
       input: list of issues"""
    f.write("<div style='columns: 2'>")
    [write_TOC(f, section) for section in paper]
    [write_articles(f, section) for section in paper]
    f.write("</div>")

def create_ebook(filename, issue_date, paper):
    """creates a new html file and names it. writes the file.
    input: list of issue objects
    output: compiled html file in folder"""
    with io.open(filename, "w+", encoding="UTF8") as f:
        write_html_head(f, issue_date)
        write_issue(f, paper)
        write_html_end(f)
