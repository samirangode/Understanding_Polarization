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

        if th is not None and inside_personal_details:
            key = None
            if th.attrs["class"] == ["infobox-label"]:
                key = th.text
            td = tr.find("td")
            val = None
            if td is not None and td.attrs["class"] == ["infobox-data"]:
                val = td.text

            data[key] = val

    return data

df = pd.read_csv(r"E:\DOWNLOADS\POLARIZATION\congress_links_104_117.csv", header=None)
urls_list = df.iloc[:, 0].tolist()
labels = df.iloc[:, 1].tolist()

final_list = []
table_crawled = False # crawling personal details
print(urls_list[0])
for i,url in enumerate(urls_list):
    print(i)
    if i==457:
        continue
    try:
        result_content = requests.get(url)
    except:
        print("url: ", url, "didn't work")

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
    # data['Label'] = labels[i]
    subheader = None
    table_crawled = False
    for c in content.contents:
        if c != "\n":

            if c.name == "h2":
                header_name = c.text
                # strip [edit]
                header_name = header_name.split("[edit]")[0]
                subheader = None
                data[header_name] = ""

            if c.name == "p":
                if subheader is not None:
                    data[header_name][subheader] += "\n" + c.text
                else:
                    data[header_name] += "\n" + c.text


            if c.name=="ol" or c.name== "ul" or c.name == "li":
                data[header_name] += "\n" + c.text

            
            ## H3 was removed in order to consolidate subheader contents coming after h2. 
            # Now h3 subheader is skipped and rest of the body is stored. Refer Scot . L Fiterald

            # if c.name == "h3":
            #     subheader = c.text
            #     # strip [edit]
            #     subheader = subheader.split("[edit]")[0]
            #     if isinstance(data[header_name], str):
            #         data[header_name] = {}
            #     data[header_name][subheader] = ""

            if not table_crawled and c.name == "table" and c.attrs["class"] == ["infobox", "vcard"]:
                data["PersonalDetails"] = get_personal_details(c)
                table_crawled = True

    if "PersonalDetails" not in data:
        print("Personal details missing: ", url)

    final_list.append(data)

with open('PHASE_4.json', 'w') as fout:
    json.dump(final_list , fout)