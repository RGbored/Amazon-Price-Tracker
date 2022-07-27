from bs4 import BeautifulSoup
from csv import writer
import requests
from urllib.parse import urlparse
import urllib
from urllib.request import urlopen
url = "https://www.amazon.in/Logitech-MK295-Wireless-Keyboard-Mouse/dp/B08FMLQXN4/ref=sr_1_2_sspa?keywords=keyboard&qid=1637736259&s=electronics&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBWkFZN0ozUThUNEEmZW5jcnlwdGVkSWQ9QTA1MzI0ODYzR0dJOU5NSUUxUExCJmVuY3J5cHRlZEFkSWQ9QTA4MTQ5MjYzVENNUUY3QTJCREVPJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
# soup.prettify()
# js_test = soup.find('span', class ='a-price-whole')
js_test = soup.find("span", { "class" : "a-price-whole" })
# print(soup)
if js_test!=None:
    print(js_test.text)
List=['Price', 'Price']
print(js_test)
if js_test !=None:
    List.append(js_test.text)
with open("C:\\Users\\rgbor\\Documents\\c++\\Amazon_Price_Tracker\\prices.csv", 'a') as f_object:
    writer_object = writer(f_object)
  
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)
  
    #Close the file object
    f_object.close()
print(soup.select_one("span[id  =priceblock_ourprice]"))
if js_test is None:
    js_test = soup.find('span', id ='priceblock_dealprice')		
str = ""
for line in js_test.stripped_strings :
    str = line
# convert to integer
str = str.replace(",", "")
current_price = int(float(str))
your_price = 600
print(current_price)
