# import bs4 as bs
# import urllib.request

# sauce = urllib.request.urlopen('http://www.fightmetric.com/fighter-details/fd55393021a8c255').read()
# soup = bs.BeautifulSoup(sauce, 'lxml')
# # tables = soup.find_all('li')
# link_soup = ('<li class="b-list__box-list-item b-list__box-list-item_type_block">')
# link_soup.find_all("li, class_=b-list__box-list-item b-list__box-list-item_type_block")
# print(link_soup)



from bs4 import BeautifulSoup
import urllib.request

source = urliib.request.urlopen('http://www.fightmetric.com/fighter-details/fd55393021a8c255').read()
soup = BeautifulSoup(aource, 'lxml')
print(source)