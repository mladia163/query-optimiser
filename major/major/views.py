from django.shortcuts import render
import MySQLdb
import json
import time
from date_range import *
from dateparser import parse
from kdtree import *
from nearest_neighbors import *

def getDBobject():
	db = MySQLdb.connect(host="localhost",user="root",passwd="9163",db="major")
	return db
	
def index(request):
	start_time = time.clock()
	db = getDBobject()
	cursor = db.cursor()
	sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
	cursor.execute(sql)
	rows = cursor.fetchall()
	sql = "SELECT name,lat,lon FROM disease;"
	cursor.execute(sql)
	map_val = cursor.fetchall()
	row_count = cursor.rowcount
	map_list = list()

	for i in xrange(0,row_count):	
		map_list.append(list(map_val[i]))
	for i in xrange(0,row_count):
		map_list[i][0] = str(map_list[i][0])
		map_list[i][1] = float(map_list[i][1])
		map_list[i][2] = float(map_list[i][2])

	end_time = time.clock()
	time_taken = end_time-start_time
	print map_list
	return render(request,'index.html',{'rows':rows,'map_val':map_list,'time_taken':time_taken})
	
	
def kd_tree(request):
	if request.method == "GET":
		lat = request.GET.get("lati")
		lon = request.GET.get("long")
		lat = float(lat)
		lon = float(lon)
		data = [lat,lon]
		ans = kdtree(data)
		time_taken = ans[1]
		print ans
		if ans != 987654321:
			db = getDBobject()
			cursor = db.cursor()
			sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
			cursor.execute(sql)
			rows = cursor.fetchall()
			map_list = ans[0]
			print map_list
			return render(request,'kdtree.html',{'rows':rows,'map_val':map_list,'time_taken':time_taken})
		else:
			db = getDBobject()
			cursor = db.cursor()
			sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
			cursor.execute(sql)
			rows = cursor.fetchall()
			sql = "SELECT name,lat,lon FROM disease;"
			cursor.execute(sql)
			map_val = cursor.fetchall()
			row_count = cursor.rowcount
			map_list = list()

			for i in xrange(0,row_count):	
				map_list.append(list(map_val[i]))
			for i in xrange(0,row_count):
				map_list[i][0] = str(map_list[i][0])
				map_list[i][1] = float(map_list[i][1])
				map_list[i][2] = float(map_list[i][2])

#			print map_list	
			return render(request,'kdtree.html',{'rows':rows,'map_val':map_list,'time_taken':time_taken})			
			
			
			
def nearest_neighbors(request):
	if request.method == "GET":
		ans = nearest()
		time_taken = ans[1]
		map_list = ans[0]

		db = getDBobject()
		cursor = db.cursor()
		sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		
		return render(request,'kdtree.html',{'rows':rows,'map_val':map_list,'time_taken':time_taken})
		
def disease_select(request):
	if request.method == "GET":
		db = getDBobject()
		cursor = db.cursor()
		start_time = time.clock()
		values = request.GET.getlist("diseases")
		tree = request.GET.get("tree")
		print tree
		print values[0]
		sql = "SELECT name,lat,lon FROM disease WHERE subject IN (";
		temp = ""
		for i in values:
			temp = temp + "'"+ i + "',"
		temp = temp[:-1]
		
		print temp
		sql = sql + temp + ");"
		
		print sql
		
		cursor.execute(sql)
		map_val = cursor.fetchall()
		row_count = cursor.rowcount
		map_list = list()
		
		for i in xrange(0,row_count):
			map_list.append(list(map_val[i]))
		for i in xrange(0,row_count):
			map_list[i][0] = str(map_list[i][0])
			map_list[i][1] = float(map_list[i][1])
			map_list[i][2] = float(map_list[i][2])
		end_time = time.clock()
		time_taken = end_time-start_time
		return render(request,'disease_select.html',{'values':values,'map_val':map_list,'time_taken':time_taken})
	else:
		db = getDBobject()
		cursor = db.cursor()
		sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		return render(request,'index.html',{'rows':rows})
		
		
		
		
def date_range(request):
	if request.method=="GET":
		db = getDBobject()
		cursor = db.cursor()
		from_date = request.GET.get("from")
		to_date = request.GET.get("to") 

#		from_date = dateparser.date(from_date)
#		to_date = dateparser.date(to_date)
		time_taken = 0
#		print from_date[0]
#		print "mayank ladia"
		segment_tree(from_date,to_date)
		sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		return render(request,'date_range.html',{'rows':rows,'time_taken':time_taken})
		
	else:
		db = getDBobject()
		cursor = db.cursor()
		sql = "SELECT DISTINCT(subject) AS Diseases FROM disease;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		return render(request,'index.html',{'rows':rows})
	
