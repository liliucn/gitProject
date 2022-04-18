import pandas as pd
import pymssql
import numpy as np
import matplotlib.pyplot as plt
import logging
'''
描述：动态生成建表语句，传表名和以逗号分隔的字段名，自增主键字段为autoID
'''
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

def shop_logging(name):
    logger = logging.getLogger()
    fh = logging.FileHandler('LOG/customer/'+__name__+'.log',encoding="utf-8",mode="a")
    formatter = logging.Formatter("%(asctime)s - %(name)s-%(levelname)s %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    logger.info(name)

def createTableDB(tableName,createSql):
    try:
        # region 创建表
        createSql = ' if exists (select * from dbo.sysobjects where id = object_id(\''+tableName+'\') and OBJECTPROPERTY(id, \'IsUserTable\') = 1)  DROP TABLE '+tableName+';  create table '+tableName+' ('+createSql+');'
        executeSql(createSql)
        print(createSql)
        # endregion
    except (OSError,TypeError) as reason:
        shop_logging('建表报错，错误的原因是:',str(reason))

#insert into Table
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
def birthCreateSql(sqlTemp,tablenameT):
    #一键生成建表语句
    # createSql='autoID,followUserId,groupId,name,call,gender,birthday,isLunarBirthday,title,qq,mobile,phone,fax,email,company,companyUrl,companyAddress,memo,vocation,channel,prefecture,fieldInfos,crmId,modifyTime,contactTime,createTime,lastFollowUserId,step,createUserId,wechat,wechats,emails,mobiles,storageTime,publicPondId,apiAdd,crmType,shareUserId,lastContactTime,stars,khhyflyj,khhyflej,sheng,shi,qx,dwxz,cp,remark1,remark2,remark3,remark4,remark5,remark6'
    tempL=sqlTemp.split(',')
    print(len(tempL))
    createSql = ' nvarchar(2000),'.join(tempL) + ' nvarchar(2000)'
    createSql=createSql.replace('autoID nvarchar(2000),','autoID int identity(1,1) not null PRIMARY key ,')
    createTableDB(tablenameT, createSql)

def main():
    dicTemp={'客户信息':{'tableName':'ec_dim_student','fieldStr':'autoID,followUserId,groupId,name,call,gender,birthday,isLunarBirthday,title,qq,mobile,phone,fax,email,company,companyUrl,companyAddress,memo,vocation,channel,prefecture,fieldInfos,crmId,modifyTime,contactTime,createTime,lastFollowUserId,step,createUserId,wechat,wechats,emails,mobiles,storageTime,publicPondId,apiAdd,crmType,shareUserId,lastContactTime,stars,khhyflyj,khhyflej,sheng,shi,qx,dwxz,cp,remark1,remark2,remark3,remark4,remark5,remark6'}
            ,'枚举信息':{'tableName':'ec_dim_class','fieldStr':'autoID,fieldId,paramId,parentParamId,paramName,sort,remark1,remark2,remark3,remark4,remark5,remark6'}
            }
    for dicT in dicTemp:
        if dicT != '':
            tableName = dicTemp[dicT]['tableName']
            fieldStr = dicTemp[dicT]['fieldStr']
            birthCreateSql(fieldStr,tableName)
main()
