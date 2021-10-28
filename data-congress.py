import json
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request, urllib.parse, urllib.error

def get_personal_details(c):
    data = {}

    inside_personal_details = False
    for tr in c.find_all("tr"):
        th = tr.find("th")
        if (th is not None and
                "class" in th.attrs and
                th.attrs["class"] == ["infobox-header"] and
                th.text == "Personal details"):
            inside_personal_details = True
            continue

        if (inside_personal_details and
                th is not None and
                th.attrs["class"] == ["infobox-header"] and
                th.text != "Personal details"):
            inside_personal_details = False

        if inside_personal_details:
            key = None
            if th.attrs["class"] == ["infobox-label"]:
                key = th.text
            td = tr.find("td")
            val = None
            if td is not None and td.attrs["class"] == ["infobox-data"]:
                val = td.text

            data[key] = val

    return data

df = pd.read_csv("104to117.csv", header=None)
urls_list = df.iloc[:, 0].tolist()
labels = df.iloc[:, 1].tolist()

final_list = []
table_crawled = False # crawling personal details
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
      if c != "\n":
  #         if c.name == "h3":
          if c.name == "p":
              if subheader is not None:
                  data[header_name][subheader] += "\n" + c.text
              else:
                  data[header_name] += "\n" + c.text

          if c.name == "h2":
              header_name = c.text
              subheader = None
              data[header_name] = ""

          if c.name == "h3":
              subheader = c.text
              if isinstance(data[header_name], str):
                  data[header_name] = {}
              data[header_name][subheader] = ""

          if not table_crawled and c.name == "table":
              data["PersonalDetails"] = get_personal_details(c)
              table_crawled = True

  final_list.append(data)


  with open('104_117_data_new.json', 'w') as fout:
    json.dump(final_list , fout)
