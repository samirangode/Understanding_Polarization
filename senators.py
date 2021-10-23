import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request, urllib.parse, urllib.error

TERM=[ 
        "https://en.wikipedia.org/wiki/104th_United_States_Congress",
        "https://en.wikipedia.org/wiki/105th_United_States_Congress",
        "https://en.wikipedia.org/wiki/106th_United_States_Congress",
        "https://en.wikipedia.org/wiki/107th_United_States_Congress",
        "https://en.wikipedia.org/wiki/108th_United_States_Congress",
        "https://en.wikipedia.org/wiki/109th_United_States_Congress",
        "https://en.wikipedia.org/wiki/110th_United_States_Congress",
        "https://en.wikipedia.org/wiki/111th_United_States_Congress",
        "https://en.wikipedia.org/wiki/112th_United_States_Congress",
        "https://en.wikipedia.org/wiki/113th_United_States_Congress",
        "https://en.wikipedia.org/wiki/114th_United_States_Congress",
        "https://en.wikipedia.org/wiki/115th_United_States_Congress",
        "https://en.wikipedia.org/wiki/116th_United_States_Congress",
        "https://en.wikipedia.org/wiki/117th_United_States_Congress"
]
urls = []

for i,j in enumerate(TERM):
    result = requests.get(j)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    for dd in soup.find_all("dd"):
        if "(R)" in dd.text or "(D)" in dd.text:
            a_tag = dd.find('a')
            # print(dd.text)
            for a_tag in dd.find_all("a"):
                if a_tag is not None and 'href' in a_tag.attrs:
                    if "/wiki/"in a_tag.attrs['href']:
                        temp=a_tag.attrs['href']
                        if "district" not in a_tag.attrs["href"]:
                            if "https://en.wikipedia.org" not in a_tag.attrs["href"]:
                                a_tag.attrs['href']="https://en.wikipedia.org/"+a_tag.attrs['href']
                                if a_tag.attrs['href'] not in str(urls):
                                    if "(R)" in dd.text:
                                        urls.append((a_tag.attrs['href'],"R"))
                                    elif "(D)" in dd.text:
                                        urls.append((a_tag.attrs['href'],"D"))


senators = pd.DataFrame(urls)
senators.to_csv(r'C:\Users\supreethbare\Desktop\104to117.csv',index = None, header=False)
                    
                    


