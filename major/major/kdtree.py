import MySQLdb
import time


map_list = list()
dict_lat_lon = dict()
disease_lat_lon = dict()

def getDBobject():
	db = MySQLdb.connect(host="localhost",user="root",passwd="9163",db="major")
	return db

def fetch_data():
	db = getDBobject()
	cursor = db.cursor()
	sql = "SELECT subject,lat,lon,name FROM disease;"
	cursor.execute(sql)
	map_val = cursor.fetchall()
	row_count = cursor.rowcount
	
	
	for i in xrange(0,row_count):
		map_list.append(list(map_val[i]))
	for i in xrange(0,row_count):
		map_list[i][0] = str(map_list[i][0])
		map_list[i][1] = float(map_list[i][1])
		map_list[i][2] = float(map_list[i][2])
		map_list[i][3] = str(map_list[i][3])
		
	for i in xrange(0,row_count):
		dict_lat_lon[map_list[i][1],map_list[i][2]] = [map_list[i][3]]
		disease_lat_lon[map_list[i][3]] = list()
	
	for i in range(0,row_count):
		temp = list()
		for j in range(0,4):
			temp.append(map_list[i][j])
		disease_lat_lon[map_list[i][3]].append(temp)
	

class Node:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.data = value
	
class Tree:
	def createnode(self,data):
		lat = float(data[0])
		lon = float(data[1])
		temp = [lat,lon]
		return Node(temp)
	
	def insert(self,node,data,depth):
		if node is None:
			return self.createnode(data)
		
		temp = (depth)%2
		
		if data[temp]<node.data[temp]:
			node.left = self.insert(node.left,data,depth+1)
		else:
			node.right = self.insert(node.right,data,depth+1)
		
		return node
	
	
	def search(self,node,data,depth):
		if node is None:
			return False
		
		if node.data == data:
			return True
			
		temp = (depth)%2
	
		if data[temp]<node.data[temp]:
			return search(node.left,data,depth+1)
		
		return search(node.right,data,depth+1)
		
def kdtree(data):
	fetch_data()
	root = None
	Kd = Tree()
	
	for key,value in dict_lat_lon.iteritems():
		if root == None:
			root = Kd.createnode(data)
		else:
			Kd.insert(root,key,0)

#	print type(data[0])
	
	start_time = time.clock()
	present = Kd.search(root,data,0)
	end_time = time.clock()
	time_taken = end_time - start_time
	
	if present==True:
		name = dict_lat_lon[data[0],data[1]][0]
		print name
		return [disease_lat_lon[name],time_taken]
	else:
		return [int(987654321),time_taken]
			
 
