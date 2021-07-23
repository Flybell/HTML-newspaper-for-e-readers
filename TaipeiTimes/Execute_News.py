"""
The main script

Run this script with "python Execute_News.py" in command line

Crawls through each online issue to compile the articles into
a 2 column html file (for html -> pdf export in Calibre)

"""

import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library

from HTML_News import * #functions related to web and html
from Class_News import * #magazine or newspaper classes

issue_date = ""
paper = [] #list of section
base = "https://www.taipeitimes.com/xml/index.rss"

paper = [
    {
        "title": "Today's Headlines",
        "base": "https://www.taipeitimes.com/News/front/archives/",
        "articles": [],
    },
    {
        "title": "Today's Taiwan News",
        "base": "https://www.taipeitimes.com/News/taiwan/archives/",
        "articles": [],
    }
]

print("Getting the news...")
soup = create_soup(base)
issue_date = retrieve_date(soup)
filename = "TaipeiTimes_" + date.today().strftime("%Y%m%d") +".html"

print("Downloading the news... ")
for section in paper:
    article_urls = find_article_urls(soup, section["base"])
    print("\n" + section["title"])
    print("There are " + str(len(article_urls)) + " articles.\n")
    section["articles"] = create_article_objects(article_urls)

print("Creating the ebook... ")
create_ebook(filename, issue_date, paper)

print("\nToday's paper is now in the folder. Enjoy!")
