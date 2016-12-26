from datetime import datetime
import MySQLdb


def getDBobject():
	db = MySQLdb.connect(host="localhost",user="root",passwd="9163",db="major")
	return db
 

date_map = dict()
tree = dict()
empty_list = list()
map_list = list()
	
def data_fetch():
	db = getDBobject()
	cursor = db.cursor()
	sql = "SELECT subject,lat,lon,name,date FROM disease ORDER BY date ASC;";
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
#	print map_list
	

def preprocess(node,l,r):
	if(l>r):
		return empty_list;
	
	if(l==r):	
		tree[node].append(map_list[l])
	#	print len(tree[node]) 
		return 
	
	preprocess(2*node,l,(l+r)/2)
	preprocess(1+2*node,1+(l+r)/2,r)

	if(len(tree[2*node])>len(tree[1+2*node])):
		tree[node].append(tree[2*node])
	else:
		tree[node].append(tree[1+2*node])
	print len(tree[node])
	
	
def query(node,l,r,p,q):
	
	if(p>q):
		return empty_list
	if(l>q or r<p):
		return empty_list
	
	if(l>=p and r<=q):
		return tree[node]
	
	L = query(2*node,l,(l+r)/2,p,q)
	R = query(1+2*node,1+(l+r)/2,r,p,q)
	
	if(len(L)>len(R)):
		return L
	else:
		return R
	

def segment_tree(from_date,to_date):
	data_fetch()
	for i in range(0,100000):
		tree[i] = list()
#	print map_list[0][4]
	
#	print from_date
	from_date =  str(from_date)
	to_date = str(to_date)
	format_date = "%Y-%m-%d"
	from_date = datetime.strptime(from_date,format_date).date()
	to_date = datetime.strptime(to_date,format_date).date()
	
	n = len(map_list)

	preprocess(1,0,n-1)
	for i in range(0,n):
		date_map[map_list[i][4]]=i
	print from_date
	print to_date
	left = date_map[from_date]
	right = date_map[to_date]
	print left
	print right
	print "Actual data"
	print query(1,0,n,left,right)
