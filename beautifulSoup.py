import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://www.fightmetric.com/fighter-details/fd55393021a8c255').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
tables = soup.find_all('li')




