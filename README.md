# HTML newspaper for e-readers 
Crawls and scrapes a site (news, magazine, blog, etc) for articles to compile into a lightly formatted .html file for conversion into PDF, EPUB, etc., by programs like Calibre. Personal use case: the .html file is loaded into Calibre to convert into a .MOBI file for Kindle and a PDF file for a large e-reader. 

Output: a compiled HTML file 
* Table of Contents (hyperlinked to article titles) 
* Date of issue 
* Articles (with a back to TOC hyperlink at the end of each article)
* Comments under a blog

Example output: see TaipeiTimes_20210721.html

These scripts are highly specific to the publications they're targetting. They are thus not for general use. 
The News package (Execute_News,py, HTML_News.py, Class_News.py) is for Taipei Times (http://www.taipeitimes.com/)
The Blog package (Execute_Blog.py, HTML_Blog.py, Class_Blog.py) is for The Philosopher's Cocoon (https://philosopherscocoon.typepad.com/)
Other packages have been developed for subscribed or paywalled content, but will not be made available here for obvious reasons. 
The principles are the same, though, which will be explained in detail below. The user is encouraged to use and modify the scripts for their own purposes.

# Files and what they do
There are three Python scripts: 
* Execute (Execute_News.py, Execute_Blog.py, etc) 
* HTML writer (HTML_News.py, HTML_Blog.py, etc)
* Class file of objects (Class_News.py, Class_Blog.py, etc)

*Execute* is the main script. It uses the *Class* file to create objects of each issue (a collection of articles) and each article. It then sends these objects to the *HTML* writer to create and compile a basic formatted html file. A very simple three step process. 

I've added a ```#customize``` note behind each line that needs to be customized to the specific outlet. The key is to find the right HTML tag to retrieve the title of article, the content of the article (paragraph by paragraph), and the comments of blog articles. See the scripts for further documentation.

# External dependencies, or what the script needs to run 
* Beautiful Soup (https://pypi.org/project/beautifulsoup4/) ```pip install beautifulsoup4``` to parse and search HTML files as a "soup" object

# Instructions 
1. Put all files in the same folder. The created html file will also be created in this folder. 
2. Run ``` python Execute_News.py``` in command line (or python Execute_Blog.py, etc) 

You can find the output as an html file ```Name_Date.html``` (e.g., TaipeiTimes_20210721) in the folder. 


Let me know what you think!
