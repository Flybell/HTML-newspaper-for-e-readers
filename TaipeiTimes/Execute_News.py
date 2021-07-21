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
from News import * #magazine or newspaper classes

total = [] #list of issue objects

print("Getting the news...")
tf = Front() #a front page issue object
td = Taiwan() #a Taiwan news issue object
print("Downloading the content... ")
tf.compile_articles() #get and create article objects
td.compile_articles()
print("Creating the ebook... ")
total = [tf, td]
create_ebook(total) #html writing

print("\nToday's paper is now in the folder. Enjoy!")
