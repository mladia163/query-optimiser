from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;


def test():
	print('testing')
	browser = webdriver.Firefox()
	browser.get("http://www.facebook.com/mladia163")
	WebElement email = driver.findElement(By.id("email"));
	email.sendKeys("your@email.here");

	
	xpath = "//div[@id = 'contentCol']"
	for i in browser.find_elements_by_xpath(xpath):
		print i.text
	
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
