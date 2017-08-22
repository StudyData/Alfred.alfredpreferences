import urllib2, alfred, urllib
from bs4 import BeautifulSoup
url = "http://oj.leetcode.com/problems/"

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()
dom = BeautifulSoup(data)
tds = dom.find_all('td')
possbility = []
count = 0
urls = []
title  = []

for td in tds:
    if '\n' not in  td.contents:
        if count==0:
            for t in td.children:
                title.append(str(unicode(t.contents[0])))
            urls.append("http://oj.leetcode.com"+ str(unicode(td.a['href'])))
            count += 1
        elif count == 2:
            possbility.append(str(unicode(td.contents[0])))
            count = 0
        else:
            count += 1

theQuery = u'{query}'
theQuery = urllib.quote_plus(theQuery)
i = 0
indexes = []
result = []
for t in title:
    if theQuery in t.lower():
        indexes.append(i)
    i += 1

for ix in indexes:
    item = alfred.Item({'uid':1, 'arg':urls[ix]}, title[ix], possbility[ix], ('icon', {'type':'png'}))
    result.append(item)

xml = alfred.xml(result)
alfred.write(xml)
