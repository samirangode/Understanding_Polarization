import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request, urllib.parse, urllib.error


result = requests.get("https://en.wikipedia.org/wiki/116th_United_States_Congress")
src = result.content
soup = BeautifulSoup(src, 'lxml')
urls = []
for dd in soup.find_all("dd"):
    if "(R)" in dd.text or "(D)" in dd.text:
        a_tag = dd.find('a')
        # print(dd.text)
        for a_tag in dd.find_all("a"):
            if a_tag is not None and 'href' in a_tag.attrs:
                if "/wiki/"in a_tag.attrs['href']:
                    temp=a_tag.attrs['href']
                    a_tag.attrs['href']="https://en.wikipedia.org/"+a_tag.attrs['href']
                    urls.append(a_tag.attrs['href'])
                    if(len(urls)==100):
                        print(urls)
                        senators = pd.DataFrame(urls)
                        senators.to_csv(r'C:\Users\supreethbare\Desktop\senators116.csv',index = None, header=False)
      



