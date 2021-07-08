import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(r.text, "html.parser")
title = link.find_all('div', attrs={'class': 'contentDiv'})
header = []
data_list = []
for i in title:
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            td_list = []
            if td_index.find_all('th'):
                header = [th_index.get_text() for th_index in td_index.find_all('th')]
            print(list(td_index.find_all('td')))
            for index, trd_index in enumerate(list(td_index.find_all('td'))):
                print(trd_index.get_text().lstrip('   '), index)
                if index == 0:
                    td_list.append(trd_index.get_text().lstrip('   '))
                else:
                    td_list.append(float(trd_index.get_text().lstrip('   ').replace(',', '.')))
            # td_list = [trd_index.get_text().lstrip('   ') for trd_index in td_index.find_all('td')]
            data_list.append(td_list)
print(data_list)

df = pd.DataFrame(data_list, columns=header)
df.to_csv('CursBNR.xls', header=header)