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
#----------------------------------#


class Article():
    def __init__(self, soup):
        self.title = ""
        self.content = [] #list of paragraphs
        self.soup = soup #the searchable html file from B-soup

    def get_title(self):
        """get title of article
        input is soup
        output is a title string"""
        item = self.soup.find("h1") ##customize
        if item:
            self.title = item.string #retrieves string of title tag
        else:
            raise Exception("Can't find the title.")

    def get_content(self):
        """collect the <p> of each article
        input: article soup
        output: list of <p> """
        content_div = self.soup.find("div", "archives") #customize
        content = content_div.find_all("p") #customize
        for item in content:
            if item:
                self.content.append(str(item))
            else:
                raise Exception("Can't find this article.")

class Issue():
    def __init__(self):
        self.rss = "https://www.taipeitimes.com/xml/index.rss" #RSS feed
        self.soup = "" #soup of the issue object
        self.issuedate = "" #publication date of the issue
        #below are about the articles of the issue
        self.ar_list = [] #list of article urls
        self.articles = [] #list of article objects

    def find_article_urls(self):
        """creates a list of article urls"""
        if self.soup:  #check if website exists
            all_urls = self.soup.find_all(resource=re.compile(self.ar_base)) #customize
            for item in all_urls:
                url = item.get('resource') #customize
                if url:
                    self.ar_list.append(url)
        else:
            print("Invalid website")

    def retrieve_date(self):
        """get publication date"""
        r_date = self.soup.find("dc:date") #customize
        self.issuedate = r_date.string

    def compile_articles(self):
        """main exe: get date, get article urls, create article objects """
        self.soup = make_request(self.rss) #make soup of issue
        self.retrieve_date() #get date
        self.find_article_urls() #get list of article urls
        self.create_article_objects() #make list of article objects

    def create_article_objects(self):
        """create article objects with article urls
           output: a list of article objects as an attribute"""
        for url in self.ar_list: #from list of article urls
            a = Article(make_request(url))
            a.get_title() #create title atribute of article
            print(a.title) #show progress by printing title
            a.get_content() #create content attribute of article
            self.articles.append(a) #make list


class Front(Issue):
    """Front page news"""
    def __init__(self):
        #ar_base is used to find article urls
        self.ar_base = "https://www.taipeitimes.com/News/front/archives/"
        self.filename = "Today's Headlines"
        super().__init__()

class Taiwan(Issue):
    """Taiwan news"""
    def __init__(self):
        self.ar_base = "https://www.taipeitimes.com/News/taiwan/archives/"
        self.filename = "Today's Taiwan News"
        super().__init__()
