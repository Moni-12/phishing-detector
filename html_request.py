# import requests
# from lxml.html import fromstring
# r = requests.get('http://www.imdb.com/title/tt0108778/')
# tree = fromstring(r.content)
# print(tree.findtext('.//title'))
#
# u'Friends (TV Series 1994\u20132004) - IMDb'

import requests
from requests_html import HTMLSession

url = "https://www.amazon.com/"

try:
    session = HTMLSession()
    response = session.get(url)

except requests.exceptions.RequestException as e:
    print(e)

title = response.html.find('title')
print(title[0].text)