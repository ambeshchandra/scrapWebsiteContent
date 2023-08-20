#install all these requirements
#pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
#url = "https://www.test.com"
url = 'https://www.test.com'

headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response = requests.get(url, headers=headers, timeout=10)
# step 1 get the html
#r =requests.get(url)
htmlContent=response.content
#print(htmlContent)

# step 2 parse the html

soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)




# step 3 HTML tree travesal 
title = soup.title
# commonly used types of Objects:
#print(type(title)) # 1. Tag
#print(type(title.string)) # 2. NavigableString
#print(type(soup)) # 3. BeautifulSoup
# 4. Comment

 
#print (soup.find_all("table", class_="table table-striped table-bordered widget-header table-responsive"))
#print (soup.find_all("table" ))



