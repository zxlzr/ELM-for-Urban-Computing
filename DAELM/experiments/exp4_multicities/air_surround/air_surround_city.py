# -*- coding: utf-8 -*-
import pymongo
import os
import sys
import string
import codecs
import time
ISOTIMEFORMAT='%Y-%m-%dT%XZ'
STEP = 1 
STATION = 'beijing'
TYPE = 'low'

#import math
#connect
#cities = ["苏州","南通","湖州","常州","盐城"]
#stations = ["环境监测监理中心","万寿西宫","美国大使馆","官园","定陵","东四","天坛","顺义新城","昌平镇"]  
#cities = ["廊坊","北京","北京","北京","北京","北京","北京","北京","北京"]
#stations = ["海淀区万柳","市环保局","供销社","离宫","市环保局","黑马集团"]  
cities = ["廊坊","承德","石家庄","保定","天津","唐山","张家口","秦皇岛","沧州","衡水","济南","大同","德州","滨州","东营"]

init_time = "2013-06-01T00:00:00Z"
final_time = "2014-10-31T00:00:00Z"


def get_records():
    conn = pymongo.Connection("10.214.0.147",27017)
    db = conn.Air
    collection = db.Cities


    record = [{}]*len(cities)
    for i in range(len(cities)):
        record[i]={}
        print i
        print cities[i]
        tmp_record = collection.find({"area":cities[i]},{"time_point":1,"pm2_5":1})
        for r in tmp_record:
            if r.has_key('time_point'):
                if r.has_key('pm2_5'):
                    record[i][r['time_point']] = r['pm2_5']
    return record

def get_time_list(station,mtype):
    ifile=codecs.open(u'../events/'+station+'_'+mtype+'.txt', 'r',"utf-8") 
    tmp_list = ifile.readlines()
    time_list = []
    for t in tmp_list:
        time_list.append(t.strip('\r\n')[0:19] + 'Z')
    return time_list

def pro_and_write_data(record,station,mtype):
    ofile=codecs.open(u'./'+station+'_'+mtype+'1.txt', 'w',"utf-8")

    m_result = [{}]*len(cities)
    for current_time in time_list:
        
        unix_current = time.mktime(time.strptime(current_time,ISOTIMEFORMAT))
        for time_iter in range(0,STEP):
            unix_tmp = unix_current-time_iter*3600
            tmp_time = time.strftime(ISOTIMEFORMAT,time.localtime(unix_tmp))
            print tmp_time

            for city_iter in range(len(cities)):
                m_result[city_iter]={}
                m_result[city_iter]["pm2_5"]=-1
                
                if record[city_iter].has_key(tmp_time) and record[city_iter][tmp_time] != 0:
                    m_result[city_iter]["pm2_5"] = record[city_iter][tmp_time]

            ofile.write(tmp_time)
            for city_iter in range(len(cities)):
                ofile.write(" %d"%(m_result[city_iter]["pm2_5"]))
            ofile.write("\r\n")

            
    ofile.close()

if __name__ == '__main__':
    print "Ready"
    record = get_records()
    time_list = get_time_list('beijing','low')
    pro_and_write_data(record,'beijing','low')
    time_list = get_time_list('beijing','increase')
    pro_and_write_data(record,'beijing','increase')
    time_list = get_time_list('beijing','decrease')
    pro_and_write_data(record,'beijing','decrease')
    time_list = get_time_list('beijing','high')
    pro_and_write_data(record,'beijing','high')










