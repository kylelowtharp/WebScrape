#Kyle Lowtharp
#MMA web scrape project



from lxml import html
import lxml.html
from lxml.cssselect import CSSSelector
import requests
url = 'http://www.fightmetric.com/fighter-details/33a331684283900f'
r = html.fromstring(requests.get(url).text)

for row in r.xpath('//h2/span')[:1]: 
	fighter = row.cssselect('span')[0] 


for row in r.xpath('//h2/span')[1:]:
	record = row.cssselect('span')[0]

print(fighter.text)
print(record.text)



