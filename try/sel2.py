from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.promedmail.org/")

k = driver.find_element_by_xpath("//div[@id = 'latest_list']")

while(1):
	cnt=0
	#for y in k.find_elements_by_tag_name("li"):
	#	f = y.find_element_by_tag_name("a")
	#	f.click()
	#time.sleep(2)			
	driver.find_element_by_partial_link_text("« prev").click()

	Listlinker = []
	Listlinker = driver.find_element_by_xpath("//div[@id = 'latest_list']/a")
	for prev in Listlinker:
		prev.click()
		break

#	if(y.text=="<< prev"):
#		f = x.find_element_by_tag_name("a")
#		print f.text
#		y.click()
	
	"""else:
		
		
		for x in y.find_elements_by_tag_name("li"):
			f = x.find_element_by_tag_name("a")
			#print f.text
			f.click()
	
			try:
				tex = driver.find_elements_by_xpath("//div[@id = 'preview']/p")[0].text
				val = driver.find_elements_by_xpath("//div[@id = 'preview']/p")[1].text
			except:
				print "hey " + f.text + " has been skipped for now find the fault in logic. Indexing fault "
			print tex
			print val
    #break
    """
