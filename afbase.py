# -*- coding:utf-8 -*-

import psycopg2
import time


data_date = time.strftime('%Y%m%d')
# data_date = '20230630'

f_data = open('dailydata/stockdata' + data_date + '.csv', 'r')
content = f_data.readlines()[1:]
f_data.close()
print('importing. data date: ' + data_date)

conn = psycopg2.connect(database='af', user='postgres', host='localhost', port='5432')

f_error = open('dailyerror/stockerror' + data_date + '.csv', 'w')
f_error.writelines('code,tradenum,tradesize,high,low,ori,des,ttm,size,name,market\n')
idx = 0
for each in content:
	if 'nan' in each:
		f_error.writelines(each)
	else:
		alist = each.split(',')
		insert_sql = 'INSERT INTO day (code,tradenum,tradesize,high,low,ori,des,ttm,size,name,market,date) values (' + ','.join(alist[:9]) +",'"+ alist[9] + "','" + alist[10][:-1] + "','" + data_date +"');"
		try:
			cur = conn.cursor()
			cur.execute(insert_sql)
			conn.commit()
			cur.close()
			idx = idx + 1
		except psycopg2.errors.InFailedSqlTransaction as ee:
			# print(each)
			f_error.writelines(each)
f_error.close()
conn.close()
print('import finished. data aboard: ' + str(idx) + '/' + str(len(content)) + '.')
