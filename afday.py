# -*- coding:utf-8 -*-

import akshare as ak
import pandas as pd
import time


def main():
	print('Link Start!')
	print('--'*6)

	global stock_data
	stock_data = []

	sh_data = ak.stock_sh_a_spot_em()
	da_merge(sh_data, 'sh')
	print('sh data fetched.')
	sz_data = ak.stock_sz_a_spot_em()
	da_merge(sz_data, 'sz')
	print('sz data fetched.')
	bj_data = ak.stock_bj_a_spot_em()
	da_merge(bj_data, 'bj')
	print('bj data fetched.')
	print('total data length: ' + str(len(stock_data)))
	print('--' * 6)

	csv_gen(stock_data)
	print('Link Logout.')


def da_merge(st_data, market):
	for i in range(len(st_data['名称'])):
		stock_istance = {}
		stock_istance['code'] = str(st_data['代码'][i])
		stock_istance['tradenum'] = str(st_data['成交量'][i])
		stock_istance['tradesize'] = str(st_data['成交额'][i])
		stock_istance['high'] = str(st_data['最高'][i])
		stock_istance['low'] = str(st_data['最低'][i])
		stock_istance['ori'] = str(st_data['今开'][i])
		stock_istance['des'] = str(st_data['最新价'][i])
		stock_istance['ttm'] = str(st_data['市盈率-动态'][i])
		stock_istance['size'] = str(st_data['流通市值'][i])
		stock_istance['name'] = str(st_data['名称'][i])
		stock_istance['market'] = market
		stock_data.append(stock_istance)
	return 0


def csv_gen(s_data):
	f_database = open('dailydata/stockdata' + time.strftime('%Y%m%d')+'.csv', 'w')
	f_database.writelines('code,tradenum,tradesize,high,low,ori,des,ttm,size,name,market\n')
	for i in range(len(s_data)):
		alist = []
		alist.append(str(s_data[i]['code']))
		alist.append(str(s_data[i]['tradenum']))
		alist.append(str(s_data[i]['tradesize']))
		alist.append(str(s_data[i]['high']))
		alist.append(str(s_data[i]['low']))
		alist.append(str(s_data[i]['ori']))
		alist.append(str(s_data[i]['des']))
		alist.append(str(s_data[i]['ttm']))
		alist.append(str(s_data[i]['size']))
		alist.append(str(s_data[i]['name']))
		alist.append(str(s_data[i]['market']))
		f_database.writelines(','.join(alist) + '\n')
	f_database.close()
	print('data csv recorded.')
	print('--' * 6)
	return 0


if __name__ == '__main__':
	main()
