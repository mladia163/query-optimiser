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
L = dict()
M = dict()

for x in k.find_elements_by_tag_name("li"):
    f = x.find_element_by_tag_name("a")
    f.click()
    time.sleep(2)
    tex = driver.find_elements_by_xpath("//div[@id = 'preview']/p")[0].text
    data = driver.find_elements_by_xpath("//div[@id = 'preview']/p")[1].text
    
    tex = tex.split()
    #print tex  
    date = tex[2]
    dtime = tex[3]
    subject = ""
    for_subject=0
    for i in tex:
    	for_subject+=1
    	if(i=='-' or i[0]=='('):
    		break
    	if(for_subject>6):
    		subject = subject + i + " "
    		
    archive_number = tex[len(tex)-1]
    
    print date + dtime + " " + subject + " " + archive_number
    locations = geodict_lib.find_locations_in_text(data)
    
    M.clear()
    L.clear()
    
    for i in locations:
    	temp = i['found_tokens'][0]
    	types = temp['type']
    	name = temp['matched_string']
    	lat = (str)(temp['lat'])
    	lon = (str)(temp['lon'])
    	L[name] = L.get(name,0) + 1
    	M[name] = [types,lat,lon]
    	
    for i in L:
    	I = M.get(i)
    	name = i
    	types = I[0]
    	lat = I[1]
    	lon = I[1]
    	counter = (str)(L[i])
    	print counter + " " + name + " " + types + " " + lat + " " + lon
	
	time.sleep(2)
	cnt+=1
	if(cnt==2):
		break
	
   
"""  
a = '"mayank1"'
b = '"ladia"'
"""
#sql_command = """INSERT INTO try1 VALUES ("""+a+""", """+b+""");"""
"""print sql_command        

cursor.execute(sql_command)
"""
db.commit()
cursor.close()
db.close()

