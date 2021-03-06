#-*- coding: utf-8 -*-
import pymongo
import datetime

ADDRESS = "10.214.0.147"
PORT = 27017
ISOTIMEFORMAT='%Y-%m-%dT%XZ'
cities = ['北京','廊坊','天津','保定','沧州','张家口','唐山','承德','衡水','德州','石家庄','南充','滨州','大同','秦皇岛','东营','济南']
#cities = ['上海','太仓','昆山','吴江','常熟','苏州','嘉兴','南通','张家港','无锡']
def get_city_history(city_name):
	result = {}
	conn = pymongo.Connection(ADDRESS,PORT)
	db = conn['Air']
	collection = db['Cities']
	air_list = collection.find({'area':city_name})
	for a in air_list:
		result[a['time_point']] = a['aqi']
	return result

def get_time_list():
	result = []
	start_time = datetime.datetime(2013,1,1,0,0,0)
	an_hour = datetime.timedelta(hours=1)
	end_time = datetime.datetime(2014,12,31,23,59,59)
	while start_time<=end_time:
		result.append(start_time.strftime(ISOTIMEFORMAT))
		start_time+=an_hour
	return result

if __name__ == '__main__':
	time_list = get_time_list()
	city_history = []
	for current_city in cities:
		city_history.append(get_city_history(current_city))
	result = []
	for t in time_list:
		tmp=t+" "
		for c in range(len(cities)):
			if city_history[c].has_key(t):
				#tmp+=cities[c]+":"+str(city_history[c][t])+" "
				tmp+=str(city_history[c][t])+" "
			else:
				#tmp+=cities[c]+":"+"-1"+" "
				tmp+="-1"+" "
		tmp+='\r\n'
		result.append(tmp)
	ofile = open('city_history1_withname.txt','w')
	ofile.writelines(result)
	ofile.close()

