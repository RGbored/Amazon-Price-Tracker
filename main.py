# Amazon product price tracker using Python

# importing libraries
import bs4 as bs
import sys
# import schedule
import time
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import winsound
frequency = 2500 # Set Frequency To 2500 Hertz
duration = 1000 # Set Duration To 1000 ms == 1 second


class Page(QWebEnginePage):

	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebEnginePage.__init__(self)
		self.html = ''
		self.loadFinished.connect(self._on_load_finished)
		self.load(QUrl(url))
		self.app.exec_()

	def _on_load_finished(self):
		self.html = self.toHtml(self.Callable)
		print('Load finished')

	def Callable(self, html_str):
		self.html = html_str
		self.app.quit()

def exact_url(url):
	index = url.find("B0")
	index = index + 10
	current_url = ""
	current_url = url[:index]
	return current_url
	

def mainprogram():
	url = "https://www.amazon.in/Logitech-MK295-Wireless-Keyboard-Mouse/dp/B08FMLQXN4/ref=sr_1_2_sspa?keywords=keyboard&qid=1637736259&s=electronics&sr=1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBWkFZN0ozUThUNEEmZW5jcnlwdGVkSWQ9QTA1MzI0ODYzR0dJOU5NSUUxUExCJmVuY3J5cHRlZEFkSWQ9QTA4MTQ5MjYzVENNUUY3QTJCREVPJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
	exacturl = exact_url(url) # main url to extract data
	page = Page(exacturl)
	soup = bs.BeautifulSoup(page.html, 'html.parser')
	# js_test = soup.find('span', id ='priceblock_ourprice')
	print(soup)
# 	if js_test is None:
# 		js_test = soup.find('span', id ='priceblock_dealprice')		
# 	str = ""
# 	for line in js_test.stripped_strings :
# 		str = line

# 	# convert to integer
# 	str = str.replace(", ", "")
# 	current_price = int(float(str))
# 	your_price = 600
# 	if current_price < your_price :
# 		print("Price decreased book now")
# 		winsound.Beep(frequency, duration)
# 	else:
# 		print("Price is high please wait for the best deal")
	
# def job():
# 	print("Tracking....")	
# 	mainprogram()

# # main code
# schedule.every(1).minutes.do(job)

# while True:
# 	schedule.run_pending()
# 	time.sleep(1)
