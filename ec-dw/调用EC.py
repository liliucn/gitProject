import requests
import json
import pymssql
import hashlib
import time
import graphviz
# region https://www.cnblogs.com/PPWEI/p/11805247.html
# import warnings
# warnings.filterwarnings("ignore")
import requests
import os
import time
import pandas as pd
import json
import warnings
import logging
warnings.filterwarnings("ignore")
requests.adapters.DEFAULT_RETRIES = 20
# logging.FileHandler(filename='LOG/'+__name__+'.log',encoding="utf-8",mode="a")
# logging.basicConfig(filename='LOG/'+__name__+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level = logging.DEBUG,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p',encoding="utf-8",mode="a")

def shop_logging(name):
    logger = logging.getLogger()
    fh = logging.FileHandler('LOG/customer/'+__name__+'.log',encoding="utf-8",mode="a")
    formatter = logging.Formatter("%(asctime)s - %(name)s-%(levelname)s %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    logger.info(name)

# region 数据库相关操作 【增、删、改、查】
def executeSql(str):
    conn = pymssql.connect(host="192.168.2.29",database="DW",user="sa",password="Sql2008R@")
    cur = conn.cursor()
    cur.execute(str)
    conn.commit()
    cur.close()
    conn.close()

def selectSql(strdat):
    conn = pymssql.connect(host="192.168.2.29", database = "DW",user = "sa", password = "Sql2008R@")
    cur = conn.cursor()
    cur.execute(strdat)
    result = cur.fetchall()
    # print(str(result[1]).encode('latin-1').decode('gbk'))
    df = pd.DataFrame(list(result))
    conn.commit()
    cur.close()
    conn.close()
    return df

def executeMany(insertSql,data):
    conn = pymssql.connect(host="192.168.2.29",database="DW",user="sa",password="Sql2008R@")
    cur = conn.cursor()
    cur.executemany(insertSql,tuple(data))
    conn.commit()
    cur.close()
    conn.close()
# endregion 数据库相关操作

#region 动态建表，动态入库的语句
# 执行写入数据的操作
def writeDBChildTable(tableName,fieldList,data,fieldLength):
    try:
        # region删除表记录
        delSql="delete from "+ tableName
        executeSql(delSql)
        # endregion

        # region 新增记录
        tempFormat=str('%s,'*fieldLength)[:-1]
        insertSql = "insert into  "+tableName+"  ("+fieldList+") values ("+tempFormat+")"
        executeMany(insertSql,data)
        # endregion
    except (OSError,TypeError) as reason:
        shop_logging('第一个网站，解析报错，错误的原因是:',str(reason))

# 执行建表的操作
def createTableDB(tableName,createSql):
    try:
        # region 创建表
        createSql = ' if exists (select * from dbo.sysobjects where id = object_id(\''+tableName+'\') and OBJECTPROPERTY(id, \'IsUserTable\') = 1)  DROP TABLE '+tableName+';  create table '+tableName+' ('+createSql+');'
        executeSql(createSql)
        # endregion
    except (OSError,TypeError) as reason:
        shop_logging('第一个网站，解析报错，错误的原因是:',str(reason))
#endregion

#region 动态解析json、动态建表、动态入库
def jieXiData(tablename,dataTemp):
    try:
        resultContent=dataTemp #去掉空格
        dicContent=eval(str(resultContent))
        # print(dicContent)
        if 'list' in dicContent['data']: #获取所有的客户
            dicListData=dicContent['data']['list']
        elif 'fieldParams' in dicContent['data']: #获取级联的字段
            dicListData=dicContent['data']['fieldParams']
        elif tablename=='depts' : #获取组织机构的部门
            dicListData = dicContent['data'][tablename]
            tablename='EC_dim_depts'
        elif tablename=='users' : #获取组织机构的人员
            dicListData = dicContent['data'][tablename]
            tablename='EC_dim_users'
        elif 'fieldParam' in dicContent['data'][0]:# 获取 企业的自定义字段信息 【没完，需要自定义组装数据集】
            dicListData=dict(dicContent['data'][0])
            print(dicListData['fieldParam'])
            daTe = [[len(t), t] for t in dicListData]
            daTe.sort(key=lambda x: x[0], reverse=True)  # 降序排列
            keyLengthMax = daTe.keys()
            print(daTe)
        elif tablename=='channelSource' : #获取来源信息
            dicListData = dicContent['data']
            tablename='EC_dim_channelSource'
        elif tablename=='customStages' : #获取客户进展信息
            dicListData = dicContent['data']
            tablename='EC_dim_customStages'
        elif tablename=='pubicPond' : #获取业务组信息
            dicListData = dicContent['data']
            tablename='EC_dim_pubicPond'
        elif tablename=='productGroup' : #获取产品分组
            dicListData = dicContent['data']
            tablename='EC_dim_productGroup'
        elif tablename=='ec_apipush' : #查询主动推送接口
            dicListData = dicContent['data']
            tablename='ec_apipush'
        elif tablename=='role' : #获取角色信息
            dicListData = dicContent['data']
            tablename='EC_dim_role'
        createAndInsertTable(dicListData, tablename)
    except (OSError, TypeError) as reason:
        shop_logging('jieXiData:报错'+str(reason))
#endregion

#region 公共方法 执行建表和新增数据
def createAndInsertTable(dicListData, tablename):
    try:
        # 取出返回list key最长的 取出最全的key当作字段名
        daTe = [[len(t), t] for t in dicListData]
        daTe.sort(key=lambda x: x[0], reverse=True)  # 降序排列
        keyLengthMax = daTe[0][1].keys()
        # dicListDataList=dict(dicContent['data']['list'][0])
        # region 拼接insert into 和 create table 语句的前边字段部分
        # fieldTemp=['custom_'+str(i) for i in list(dicListDataList.keys())]
        fieldTemp = [str(i) for i in list(keyLengthMax)]  # 取出所有的key，当作字段
        fieldList = ','.join(fieldTemp)  # 组装-字段列表 拼接insert语句的sql
        createSql = ' nvarchar(2000),'.join(fieldTemp) + ' nvarchar(2000)'  # 拼接create table语句的sql
        # endregion
        listTReturn = []
        m = 0
        for rowT in dicListData:
            m = m + 1
            temp = []
            # region 循环所有的键
            # for j in rowT: #循环所有的键
            for j in keyLengthMax:  # 循环所有的键
                tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                temp.append(str(tempValue))
            listTReturn.append(tuple(temp))
            # endregion
        if len(fieldTemp) == len(listTReturn[0]):
            print(len(fieldTemp), len(listTReturn[0]), fieldList)
            # 将网页的内容解析入库；所有字段
            createTableDB(tablename, createSql) # 取消新建表
            writeDBChildTable(tablename, fieldList, listTReturn, len(listTReturn[0]))
    except (OSError, TypeError) as reason:
        shop_logging('CreateAndInsertTable:报错'+str(reason))
#endregion

#region 获取签名，各接口都需要
def get_sign(app_id, app_secret, timestamp):
    str = 'appId=' + app_id + '&appSecret=' + app_secret + '&timeStamp=' + timestamp
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest().upper()
#endregion

#region main方法
if __name__ == '__main__':
    #第一步：获取签名  https://open.workec.com/newdoc/doc/1hzrmo5Kq
    timestamp = int(round(time.time() * 1000))
    app_id = '763422286010122240'
    app_secret = 'vGUltdoYbnaE2iwi4Xf'
    sign = get_sign(app_id, app_secret, str(timestamp))

    heads = {'Content-type': 'application/json',
             'X-Ec-Cid': '15912663',
             'X-Ec-Sign': sign,
             'X-Ec-TimeStamp': str(timestamp)
             }

    #第二步：拼接header，请求头信息  https://open.workec.com/newdoc/doc/zKMGwg1NN
    dicTemp={'客户列表':{'tableName':'ec_customer','requestStyle':'post','interfaceUrl':'https://open.workec.com/v2/customer/queryList','params':{"pageNo": "1","pageSize": "200"}}
            # ,'字典表-级联字段':{'tableName':'ec_dim_JiLian','requestStyle':'post','interfaceUrl':'https://open.workec.com/v2/customer/getCasCadeFieldMapping','params':{"fieldIds": [81655955,81654764,81656622,81619239,81656624,81656625,81649962]}} #,"lastId":2282208
             ,'组织架构-部门':{'tableName':'depts','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/org/struct/info','params':''}
             ,'组织架构-人员':{'tableName':'users','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/org/struct/info','params':''}
            # ,'来源信息':{'tableName':'channelSource','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/customer/getChannelSource','params':''}
            # ,'客户进展信息':{'tableName':'customStages','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/config/getStages','params':''}
            # ,'公海池信息':{'tableName':'pubicPond','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/config/getPubicPond','params':''}
            # ,'获取产品分组':{'tableName':'productGroup','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/sales/getProductGroupList','params':''}
            # ,'查询主动推送接口':{'tableName':'ec_apipush','requestStyle':'post','interfaceUrl':'https://open.workec.com/v2/apipush/getApiPush','params':{"beginTime": "2022-03-04 00:00:00","endTime": "2022-03-24 17:11:11","onlyError": True,"pageSize": 1000}}
            # ,'获取角色':{'tableName':'role','requestStyle':'post','interfaceUrl':'https://open.workec.com/v2/role/list','params':{"userId" : 111}}
            # ,'企业的自定义字段信息':{'tableName':'EC_dim_customerAutoInfo','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/config/getFieldMapping','params':''}
            # ,'企业联系人的自定义字段':{'tableName':'EC_dim_customerContactAutoInfo','requestStyle':'get','interfaceUrl':'https://open.workec.com/v2/config/getBookFieldMapping','params':''}
           }
    for dicT in dicTemp:
        # for childT in dicTemp[dicT]:
        if dicT!='':
            tableName=dicTemp[dicT]['tableName']
            interfaceUrl=dicTemp[dicT]['interfaceUrl']
            params=dicTemp[dicT]['params']
            print(tableName,interfaceUrl,params)
            params = json.dumps(params)
            requeststyle=dicTemp[dicT]['requestStyle']

            if requeststyle=='get':
                returnResponse=requests.get(url=interfaceUrl,headers=heads,data=params)
            else:
                returnResponse=requests.post(url=interfaceUrl,headers=heads,data=params)
            data=returnResponse.json()
            jieXiData(tableName,data)

    #获取级联字段-数据："fieldIds": [81654764]  参数：{"fieldIds":[81649962]}
    #客户--客户行业分类：81655955
    #客户--省市县：81654764
    #客户--单位性质：81656622
    #客户--产品：81619239
    #客户联系人--部门：81656624
    #客户联系人--职务：81656625
    #客户联系人--联系人层级：81649962
#endregion
