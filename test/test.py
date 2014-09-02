import unittest
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urlparse import urlparse

host = 'http://127.0.0.1:5000/'
valid_protocols = ['http', 'https']

if len(sys.argv) > 1 and sys.argv[1] == ('--host' or '-h'):
	host = sys.argv[2]

valid_link = ('http://docs.seleniumhq.org', 'Selenium - Web Browser Automation')

not_a_link = ('www.meetup.com/Selenium-Israel/', 'Selenium Israel (Tel Aviv-Yafo) - Meetup')

invalid_ids = [-1, 'doge']

class LinkShortenerTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def add_link(self, link):
		self.driver.get(host)
		text_box = self.driver.find_element_by_name('link')
		text_box.send_keys(link[0])
		text_box.submit()

	def test_submit_valid_link(self):
		self.add_link(valid_link)
		self.assertEqual(self.driver.current_url, host + 'newlink')

	def test_redirect_valid_link(self):
		self.add_link(valid_link)
		shortened_link = self.driver.find_element_by_partial_link_text('/l/')
		shortened_link.click()
		self.assertEqual(self.driver.title, valid_link[1])

	def test_submit_not_a_link(self):
		self.add_link(not_a_link)
		self.assertEqual(self.driver.current_url, host + 'error')

	def test_invalid_shortened_link(self):
		for index in invalid_ids:
			self.driver.get(host + 'l/' + str(index))
			message = self.driver.find_element_by_tag_name('p')
			self.assertEqual(message.text, 'There\'s nothing in here.')

if __name__ == '__main__':
	unittest.main()

