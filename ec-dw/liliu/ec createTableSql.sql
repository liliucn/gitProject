IF EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_customer_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_customer_temp;
CREATE TABLE ec_dim_customer_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
followUserId nvarchar ( 2000 ),
groupId nvarchar ( 2000 ),
name nvarchar ( 2000 ),
call nvarchar ( 2000 ),
gender nvarchar ( 2000 ),
birthday nvarchar ( 2000 ),
isLunarBirthday nvarchar ( 2000 ),
title nvarchar ( 2000 ),
qq nvarchar ( 2000 ),
mobile nvarchar ( 2000 ),
phone nvarchar ( 2000 ),
fax nvarchar ( 2000 ),
email nvarchar ( 2000 ),
company nvarchar ( 2000 ),
companyUrl nvarchar ( 2000 ),
companyAddress nvarchar ( 2000 ),
memo nvarchar ( 2000 ),
vocation nvarchar ( 2000 ),
channel nvarchar ( 2000 ),
prefecture nvarchar ( 2000 ),
crmId nvarchar ( 2000 ),
modifyTime nvarchar ( 2000 ),
contactTime nvarchar ( 2000 ),
createTime nvarchar ( 2000 ),
lastFollowUserId nvarchar ( 2000 ),
step nvarchar ( 2000 ),
createUserId nvarchar ( 2000 ),
wechat nvarchar ( 2000 ),
wechats nvarchar ( 2000 ),
emails nvarchar ( 2000 ),
mobiles nvarchar ( 2000 ),
storageTime nvarchar ( 2000 ),
publicPondId nvarchar ( 2000 ),
apiAdd nvarchar ( 2000 ),
crmType nvarchar ( 2000 ),
shareUserId nvarchar ( 2000 ),
lastContactTime nvarchar ( 2000 ),
stars nvarchar ( 2000 ),
khhyflyj nvarchar ( 2000 ),
khhyflej nvarchar ( 2000 ),
sheng nvarchar ( 2000 ),
shi nvarchar ( 2000 ),
qx nvarchar ( 2000 ),
dwxz nvarchar ( 2000 ),
cp nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户列表
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_enum_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_enum_temp;
CREATE TABLE ec_dim_enum_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
fieldId nvarchar ( 2000 ),
paramId nvarchar ( 2000 ),
parentParamId nvarchar ( 2000 ),
paramName nvarchar ( 2000 ),
sort nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 枚举表-级联字段
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_customerContact_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_customerContact_temp;
CREATE TABLE ec_dim_customerContact_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
id nvarchar ( 2000 ),
crmId nvarchar ( 2000 ),
corpid nvarchar ( 2000 ),
createUserId nvarchar ( 2000 ),
name nvarchar ( 2000 ),
callName nvarchar ( 2000 ),
title nvarchar ( 2000 ),
mobile nvarchar ( 2000 ),
mobileCode nvarchar ( 2000 ),
phone nvarchar ( 2000 ),
phoneCode nvarchar ( 2000 ),
phoneExtension nvarchar ( 2000 ),
qq nvarchar ( 2000 ),
email nvarchar ( 2000 ),
wechat nvarchar ( 2000 ),
birthday nvarchar ( 2000 ),
lunarBirthday nvarchar ( 2000 ),
lunarLeap nvarchar ( 2000 ),
memo nvarchar ( 2000 ),
gender nvarchar ( 2000 ),
createTime nvarchar ( 2000 ),
updateTime nvarchar ( 2000 ),
bumen nvarchar ( 2000 ),
zhiwu nvarchar ( 2000 ),
lxrcj nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户联系人信息
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_department_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_department_temp;
CREATE TABLE ec_dim_department_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
deptId nvarchar ( 2000 ),
dept nvarchar ( 2000 ),
parentDeptId nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 组织架构-部门
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_employee_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_employee_temp;
CREATE TABLE ec_dim_employee_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
userId nvarchar ( 2000 ),
userName nvarchar ( 2000 ),
deptId nvarchar ( 2000 ),
title nvarchar ( 2000 ),
status nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 组织架构-人员
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_fileList_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_fileList_temp;
CREATE TABLE ec_dim_fileList_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
crmId nvarchar ( 2000 ),
folderId nvarchar ( 2000 ),
createUserId nvarchar ( 2000 ),
createUserName nvarchar ( 2000 ),
path nvarchar ( 2000 ),
id nvarchar ( 2000 ),
name nvarchar ( 2000 ),
SIZE nvarchar ( 2000 ),
updateTime nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- EC-客户资料-文件列表查询
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_fileFolderList_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_fileFolderList_temp;
CREATE TABLE ec_dim_fileFolderList_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
CrmFolderItem nvarchar ( 2000 ),
crmId nvarchar ( 2000 ),
createUserId nvarchar ( 2000 ),
createUserName nvarchar ( 2000 ),
id nvarchar ( 2000 ),
name nvarchar ( 2000 ),
SIZE nvarchar ( 2000 ),
updateTime nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- EC-客户资料-文件目录查询
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusLabelBaseInfosGroup_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusLabelBaseInfosGroup_temp;
CREATE TABLE ec_dim_cusLabelBaseInfosGroup_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
labelGroupId nvarchar ( 2000 ),
labelGroupName nvarchar ( 2000 ),
labelGroupSort nvarchar ( 2000 ),
labelGroupType nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户标签管理-分组
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusLabelBaseInfosLabel_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusLabelBaseInfosLabel_temp;
CREATE TABLE ec_dim_cusLabelBaseInfosLabel_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
labelGroupId nvarchar ( 2000 ),
labelId nvarchar ( 2000 ),
labelName nvarchar ( 2000 ),
labelSort nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户标签管理-标签
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusLabelList_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusLabelList_temp;
CREATE TABLE ec_dim_cusLabelList_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
crmId nvarchar ( 2000 ),
labelId nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户标签列表
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusStageBaseInfos_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusStageBaseInfos_temp;
CREATE TABLE ec_dim_cusStageBaseInfos_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
name nvarchar ( 2000 ),
stage nvarchar ( 2000 ),
status nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户进展列表
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusImagesList_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusImagesList_temp;
CREATE TABLE ec_dim_cusImagesList_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
crmId nvarchar ( 2000 ),
face nvarchar ( 2000 ),
name nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户头像
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusTrajectoryBaseInfos_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusTrajectoryBaseInfos_temp;
CREATE TABLE ec_dim_cusTrajectoryBaseInfos_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
levelOneID nvarchar ( 2000 ),
levelOneName nvarchar ( 2000 ),
TrajectoryID nvarchar ( 2000 ),
TrajectoryName nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 客户轨迹
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_cusTrajectory_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_cusTrajectory_temp;
CREATE TABLE ec_dim_cusTrajectory_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
content nvarchar ( 2000 ),
createTime nvarchar ( 2000 ),
crmId nvarchar ( 2000 ),
receiveUserIds nvarchar ( 2000 ),
trajectoryId nvarchar ( 2000 ),
trajectoryType nvarchar ( 2000 ),
userId nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 查询客户轨迹
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_customer_del_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_customer_del_temp;
CREATE TABLE ec_dim_customer_del_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
crmId nvarchar ( 2000 ),
delTime nvarchar ( 2000 ),
id nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 删除客户
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_taskList_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_taskList_temp;
CREATE TABLE ec_dim_taskList_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
taskId nvarchar ( 2000 ),
ruleId nvarchar ( 2000 ),
title nvarchar ( 2000 ),
noticeTime nvarchar ( 2000 ),
endTime nvarchar ( 2000 ),
createName nvarchar ( 2000 ),
createUserId nvarchar ( 2000 ),
exeName nvarchar ( 2000 ),
exeId nvarchar ( 2000 ),
exeNum nvarchar ( 2000 ),
taskNum nvarchar ( 2000 ),
detail nvarchar ( 2000 ),
ruleType nvarchar ( 2000 ),
taskType nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 查询任务
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'ec_dim_kindType_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE ec_dim_kindType_temp;
CREATE TABLE ec_dim_kindType_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
typeID nvarchar ( 2000 ),
typeName nvarchar ( 2000 ),
kindType nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 规则|任务类型
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'EC_dim_customerAutoInfo_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE EC_dim_customerAutoInfo_temp;
CREATE TABLE EC_dim_customerAutoInfo_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
fieldGroupId nvarchar ( 2000 ),
fieldGroupName nvarchar ( 2000 ),
fieldGroupSort nvarchar ( 2000 ),
fieldId nvarchar ( 2000 ),
fieldName nvarchar ( 2000 ),
fieldSort nvarchar ( 2000 ),
fieldType nvarchar ( 2000 ),
category nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 企业的自定义字段信息
IF
	EXISTS ( SELECT * FROM dbo.sysobjects WHERE id = object_id( 'EC_dim_customerContactAutoInfo_temp' ) AND OBJECTPROPERTY( id, 'IsUserTable' ) = 1 ) DROP TABLE EC_dim_customerContactAutoInfo_temp;
CREATE TABLE EC_dim_customerContactAutoInfo_temp (
autoID INT IDENTITY ( 1, 1 ) NOT NULL PRIMARY KEY,
id nvarchar ( 2000 ),
text nvarchar ( 2000 ),
type nvarchar ( 2000 ),
isMust nvarchar ( 2000 ),
regex nvarchar ( 2000 ),
LEVEL nvarchar ( 2000 ),
remark1 nvarchar ( 2000 ),
remark2 nvarchar ( 2000 ),
remark3 nvarchar ( 2000 ),
remark4 nvarchar ( 2000 ),
remark5 nvarchar ( 2000 ),
remark6 nvarchar ( 2000 ));
-- 企业联系人的自定义字段