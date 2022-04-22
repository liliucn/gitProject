import hashlib
import json
import logging
import time
import warnings

import pandas as pd
import pymssql
# region https://www.cnblogs.com/PPWEI/p/11805247.html
# import warnings
# warnings.filterwarnings("ignore")
import requests

warnings.filterwarnings("ignore")
requests.adapters.DEFAULT_RETRIES = 20


# logging.FileHandler(filename='LOG/'+__name__+'.log',encoding="utf-8",mode="a")
# logging.basicConfig(filename='LOG/'+__name__+'.log',format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level = logging.DEBUG,filemode='a',datefmt='%Y-%m-%d%I:%M:%S %p',encoding="utf-8",mode="a")

def shop_logging(name):
    logger = logging.getLogger()
    fh = logging.FileHandler('LOG/customer/' + __name__ + '.log', encoding="utf-8", mode="a")
    formatter = logging.Formatter("%(asctime)s - %(name)s-%(levelname)s %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    logger.info(name)


# region 数据库相关操作 【增、删、改、查】
def executeSql(str):
    conn = pymssql.connect(host="192.168.2.29", database="DW", user="sa", password="Sql2008R@")
    cur = conn.cursor()
    cur.execute(str)
    conn.commit()
    cur.close()
    conn.close()


def selectSql(strdat):
    conn = pymssql.connect(host="192.168.2.29", database="DW", user="sa", password="Sql2008R@")
    cur = conn.cursor()
    cur.execute(strdat)
    result = cur.fetchall()
    # print(str(result[1]).encode('latin-1').decode('gbk'))
    df = pd.DataFrame(list(result))
    conn.commit()
    cur.close()
    conn.close()
    return df


def executeMany(insertSql, data):
    conn = pymssql.connect(host="192.168.2.29", database="DW", user="sa", password="Sql2008R@")
    cur = conn.cursor()
    cur.executemany(insertSql, tuple(data))
    conn.commit()
    cur.close()
    conn.close()


# endregion 数据库相关操作

#region 获取数据
def getJilianData():
    sqlSel='select distinct fieldID from ec_dim_customerAutoInfo ' \
           ' union all' \
           ' select distinct id from ec_dim_customerContactAutoInfo;'
    dataT=selectSql(sqlSel)
    return list(dataT[0])
#endregion

# region 动态建表，动态入库的语句
# 执行写入数据的操作
def writeDBChildTable(tableName, fieldList, data, fieldLength):
    try:
        # region删除表记录
        if tableName=='EC_dim_customerAutoInfo': #先删除主表，再删除子表
            delSql="delete from "+ tableName+" ; delete from EC_dim_customerAutoInfoChild; ";
            executeSql(delSql)
        if tableName=='EC_dim_customerContactAutoInfo':#先删除主表，再删除子表
            delSql="delete from "+ tableName+" ; delete from EC_dim_customerContactAutoInfoChild; ";
            executeSql(delSql)
        if tableName=='ec_dim_cusLabelBaseInfosGroup':#先删除主表，再删除子表
            delSql="delete from "+ tableName+" ; delete from ec_dim_cusLabelBaseInfosLabel; ";
            executeSql(delSql)
        if tableName=='ec_dim_enum' and isFirst==1:
            delSql = "delete from " + tableName;
            executeSql(delSql)
        if tableName=='ec_dim_enum' and isFirst!=1:
            print('只有第一次执行删除');
        else:#没主子表时，只删除当前表表
            delSql="delete from "+ tableName;
            executeSql(delSql)

        # endregion

        # region 新增记录
        tempFormat = str('%s,' * fieldLength)[:-1]
        insertSql = " insert into  " + tableName + "  (" + fieldList + ") values (" + tempFormat + ")"
        # print(insertSql)
        executeMany(insertSql, data)
        # endregion
    except (OSError, TypeError) as reason:
        shop_logging('第一个网站，解析报错，错误的原因是:', str(reason))


# endregion

# region 动态解析json、动态建表、动态入库
def jieXiData(tablename, dataTemp):
    try:
        resultContent = dataTemp  # 去掉空格
        dicContent = eval(str(resultContent))
        if 'EC_dim_customerAutoInfo' in tablename:  # 企业的自定义字段信息
            dicListData = dicContent['data']
        if 'EC_dim_customerContactAutoInfo' in tablename:  # 企业联系人的自定义字段
            dicListData = dicContent['data']
        elif 'ec_dim_enum' in tablename: #获取级联的字段
            dicListData=dicContent['data']['fieldParams']
            global hasNextPage
            global lastId
            hasNextPage=dicContent['data']['nextPageDTO']['hasNextPage']
            lastId=dicContent['data']['nextPageDTO']['nextLastId']
            print(hasNextPage,lastId)
        elif 'depts' in tablename: #获取组织机构的部门
            dicListData = dicContent['data']['depts']
        elif 'users' in tablename:#获取组织机构的人员
            dicListData = dicContent['data']['users']
        elif 'ec_dim_cusLabelBaseInfosGroup' in tablename:#客户标签管理-分组
            # print(dicContent['data'])
            dicListData = dicContent['data']
        elif 'ec_dim_cusStageBaseInfos' in tablename:  # 获取客户进展信息
            # print(dicContent['data'])
            dicListData = dicContent['data']

        # elif 'fieldParam' in dicContent['data'][0]:# 获取 企业的自定义字段信息 【没完，需要自定义组装数据集】
        #     dicListData=dict(dicContent['data'][0])
        #     print(dicListData['fieldParam'])
        #     daTe = [[len(t), t] for t in dicListData]
        #     daTe.sort(key=lambda x: x[0], reverse=True)  # 降序排列
        #     keyLengthMax = daTe.keys()
        #     print(daTe)
        # print(dicListData)
        createAndInsertTable(dicListData, tablename)
    except (OSError, TypeError) as reason:
        shop_logging('jieXiData:报错' + str(reason))


# endregion

# region 公共方法 执行建表和新增数据
def createAndInsertTable(dicListData, tablename):
    try:
        tableNameChild=''
        fieldListChild=''
        childTempList=[]
        listTReturn = []

        # 取出返回list key最长的 取出最全的key当作字段名
        daTe = [[len(t), t] for t in dicListData]
        daTe.sort(key=lambda x: x[0], reverse=True)  # 降序排列
        keyLengthMax = daTe[0][1].keys()
        # dicListDataList=dict(dicContent['data']['list'][0])
        # region 拼接insert into 语句的前边字段部分
        # fieldTemp=['custom_'+str(i) for i in list(dicListDataList.keys())]
        fieldTemp = [str(i) for i in list(keyLengthMax)]  # 取出所有的key，当作字段
        if 'EC_dim_customerAutoInfo' in tablename:  # 企业的自定义字段信息 接口  【有子表】
            fieldTemp.remove('fieldParam')
            tableNameChild='EC_dim_customerAutoInfoChild'
            fieldListChild='paramId,paramName,paramSort,parentID'
        if 'EC_dim_customerContactAutoInfo' in tablename:  # 企业联系人的自定义字段 接口 【有子表】
            fieldTemp.remove('params')
            tableNameChild='EC_dim_customerContactAutoInfoChild'
            fieldListChild='paramId,paramName,paramchildNumber,parentID'
        if 'ec_dim_cusLabelBaseInfosGroup' in tablename:  # 客户标签管理-分组 【有子表】
            fieldTemp.remove('list')
            tableNameChild='ec_dim_cusLabelBaseInfosLabel'
            fieldListChild='classId,className,sort,parentID'
        fieldList = ','.join(fieldTemp)  # 组装-字段列表 拼接insert语句的sql
        # print(fieldList)
        # endregion
        m = 0
        for rowT in dicListData:
            m = m + 1
            temp = []
            # region 循环所有的键
            # for j in rowT: #循环所有的键
            for j in keyLengthMax:  # 循环所有的键
                #region 1、企业的自定义字段信息 接口 2个表
                if 'EC_dim_customerAutoInfo' in tablename: #企业的自定义字段信息-主表信息
                    tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                    if j!='fieldParam':
                        temp.append(str(tempValue))
                    if isinstance(rowT[j], (list)) and j=='fieldParam' and len(rowT[j])>0: #用户自定义信息
                        for childTemp in rowT[j]: ##企业的自定义字段信息-子表信息
                            tempC=[]
                            tempC.append(str(childTemp['paramId']))
                            tempC.append(childTemp['paramName'])
                            tempC.append(str(childTemp['paramSort']))
                            tempC.append(str(rowT['fieldId']))
                            childTempList.append(tuple(tempC))
                #endregion

                #region 2、企业联系人的自定义字段信息 接口 2个表
                if 'EC_dim_customerContactAutoInfo' in tablename: #企业联系人的自定义字段信息-主表信息
                    tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                    if j!='params':
                        temp.append(str(tempValue))
                    if isinstance(rowT[j], (list)) and j=='params' and len(rowT[j])>0: #用户自定义信息
                        for childTemp in rowT[j]: ##企业的自定义字段信息-子表信息
                            tempC=[]
                            tempC.append(str(childTemp['id']))
                            tempC.append(childTemp['name'])
                            tempC.append(str(childTemp['childNumber']))
                            tempC.append(str(rowT['id']))
                            childTempList.append(tuple(tempC))
                #endregion

                #region 3、级联 接口 1个表
                if 'ec_dim_enum' in tablename:
                    tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                    temp.append(str(tempValue))
                #endregion

                #region 4、组织架构-部门|人员 2个表、一个组织、一个人员
                if 'ec_dim_org' in tablename:
                    tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                    temp.append(str(tempValue))
                #endregion

                #region 5、客户标签管理 - 分组 2个表
                if 'ec_dim_cusLabelBaseInfosGroup' in tablename:  # 客户标签管理-分组
                    tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                    if j != 'list':
                        temp.append(str(tempValue))
                    if isinstance(rowT[j], (list)) and j == 'list' and len(rowT[j]) > 0:  # 用户自定义信息
                        for childTemp in rowT[j]:  ##企业的自定义字段信息-子表信息
                            tempC = []
                            tempC.append(str(childTemp['classId']))
                            tempC.append(childTemp['className'])
                            tempC.append(str(childTemp['sort']))
                            tempC.append(str(rowT['groupId']))
                            childTempList.append(tuple(tempC))
                #endregion

                #region 6、获取客户进展信息 1个表
                if 'ec_dim_cusStageBaseInfos' in tablename:
                    tempValue = str(rowT[j]) if j in rowT else ''  # 判断当前的key，在不是当前的list里面，如果不在，则赋空值
                    temp.append(str(tempValue))
                #endregion

            listTReturn.append(tuple(temp))
            # endregion
        # print(len(fieldTemp),len(listTReturn[0]))
        if len(fieldTemp) == len(listTReturn[0]):
            print(len(fieldTemp), len(listTReturn[0]), fieldList)
            # 将网页的内容解析入库；所有字段
            writeDBChildTable(tablename, fieldList, listTReturn, len(listTReturn[0]))
            if tableNameChild!='':
                writeDBChildTable(tableNameChild, fieldListChild, childTempList, len(childTempList[0]))
    except (OSError, TypeError) as reason:
        shop_logging('CreateAndInsertTable:报错' + str(reason))


# endregion

# region 获取签名，各接口都需要
def get_sign(app_id, app_secret, timestamp):
    str = 'appId=' + app_id + '&appSecret=' + app_secret + '&timeStamp=' + timestamp
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest().upper()
# endregion

# region main方法
isContinue=True
if __name__ == '__main__':
    # 第一步：获取签名  https://open.workec.com/newdoc/doc/1hzrmo5Kq
    timestamp = int(round(time.time() * 1000))
    app_id = '763422286010122240'
    app_secret = 'vGUltdoYbnaE2iwi4Xf'
    sign = get_sign(app_id, app_secret, str(timestamp))

    heads = {
        'Content-type': 'application/json',
        'X-Ec-Cid': '15912663',
        'X-Ec-Sign': sign,
        'X-Ec-TimeStamp': str(timestamp)
    }

    # 第二步：拼接header，请求头信息  https://open.workec.com/newdoc/doc/zKMGwg1NN
    dicTemp = {
            '企业的自定义字段信息': {'tableName': 'EC_dim_customerAutoInfo', 'requestStyle': 'get',
                             'interfaceUrl': 'https://open.workec.com/v2/config/getFieldMapping', 'params': '','IsXunHuan':'否'}
            ,'企业联系人的自定义字段': {'tableName': 'EC_dim_customerContactAutoInfo', 'requestStyle': 'get',
                              'interfaceUrl': 'https://open.workec.com/v2/config/getBookFieldMapping', 'params': '','IsXunHuan':'否'}
            ,'组织架构-部门': {'tableName': 'ec_dim_orgdepts', 'requestStyle': 'get',
                          'interfaceUrl': 'https://open.workec.com/v2/org/struct/info', 'params': '','IsXunHuan':'否'}
            ,'组织架构-人员': {'tableName': 'ec_dim_orgusers', 'requestStyle': 'get',
                          'interfaceUrl': 'https://open.workec.com/v2/org/struct/info', 'params': '','IsXunHuan':'否'}
            ,'客户标签管理-分组': {'tableName': 'ec_dim_cusLabelBaseInfosGroup', 'requestStyle': 'post',
                            'interfaceUrl': 'https://open.workec.com/v2/label/getLabelInfo', 'params': '','IsXunHuan':'否'}
            ,'客户进展列表': {'tableName': 'ec_dim_cusStageBaseInfos', 'requestStyle': 'get',
                     'interfaceUrl': 'https://open.workec.com/v2/config/getStages', 'params': '','IsXunHuan':'否'}
            ,'客户枚举相关字段': {'tableName': 'ec_dim_enum', 'requestStyle': 'post',
                            'interfaceUrl': 'https://open.workec.com/v2/customer/getCasCadeFieldMapping', 'params': {
                                       },'IsXunHuan':'是'} # "fieldIds": [81655955, 81654764, 81656622, 81619239, 81656624, 81656625, 81649962] #完
            # ,'客户列表': {'tableName': 'ec_dim_customer', 'requestStyle': 'post',
            #            'interfaceUrl': 'https://open.workec.com/v2/customer/queryList',
            #            'params': {"pageNo": "1", "pageSize": "200"}}
            # , '客户联系人信息': {'tableName': 'ec_dim_customerContact', 'requestStyle': 'post',
            #               'interfaceUrl': 'https://open.workec.com/v2/contactbook/list',
            #               'params': {"crmId": 5625884449, "optUserId": 17640187}}
            # , '客户资料-文件列表查询': {'tableName': 'ec_dim_fileList', 'requestStyle': 'get',
            #                   'interfaceUrl': 'https://open.workec.com/v2/customer/file/list',
            #                   'params': {"crmIds": "5624387252,5624487824", "folderId": 1}}
            # , '客户资料-文件目录查询': {'tableName': 'ec_dim_fileFolderList', 'requestStyle': 'get',
            #                   'interfaceUrl': 'https://open.workec.com/v2/customer/folder/list',
            #                   'params': {"crmIds": "5624387252,5624487824"}}
            # , '客户标签列表': {'tableName': 'ec_dim_cusLabelList', 'requestStyle': 'get',
            #              'interfaceUrl': 'https://open.workec.com/v2/customer/queryLabel',
            #              'params': {"crmIds": "5624387252,5624487824"}}
            # , '客户头像列表': {'tableName': 'ec_dim_cusImagesList', 'requestStyle': 'get',
            #              'interfaceUrl': 'https://open.workec.com/v2/customer/face', 'params': ''}
            # , '查询客户轨迹': {'tableName': 'ec_dim_cusTrajectory', 'requestStyle': 'get',
            #              'interfaceUrl': 'https://open.workec.com/v2/customer/getTrajectory', 'params': {
            #         "date": {
            #             "endTime": "2022-03-25 17:00:00",
            #             "startTime": "2022-02-28 00:00:00"
            #         }}}
            # , '删除客户': {'tableName': 'ec_dim_customer_del', 'requestStyle': 'get',
            #            'interfaceUrl': 'https://open.workec.com/v2/customer/delcrms', 'params': {
            #         "startTime": "2022-03-18 00:00:00",
            #         "endTime": "2022-03-24 00:00:00",
            #         "lastId": ""
            #     }}
            # , '查询任务 ': {'tableName': 'ec_dim_taskList', 'requestStyle': 'get',
            #             'interfaceUrl': 'https://open.workec.com/v2/task/query', 'params': {
            #         "userType": 1,  # 1 我的任务 2 团队任务
            #         "exeType": 0,   # 执行与否（0 待执行 1 已结束 ）
            #         "optUserId": 17640187 # 操作人
            #     }}
            }
    for dicT in dicTemp:
        # for childT in dicTemp[dicT]:
        if dicT != '':
            tableName = dicTemp[dicT]['tableName']
            interfaceUrl = dicTemp[dicT]['interfaceUrl']
            params = dicTemp[dicT]['params']
            requeststyle = dicTemp[dicT]['requestStyle']

            if dicTemp[dicT]['IsXunHuan']=='是':
                if 'ec_dim_enum' in tableName:
                    #region 级联字段
                    dataList=getJilianData() #得到所有的级联字段
                    global isFirst #只有第一次才执行删除
                    isFirst=1
                    while isContinue:
                        params['fieldIds'] = dataList
                        paramsT = json.dumps(params)
                        if requeststyle == 'get':
                            returnResponse = requests.get(url=interfaceUrl, headers=heads, data=paramsT)
                        else:
                            returnResponse = requests.post(url=interfaceUrl, headers=heads, data=paramsT)
                        data = returnResponse.json()
                        jieXiData(tableName, data)
                        global isFirst
                        isFirst = isFirst+1
                        if hasNextPage==0:
                            isContinue = False
                            break;
                        else:
                            params['lastId']=lastId
                            isContinue = True
                    #endregion 级联字段
                elif 'ec_dim_customer' in tableName:
                    #region 客户信息
                    global isFirst  # 只有第一次才执行删除
                    isFirst = 1
                    while isContinue:
                        params['fieldIds'] = dataList
                        paramsT = json.dumps(params)
                        if requeststyle == 'get':
                            returnResponse = requests.get(url=interfaceUrl, headers=heads, data=paramsT)
                        else:
                            returnResponse = requests.post(url=interfaceUrl, headers=heads, data=paramsT)
                        data = returnResponse.json()
                        jieXiData(tableName, data)
                        isFirst = isFirst + 1
                        if hasNextPage == 0:
                            isContinue = False
                            break;
                        else:
                            params['lastId'] = lastId
                            isContinue = True
                    #endregion
            elif dicTemp[dicT]['IsXunHuan']=='否':
                paramsP = json.dumps(params)
                if requeststyle == 'get':
                    returnResponse = requests.get(url=interfaceUrl, headers=heads, data=paramsP)
                else:
                    returnResponse = requests.post(url=interfaceUrl, headers=heads, data=paramsP)
                data = returnResponse.json()
                jieXiData(tableName, data)

    # 获取级联字段-数据："fieldIds": [81654764]  参数：{"fieldIds":[81649962]}
    # 客户--客户行业分类：81655955
    # 客户--省市县：81654764
    # 客户--单位性质：81656622
    # 客户--产品：81619239#客户联系人--部门：81656624
    # 客户联系人--职务：81656625
    # 客户联系人--联系人层级：81649962
# endregion
