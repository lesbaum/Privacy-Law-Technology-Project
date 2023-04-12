from urllib.request import Request, urlopen
import pandas as pd
import numpy as np

apps = pd.read_excel("./testTestPrivacy.xlsx")
privacyPolicies = []

for index, row in apps.iterrows():
    print(row['privacyPolicy'])
    print(row['Raw Privacy Policy'])
    if (not str(row["Raw Privacy Policy"]) == 'nan'): 
        privacyPolicies.append(row["Raw Privacy Policy"])
        continue
    if row["title"] == "Pix123: Color by Number Games" or row['title'] == 'Univerzoom 3D Discover Scales': 
        privacyPolicies.append("Illegal excel character")
        continue
    url = Request(
            url = row['privacyPolicy'],
            headers={'User-Agent': 'Mozilla/5.0'}
        )
    try:
        page = urlopen(url)
    except:
        privacyPolicies.append("Couldn't access link")
        continue
    html_bytes = page.read()
    try:
        html = html_bytes.decode("utf-8")
    except: 
        html = "Couldn't decode"
    privacyPolicies.append(html)

apps["Raw Privacy Policy"] = privacyPolicies

apps.to_excel("./testTestPrivacy.xlsx")