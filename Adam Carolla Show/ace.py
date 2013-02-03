import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import os
import time

username = 'getiton@gmail.com'
password = 'gottogetitonnoichoicebuttogetitonmandategetiton'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'login_email' : username, 'login_password' : password})
opener.open('https://my.libsyn.com/index', login_data)
resp = opener.open('http://theadamcarollashow.libsyn.com/podcast')

soup = BeautifulSoup(resp.read())
soup = soup.find(id="archives_text")
scrape = []
download_links = []

for archive_link in soup.find_all('a'):
    link = 'http://theadamcarollashow.libsyn.com' + archive_link.get('href')
    
    if len(link.split('/')) > 5:
        scrape.append(link)

for scrape_link in scrape:
    load = opener.open(scrape_link)
    soup = BeautifulSoup(load.read())

    print "Downloading %s" %scrape_link
    
    for download_link in soup.find_all('a'):
        if download_link.parent.name == 'li':
            url = download_link.get('href')
            filename = url.split('/')[-1]
            print "Downloading %s..." %filename
            urllib.urlretrieve (url, filename)
            time.sleep(10)
            
    time.sleep(30)               