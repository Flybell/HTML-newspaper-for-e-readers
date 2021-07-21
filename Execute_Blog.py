"""
The main script

Run this script with "python Execute_Blog.py" in command line

Crawls through a monthly archive of the blog to compile the latest 30 articles into
a 1 column html file (for html -> pdf or html -> mobi export in Calibre).

"""

import re #regular expression
import io #for UTF8 processing
from bs4 import BeautifulSoup #HTML parser library
from datetime import date #get dates

from Blogs import * #class file of blog and post objects
from HTML_Blog import *#html writer


print("Getting posts...")
blog = Blog() #create blog object
blog.grab_content() #get content from the website and create article objects

print("Creating the html ebook... ")
create_ebook("PhilosophersCocoon_", blog) #generate ebook

print("\nToday's blog is now in the folder. Enjoy!") #status report
