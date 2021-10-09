import requests
from bs4 import BeautifulSoup
import pandas as pd

result = requests.get("https://en.wikipedia.org/wiki/List_of_current_United_States_senators")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for table in soup.find_all('table'):
    for tbody in soup.find('tbody'):
         for tr in soup.find('tr'):
             for th in soup.find('th'):
                for span in soup.find_all('span'):
                    # for span in soup.find('span'):
                    #     for span in soup.find('span'):
                            a_tag = span.find('a')
                            if a_tag is not None and 'href' in a_tag.attrs:
                                if a_tag.attrs['href'] not in urls:              
                                    urls.append(a_tag.attrs['href'])
                                    # print(a_tag.attrs['href'])

print(urls)

cities = pd.DataFrame(urls)
cities.to_csv(r'C:\Users\supreethbare\Desktop\urls.csv',index = None, header=True)
