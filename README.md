# HTML newspaper for e-readers 
Crawls and scrapes a site or rss feed (news, magazine, blog, etc) for articles to compile into a lightly formatted .html file for conversion into PDF, EPUB, etc., by programs like Calibre. Personal use case: the .html file is loaded into Calibre to convert into a .MOBI file for Kindle and a PDF file for a large e-reader. 

Output: a compiled HTML file 
* Table of Contents (hyperlinked to article titles) 
* Date of issue 
* Articles (with a back to TOC hyperlink at the end of each article)
* Comments under a blog

Example output: see TaipeiTimes_20210721.html

# Applicability 
These scripts are highly specific to the publications they're targetting. They are thus not for general use, but are super easy to tweak.
* The Taipei Times folder (Execute_News,py, HTML_News.py, Class_News.py)  (http://www.taipeitimes.com/), focused on front page and Taiwan news sections
* The Philosopher's Cocoon folder (Execute_Blog.py, HTML_Blog.py, Class_Blog.py) (https://philosopherscocoon.typepad.com/), July archive, 30 posts with comments
* The Daily Nous folder (Execute_Blog.py, HTML_Blog.py, Class_Blog.py) (https://dailynous.com/2021/07/), July archive, 30 posts without comments

Other packages have been developed for magazines, etc, but will not be made available here for obvious reasons. 
The principles are the same, which will be explained in detail below. The user is encouraged to use and modify the scripts for their own purposes.

# The scripts and what they do
There are three Python scripts: 
* Execute (Execute_News.py, Execute_Blog.py, etc) 
* HTML writer (HTML_News.py, HTML_Blog.py, etc)
* Class file of objects (Class_News.py, Class_Blog.py, etc)

*Execute* is the main script. It uses the *Class* file to create objects of each issue (a collection of articles) and each article. It then sends these objects to the *HTML* writer to create and compile a basic formatted html file. A very simple three step process. 

I've added a ```#customize``` note behind each line that needs to be customized to the specific outlet. The key is to find the right HTML tag to retrieve the title of article, the content of the article (paragraph by paragraph), and the comments of blog articles. See the scripts for further documentation.

# External dependencies, or what the script needs to run 
* Beautiful Soup (https://pypi.org/project/beautifulsoup4/) to parse and search HTML files as a "soup" object. ```pip install beautifulsoup4``` 

# Instructions 
1. Put all files in the same folder. The created html file will also be created in this folder. 
2. Run ``` python Execute_News.py``` in command line (or python Execute_Blog.py, etc) 

You can find the output as an html file ```Name_Date.html``` (e.g., TaipeiTimes_20210721.html) in the folder. 


Let me know what you think!
