import requests
from bs4 import BeautifulSoup
import csv
import os
import json
import datetime
URL_2="https://www.flipkart.com"
URL_1 = f"https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&page="
r = requests.get(URL_1+"1")
soup = BeautifulSoup(r.content, 'html5lib')
pages=soup.find('div',attrs={'class':"_1G0WLw"})
page_value=pages.find('span')
total_page=page_value.text.split()[-1]
product=[]
for j in range(1,int(2)):
    k=URL_1+str(j)
    r = requests.get(k)
    soup = BeautifulSoup(r.content, 'html5lib')
    content=soup.find_all('div',attrs={'class':'_75nlfW'})
    for i in content:
        total_dict={}
        name=i.find('div',attrs={'class':'KzDlHZ'})
        total_dict['NAME']=name.text
        print(name.text)
        price=i.find('div',attrs={'class':'Nx9bqj _4b5DiR'})
        print(price.text)
        link_a=i.find('a',attrs={'class':'CGtC98'})
        link=link_a.get('href')
        image_a=i.find('img',attrs={'class':'DByuf4'})
        img_=image_a.get('src')
        total_dict['IMAGE_LINK']=img_
        final_link=URL_2+link
        total_dict['VISIT_LINK']=final_link
        try:
            r_2 = requests.get(final_link)
            soup = BeautifulSoup(r_2.content, 'html5lib')
            specs=soup.find_all('div',attrs={'class':"GNDEQ-"})
            specs_={}
            review = {}
            review_ = soup.find_all('text', attrs={'class': '_2DdnFS'})
            review_d = soup.find_all('div', attrs={'class': 'NTiEl0'})
            print(review_,review_d)
            try:
                for i, j in zip(review_d, review_):
                    review[i.text.strip()] = j.text.strip()
                print(review)
                total_dict['REVIEW'] = review
            except:
                total_dict['REVIEW'] = {}
            for i in specs:
                specs_table=i.find('table',attrs={'class':'_0ZhAN9'})
                for i in specs_table.tbody.find_all('tr'):
                    p=i.find_all('td')
                    col_1=i.find_all('td',attrs={'class':'+fFi1w col col-3-12'})
                    col_2=i.find_all('td',attrs={'class':'Izz52n col col-9-12'})
                    for i,j in zip(col_1,col_2):
                        specs_[i.text]=j.text
                total_dict['SPECS']=specs_
        except:
            total_dict['SPECS']={}
        product.append(total_dict)
        
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")   
with open(f"{timestamp}.json", "w", encoding='utf-8') as f:
    json.dump(product, f, ensure_ascii=False, indent=4)

print(f"Scraping complete! Saved {len(product)} products.")


    

