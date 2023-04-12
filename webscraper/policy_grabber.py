from urllib.request import Request, urlopen
import pandas as pd
import numpy as np

apps = pd.read_csv("./data.csv", nrows = 3)

for index, row in apps.iterrows(): 
    print(row['privacyPolicy'])
    url = Request(
        url = row['privacyPolicy'],
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)

#TODO: Change write to cvs to also have column headers and not split on the commas, get rid of duplicates in data, add these html results to data by appending to dataframe