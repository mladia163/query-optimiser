import MySQLdb
import time
from sklearn.neighbors import NearestNeighbors
import numpy as np


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
	



def nearest():
	fetch_data()
	data_points = list()
	
	for key,value in dict_lat_lon.iteritems():
		arr = [key[0],key[1]]
		data_points.append(arr)
	print data_points
	X = np.array(data_points)
	start_time = time.clock()
	nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X)
	distances, indices = nbrs.kneighbors(X)
	end_time = time.clock()
	time_taken = end_time-start_time
	ans = list()
	for i in range(0,10):
		name = dict_lat_lon[data_points[indices[3][i]][0],data_points[indices[3][i]][1]]
		if len(name) != 0:
			ans.append(disease_lat_lon[name[0]][0])
	
	return [ans,time_taken]
 
