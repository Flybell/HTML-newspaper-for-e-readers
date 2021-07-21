"""
Classes: Blog, Post

Each blog consists of multiple posts.

General idea: After each blog object is generated,
the post objects of each issue are then generated and stored
as an attribute in the blog object.

"""
import re #regular expression
from bs4 import BeautifulSoup #web parsing library
import io
import string
from datetime import date #get dates
from HTML_Blog import * #html writer

#------- BEAUTIFUL SOUP----------#
#pretend to be a browser
import requests
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

#create a soup
def make_request(url):
    """request HTML soup object from url via beautiful soup"""
    req = requests.get(url, headers)
    soup = BeautifulSoup (req.content, "html5lib")
    return soup
#----------------------------------#

class Blog():
    def __init__(self):
        self.posts = [] #list of post objects
        self.post_urls = [] #list of post urls
        self.seed_url = "https://philosopherscocoon.typepad.com/blog/2021/07/index.html" #customize
        self.ar_base = "blog/2021/07/" #customize
        self.soup = ""
        self.retrievedate = date.today().strftime("%Y/%m/%d")

    def create_posts(self):
        """ creates a list of posts"""
        for ar_url in self.post_urls:
            ar_soup = make_request(ar_url) #create soup
            if ar_soup:
                a = Post(ar_soup)
                a.get_title()
                a.get_content()
                a.get_comments()
                self.posts.append(a)
                print("Downloading article... "+ str(a.title)) #display
            else:
                raise Exception("Can't find this article.")
        #self.issue = posts

    def get_article_urls(self): #find urls in soup
        """finds url of posts based on a part of URL string.
        input: criteria string, set limit to num of posts
        output: a list of URLs, eg [URL1, URL2, URL3] """
        all_urls = self.soup.find_all("h3", limit=30) #customize
        for item in all_urls:
            post = item.a.get('href')
            if post:
                self.post_urls.append(post)
            else:
                raise Exception("Error: can't find this article.")

    def grab_content(self):
        """scrapes the site to create post objects"""
        self.soup = make_request(self.seed_url) #use seed url to make html object
        if self.soup:  #check if website exists
            self.get_article_urls() #get post links on the page
            self.create_posts() #create postobjects
        else:
            raise Exception("Can't find website.")
#--------------------------------------------------------------------------#

class Post():
    def __init__(self, soup):
        self.title = ""
        self.content = []
        self.comments = []
        self.soup = soup

    def get_title(self):
        """get title of article based on article soup
        input is soup; output is a string"""
        item = self.soup.find("h3", attrs={"class": "entry-header"}) #customize
        if item:
            self.title= item.string #retrieves string of title tag

    def get_content(self):
        """get all the paragraphs of each post
        input: post soup; output: list of <p> """
        item = self.soup.find("div", attrs={"class": "entry-body"}) #customize
        content = item.find_all("p") #customize
        for item in content:
            if item:
                self.content.append(str(item))

    def get_comments(self):
        """get all the comments under each post
           input: post soup
           output: list of <p> """
        item = self.soup.find("div", attrs={"id": "all-comments"}) #customize
        content = item.find_all("p") #customize
        for item in content:
            if item:
                self.comments.append(str(item))
