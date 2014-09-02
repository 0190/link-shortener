import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urlparse import urlparse

host = "http://127.0.0.1:5000/"
valid_protocols = ['http', 'https']

if len(sys.argv) > 1 and sys.argv[1] == ('--host' or '-h'):
	host = sys.argv[2]

links = {'twitter.com': 'Twitter', 'http://google.com': 'Google', \
		 'http://docs.seleniumhq.org': 'Selenium - Web Browser Automation', \
		 'www.meetup.com/Selenium-Israel/': 'Selenium Israel (Tel Aviv-Yafo) - Meetup', \
		 'http://notapageatall.co.il/': 'Problem loading page', \
		 'ftp://someftp': 'No matter'}

driver = webdriver.Firefox()

for link in links:
	driver.get(host)
	text_box = driver.find_element_by_name('link')
	text_box.send_keys(link)
	text_box.submit()

	if driver.current_url == host + 'newlink':
		shortened_link = driver.find_element_by_partial_link_text('/l/')
		shortened_link.click()
		assert links[link] == driver.title
	else:
		assert driver.current_url == host + 'error'
		parsed_link = urlparse(link)
		assert parsed_link.scheme not in valid_protocols or not parsed_link.netloc

