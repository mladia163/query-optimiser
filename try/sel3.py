import geodict_lib
from selenium import webdriver
import MySQLdb
import time

db = MySQLdb.connect (host = "localhost",
                              user = "root",
                              passwd = "9163",
                              db = "major")               
cursor = db.cursor()
driver = webdriver.Firefox()
driver.get("http://www.promedmail.org/")

k = driver.find_element_by_xpath("//div[@id = 'latest_list']/ul")

cnt=0

for x in k.find_elements_by_tag_name("li"):
	time.sleep(1)
    f = x.find_element_by_tag_name("a")
    f.click()
    time.sleep(2)
    try:
        tex = driver.find_elements_by_xpath("//div[@id = 'preview']/p")[0].text
        data = driver.find_elements_by_xpath("//div[@id = 'preview']/p")[1].text
   		cnt+=1
    except:
        print "hey has been skipped for now find the fault in logic. Indexing fault"
	print tex + " : "
	print "himani"
	locations = geodict_lib.find_locations_in_text(data)
	print locations
	time.sleep(2)
	if(cnt==5):
		break
   

