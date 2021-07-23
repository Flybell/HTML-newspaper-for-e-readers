"""
Classes: Articles, Issues (Front page issue, Taiwan news issue)

Each issue consists of multiple articles.

General idea: After each issue object is generated,
the article objects of each issue are then generated and stored
as an attribute of the issue they belong to.

"""
import re #regular expression
from bs4 import BeautifulSoup #web parsing library
import io
import string

#--Beautiful Soup (B-soup)----------#

#make requests as a browser
import requests
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

def make_request(url): #create a soup
    """request HTML soup object from url via beautiful soup"""
    req = requests.get(url, headers)
    soup = BeautifulSoup (req.content, "html5lib")
    return soup

def create_soup(url):
    soup = make_request(url) #make soup of issue
    if soup:
        # check for forbidden sites
        # raise forbidden error
        return soup #check if website exists
    else:
        raise Exception("Invalid website")

def retrieve_date(soup):
    """get publication date"""
    r_date = soup.find("dc:date") #customize
    return r_date.string
#----------------------------------#

def find_article_urls(soup, base):
    """creates a list of article urls"""
    article_urls = []
    all_urls = soup.find_all(resource=re.compile(base)) #customize
    for item in all_urls:
        url= item.get('resource')  #customize
        if url:
            article_urls.append(url)
        else:
            raise Exception("Can't find article url")
    return article_urls

def create_article_objects(article_urls):
    """create article objects with article urls
       output: a list of article objects as an attribute"""
    articles = []
    for url in article_urls:
        a = Article(make_request(url))
        a.get_title()
        print(a.title) #show progress by printing title
        a.get_content()
        articles.append(a)
    return articles

class Article():
    def __init__(self, soup):
        self.title = ""  # article title
        self.content = []  # list of paragraphs
        self.ref = ""  # anchor reference
        self.soup = soup

    def get_title(self):
        """get title of article
        input is soup; output is a title string"""
        item = self.soup.find("h1") ##customize
        if item:
            self.title = item.string
            self.ref = self.title[1-3]
        else:
            raise Exception("Can't find the title.")

    def get_content(self):
        """collect the <p> of each article
        input: article soup; output: list of <p> """
        content_div = self.soup.find("div", "archives") #customize
        content = content_div.find_all("p") #customize
        for item in content:
            if item:
                self.content.append(str(item))
            else:
                raise Exception("Can't find this article.")
