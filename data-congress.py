import json
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request, urllib.parse, urllib.error


final_list = []
for i,url in enumerate(urls_list):
  print(i)
  try:
    result_content = requests.get(url)
  except:
    print("url didn't work", url, i)
  src = result_content.content
  # content = BeautifulSoup(src, 'lxml')ata
  stuff = BeautifulSoup(src)
  content = stuff.find("div", "mw-parser-output")
  name = stuff.find("h1")
  #name.text
  header_name = "Main"
  data = {}
  data[header_name] = ""
  data['Name'] = name.text
  data['Label'] = labels[i]
  subheader = None
  for c in content.contents[4:]:
      #print(c)
      if c != "\n":
  #         if c.name == "h3":
          if c.name == "p":
              if subheader is not None:
                  data[header_name][subheader] += "\n" + c.text
              else:
                  data[header_name] += "\n" + c.text
              
          if c.name == "h3":
              header_name = c.text
              subheader = None
              data[header_name] = ""
              
          if c.name == "h2":
              subheader = c.text
              if isinstance(data[header_name], str):
                  data[header_name] = {}
              data[header_name][subheader] = ""  
  final_list.append(data)


  with open('/content/drive/MyDrive/1-2/Deep-Learning/Project-data/Wiki-text/104_117_data.json', 'w') as fout:
    json.dump(final_list , fout)