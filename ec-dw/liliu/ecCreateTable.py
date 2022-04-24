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

def createTableDB(tableNameTemp,tableName,createSql):
    try:
        # region 创建表
        createSql = ' if exists (select * from dbo.sysobjects where id = object_id(\''+tableName+'\') and OBJECTPROPERTY(id, \'IsUserTable\') = 1)  DROP TABLE '+tableName+';  create table '+tableName+' ('+createSql+'); -- '+tableNameTemp

        executeSql(createSql)
        print(createSql)
        # endregion
    except (OSError,TypeError) as reason:
        shop_logging('建表报错，错误的原因是:',str(reason))

def birthCreateSql(tableName_T,sqlTemp,tablenameT):
    #一键生成建表语句
    # createSql='autoID,followUserId,groupId,name,call,gender,birthday,isLunarBirthday,title,qq,mobile,phone,fax,email,company,companyUrl,companyAddress,memo,vocation,channel,prefecture,fieldInfos,crmId,modifyTime,contactTime,createTime,lastFollowUserId,step,createUserId,wechat,wechats,emails,mobiles,storageTime,publicPondId,apiAdd,crmType,shareUserId,lastContactTime,stars,khhyflyj,khhyflej,sheng,shi,qx,dwxz,cp,remark1,remark2,remark3,remark4,remark5,remark6'
    tempL=sqlTemp.split(',')
    # print(len(tempL))
    createSql = ' nvarchar(2000),'.join(tempL) + ' nvarchar(2000)'
    createSql=createSql.replace('autoID nvarchar(2000),','autoID int identity(1,1) not null PRIMARY key ,')
    createTableDB(tableName_T,tablenameT, createSql)

def main():

    dicTemp={
        '企业的自定义字段信息':{'tableName': 'EC_dim_customerAutoInfo',
                        'fieldStr': 'autoID,fieldGroupId,fieldGroupName,fieldGroupSort,fieldId,fieldName,fieldSort,filedType,category,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '企业的自定义字段信息_子表': {'tableName': 'EC_dim_customerAutoInfoChild',
                            'fieldStr': 'autoID,paramId,paramName,paramSort,parentID,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '企业联系人的自定义字段': {'tableName': 'EC_dim_customerContactAutoInfo',
                          'fieldStr': 'autoID,id,text,type,isMust,regex,level,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '企业联系人的自定义字段_子表': {'tableName': 'EC_dim_customerContactAutoInfoChild',
                         'fieldStr': 'autoID,paramId,paramName,paramchildNumber,parentID,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '组织架构-部门': {'tableName': 'ec_dim_orgdepts',
                      'fieldStr': 'autoID,deptId,deptName,parentDeptId,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '组织架构-人员': {'tableName': 'ec_dim_orgusers',
                      'fieldStr': 'autoID,userId,userName,deptId,title,status,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '客户标签管理-分组': {'tableName': 'ec_dim_cusLabelBaseInfosGroup',
                        'fieldStr': 'autoID,groupId,groupName,sort,type,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '客户标签管理-标签': {'tableName': 'ec_dim_cusLabelBaseInfosLabel',
                        'fieldStr': 'autoID,classId,className,sort,parentID,remark1,remark2,remark3,remark4,remark5,remark6'}
        , '枚举表-级联字段': {'tableName': 'ec_dim_enum',
                       'fieldStr': 'autoID,fieldId,paramId,parentParamId,paramName,sort,remark1,remark2,remark3,remark4,remark5,remark6'}

        # , '客户列表':{'tableName':'ec_dim_customer','fieldStr':'autoID,followUserId,groupId,name,call,gender,birthday,isLunarBirthday,title,qq,mobile,phone,fax,email,company,companyUrl,companyAddress,memo,vocation,channel,prefecture,crmId,modifyTime,contactTime,createTime,lastFollowUserId,step,createUserId,wechat,wechats,emails,mobiles,storageTime,publicPondId,apiAdd,crmType,shareUserId,lastContactTime,stars,khhyflyj,khhyflej,sheng,shi,qx,dwxz,cp,lastContactType,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'客户联系人信息':{'tableName':'ec_dim_customerContact','fieldStr':'autoID,id,crmId,corpid,createUserId,name,callName,title,mobile,mobileCode,phone,phoneCode,phoneExtension,qq,email,wechat,birthday,lunarBirthday,lunarLeap,memo,gender,createTime,updateTime,bumen,zhiwu,lxrcj,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'EC-客户资料-文件列表查询':{'tableName':'ec_dim_fileList','fieldStr':'autoID,crmId,folderId,createUserId,createUserName,path,id,name,size,updateTime,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'EC-客户资料-文件目录查询':{'tableName':'ec_dim_fileFolderList','fieldStr':'autoID,CrmFolderItem,crmId,createUserId,createUserName,id,name,size,updateTime,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'客户标签列表':{'tableName':'ec_dim_cusLabelList','fieldStr':'autoID,crmId,labelId,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'客户进展列表':{'tableName':'ec_dim_cusStageBaseInfos','fieldStr':'autoID,name,stage,status,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'客户头像':{'tableName':'ec_dim_cusImagesList','fieldStr':'autoID,crmId,face,name,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'客户轨迹':{'tableName':'ec_dim_cusTrajectoryBaseInfos','fieldStr':'autoID,levelOneID,levelOneName,TrajectoryID,TrajectoryName,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'查询客户轨迹':{'tableName':'ec_dim_cusTrajectory','fieldStr':'autoID,content,createTime,crmId,receiveUserIds,trajectoryId,trajectoryType,userId,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'删除客户':{'tableName':'ec_dim_customer_del','fieldStr':'autoID,crmId,delTime,id,remark1,remark2,remark3,remark4,remark5,remark6'}
        #  ,'查询任务':{'tableName':'ec_dim_taskList','fieldStr':'autoID,taskId,ruleId,title,noticeTime,endTime,createName,createUserId,exeName,exeId,exeNum,taskNum,detail,ruleType,taskType,remark1,remark2,remark3,remark4,remark5,remark6'}
        # ,'规则|任务类型':{'tableName':'ec_dim_kindType','fieldStr':'autoID,typeID,typeName,kindType,remark1,remark2,remark3,remark4,remark5,remark6'}
          }
    #执行createSql方法
    for dicT in dicTemp:
        if dicT != '':
            tableName_T = dicT
            tableName = dicTemp[dicT]['tableName']
            fieldStr = dicTemp[dicT]['fieldStr']
            birthCreateSql(tableName_T,fieldStr,tableName)
main()