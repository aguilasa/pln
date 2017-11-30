import urllib2
from bs4 import BeautifulSoup
from summarizer import FrequencySummarizer
from html import HtmlGenerator
import webbrowser


def get_only_text(url):
    """ 
     return the title and the text of the article
     at the specified url
    """
    page = urllib2.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, 'html.parser')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text


feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'), 'lxml')
to_summarize = map(lambda p: p.text, feed.find_all('guid'))

h = HtmlGenerator()
l = []
fs = FrequencySummarizer()
for article_url in to_summarize[:4]:
    d = []
    title, text = get_only_text(article_url)
    print '----------------------------------'
    print title
    t = []
    for s in fs.summarize(text, 2):
        print '*', s
        t.append(s)
    d.append(title)
    d.append(t)
    l.append(d)
h.set_data(l)
h.write()
webbrowser.open("index.html")