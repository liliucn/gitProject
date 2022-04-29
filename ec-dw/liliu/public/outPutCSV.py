import sys
import logging
import pymysql
import csv
import codecs
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


conn = pymysql.connect(host='192.168.2.23', user='serveru', passwd='zjzyzjzy123456', db='a1',port=3306)
def from_mysql_get_all_info():
    conn = pymysql.connect(host='192.168.2.23', user='serveru', passwd='zjzyzjzy123456', db='a1',port=3306,charset='utf8mb4')
    cursor = conn.cursor()
    sql = 'select * from a3_tab_khywcx'
    cursor.execute(sql.encode('utf-8'))
    data = cursor.fetchall()
    conn.close()
    return data
def write_csv():
    data = from_mysql_get_all_info()
    filename = 'a3_tab_khywcx.csv'
    filePath='//192.168.2.100/files/data/'
    if os.path.exists(filePath) == False:
        os.makedirs(filePath)
    with open(filePath+filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        # f.write(codecs.BOM_UTF8)
        header_list = ['id', 'khid', 'khmc', 'level', 'sheng', 'shi', 'quxian', 'ywzt', 'yjfl', 'ejfl', 'sjfl',
                       'cp', 'xm', 'hkje', 'yjje', 'cjrq', 'barq', 'yxry', 'yxbm', 'yxjgid', 'yxjg', 'owner',
                       'BDry', 'xmjl', 'xmbh', 'htje', 'jxzt', 'jdrq', 'skdid']
        write.writerow(header_list)
        for item in data:
            write.writerow(item)

write_csv()