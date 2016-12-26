import datetime 



def convert_date(dstr):
	temp = dstr.split("-")
#	temp1 = [map(int,x) for x in temp]
	temp[0] = (int)(temp[0])
	temp[1] = (int)(temp[1])
	temp[2] = (int)(temp[2])	
	date = datetime.date(temp[0],temp[1],temp[2])
	return date


print convert_date("2016-12-12")
