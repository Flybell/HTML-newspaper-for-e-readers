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

Taipei_times = {
    "base" : "https://www.taipeitimes.com/xml/index.rss",
    "front_base" : "https://www.taipeitimes.com/News/front/archives/",
    "front_title" : "Today's Headlines",
    "taiwan_base" : "https://www.taipeitimes.com/News/taiwan/archives/",
    "taiwan_title" : "Today's Taiwan News",
}

print("Getting the news...")
soup = create_soup(Taipei_times["base"])
issue_date = retrieve_date(soup)
filename = "TaipeiTimes_" + date.today().strftime("%Y%m%d") +".html"

print("Finding the sections... ")
front = Section(Taipei_times["front_base"], Taipei_times["front_title"])
print (front.title)
taiwan = Section(Taipei_times["taiwan_base"], Taipei_times["taiwan_title"])
paper = [front, taiwan]

print("Downloading the news... ")
for section in paper:
    article_urls = section.find_article_urls(soup)
    section.create_article_objects(article_urls)

print("Creating the ebook... ")
create_ebook(filename, issue_date, paper) #html writing

print("\nToday's paper is now in the folder. Enjoy!")
