from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def test():
	print('testing')
	browser = webdriver.Firefox()
	browser.get("http://www.promedmail.org")
	
	
	xpath = '//*[@id="latest_list"]/ul'
	for i in browser.find_elements_by_xpath(xpath):
		print i.click()
		xpath = '//*[@id="preview"]'
		for j in browser.find_elements_by_xpath(xpath):
			print j.text
		break
	
	"""
	alerts = browser.find_elements_by_xpath('/html/body/div[1]/div[4]/div[1]/div[1]')
	
	for alert in alerts:
		alert.getAttribute("id"); 
		print alert.text
	""""""		data = alert.get_attribute("id")
		print data
		if data=="tabs":
			print alert.text
	#	else :
	#		print "mayank"
	
"""
	#browser.close()
test()
