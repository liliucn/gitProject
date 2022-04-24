### 文章链接 https://mp.weixin.qq.com/s/abESwR5CBWBufWWcPPfp5g
from time import gmtime, strftime
import pandas as pd
import pytz
from datetime import *
from dateutil import *
from datetime import date
import random
from dateutil.rrule import rrule, WEEKLY, MO
from dateutil.relativedelta import *
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import calendar
import pendulum
import time

### 1使用 time 模块展示当前日期和时间
t = time.localtime()
print(time.asctime(t))
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%A", gmtime()))
print(strftime("%D", gmtime()))
print(strftime("%B", gmtime()))
print(strftime("%y", gmtime()))

### Convert seconds into GMT date
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(1234567890)))

# 测试
### 2将天、小时、分钟转换为秒
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

### Read the inputs from user
days = int(input("Enter number of Days: "))
hours = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))

### Calculate the days, hours, minutes and seconds
total_seconds = days * SECONDS_PER_DAY
total_seconds = total_seconds + (hours * SECONDS_PER_HOUR)
total_seconds = total_seconds + (minutes * SECONDS_PER_MINUTE)
total_seconds = total_seconds + seconds

### Display the result
print("Total number of seconds: ", "%d" % (total_seconds))

### 3使用 Pandas 获取当前日期和时间
print(pd.datetime.now())
print(pd.datetime.now().date())
print(pd.datetime.now().year)
print(pd.datetime.now().month)
print(pd.datetime.now().day)
print(pd.datetime.now().hour)
print(pd.datetime.now().minute)
print(pd.datetime.now().second)
print(pd.datetime.now().microsecond)

### 4将字符串转换为日期时间对象

d1 = "Jan 7 2015  1:15PM"
d2 = "2015 Jan 7  1:33PM"

### If you know date format
now = datetime.now()
date1=now.strftime('%a, %b %d %H:%M')
# date1 = now.strptime(d1, '%b %d %Y %I:%M%p')
print(type(date1))
print(date1)

### If you don't know date format
date2 = parser.parse(d2)
print(type(date2))
print(date2)

### 5以毫秒为单位获取当前时间
milliseconds = int(round(time.time() * 1000))
print(milliseconds)

### 6从给定的日期当中获取星期几
dayofweek = date(2018,11,1).strftime("%A")
print(dayofweek)
### weekday Monday is 0 and Sunday is 6
print("weekday():", date(2010, 6, 16).weekday())

### isoweekday() Monday is 1 and Sunday is 7
print("isoweekday()", date(2010, 6, 16).isoweekday())

dayofweek = datetime.today().strftime("%A")
print(dayofweek)
print("weekday():", datetime.today().weekday())
print("isoweekday()", datetime.today().isoweekday())

### 7计算两个日期时间对象之间的时差
datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
date1 = '2016-04-16 10:01:28.585'
date2 = '2016-03-10 09:56:28.067'
diff = datetime.strptime(date1, datetimeFormat) \
       - datetime.strptime(date2, datetimeFormat)

print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)

### 8将 5 分钟添加到 Unix 时间戳
import datetime
future = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
print(calendar.timegm(future.timetuple()))

### 9在 Python 中遍历一系列日期
start = datetime.datetime.strptime("21-06-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("05-07-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))

### 10巴黎时间更改为纽约时间
in_paris = pendulum.datetime(2016, 8, 7, 22, 24, 30, tz='Europe/Paris')
print(in_paris)

in_us = in_paris.in_timezone('America/New_York')
print(in_us)

### 11使用 Python 获得最后7个工作日
today = date.today()
for i in range(7):
    d = today - timedelta(days=i)
    if d.weekday() < 5:
        print(d)


### 11从今天的日期和一个人的生日推算年龄
def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
from datetime import date
print(calculate_age(date(2001, 3, 1)))

### 13获得本月的第一个星期二
c = calendar.Calendar(firstweekday=calendar.SUNDAY)
monthcal = c.monthdatescalendar(date.today().year, date.today().month)

try:
    tues = [day for week in monthcal for day in week if
            day.weekday() == calendar.TUESDAY and day.month == date.today().month][0]
    print(tues)
except IndexError:
    print('No date found')

### 14将整数转换为日期对象
i = 1545730073
timestamp = datetime.datetime.fromtimestamp(i)

print(timestamp)
print(type(timestamp))

### 15当前日期减去 N 天的天数

d = date.today() - timedelta(days=5)
print(d)

### 16比较两个日期
a = datetime.datetime(2020, 12, 31, 23, 59, 59)
b = datetime.datetime(2020, 11, 30, 23, 59, 59)

print(a < b)
print(a > b)

### 17从 datetime 对象中提取年份

year = datetime.date.today().year
print(year)

### 18在 Python 中找到星期几

dt = pendulum.parse('2021-05-18')
print(dt.day_of_week)

dt = pendulum.parse('2021-05-01')
print(dt.day_of_week)

dt = pendulum.parse('2021-05-21')
print(dt.day_of_week)

### 19从当前日期获取 7 天前的日期
now = datetime.datetime.now()

for x in range(7):
    d = now - timedelta(days=x)
    print(d.strftime("%Y-%m-%d"))

### 20将两个日期时间对象之间的差值转换为秒
time1 = datetime.datetime.strptime('19 01 2021', '%d %m %Y')
time2 = datetime.datetime.strptime('25 01 2021', '%d %m %Y')

difference = time2 - time1
print(difference)

seconds = difference.total_seconds()
print(seconds)

### 21获得任何一个月的第三个星期五
c = calendar.Calendar(firstweekday=calendar.SUNDAY)
year = 2021
month = 5
monthcal = c.monthdatescalendar(year, month)

try:
    third_friday = [day for week in monthcal for day in week if
                    day.weekday() == calendar.FRIDAY and day.month == month][2]
    print(third_friday)
except IndexError:
    print('No date found')

### 22从 Python 中的周数获取日期
week = 25
year = 2021
date = date(year, 1, 1) + relativedelta(weeks=+week)
print(date)

### 23获取特定日期的工作日

print(datetime.date(2020, 5, 15).isocalendar()[2])

### 24创建一个 15 分钟前的 DateTime

dt = datetime.datetime.now() - datetime.timedelta(minutes=15)
print(dt)

### 25从特定日期获取周的开始和结束日期

dt = pendulum.datetime(2012, 9, 5)

start = dt.start_of('week')
print(start.to_datetime_string())

end = dt.end_of('week')
print(end.to_datetime_string())

### 26两个日期之间的差异（以秒为单位）
fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.datetime.strptime('2020-01-01 17:31:22', fmt)
d2 = datetime.datetime.strptime('2020-01-03 17:31:22', fmt)

days_diff = d2 - d1
print(days_diff.days * 24 * 60 * 60)

### 27以这种格式获取昨天的日期MMDDYY

yesterday = date.today() - timedelta(days=1)
print(yesterday.strftime('%m%d%y'))

### 28从今天的日期获取上周三
today = date.today()
offset = (today.weekday() - 2) % 7
wednesday = today - timedelta(days=offset)
print(wednesday)

### 29所有可用时区的列表打印
for i in pytz.all_timezones:
    print(i)

### 30获取指定开始日期和结束日期之间的日期范围

start = datetime.datetime.strptime("21-06-2020", "%d-%m-%Y")
end = datetime.datetime.strptime("05-07-2020", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))

### 31毫秒转换为数据

time_in_millis = 1596542285000
dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0, tz=datetime.timezone.utc)
print(dt)


### 32查找给定日期之后的第一个星期日的日期
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


d = datetime.date(2021, 5, 16)
next_sunday = next_weekday(d, 6)
print(next_sunday)

### 33将（Unix）时间戳秒转换为日期和时间字符串
dateStr = datetime.datetime.fromtimestamp(1415419007).strftime("%A, %B %d, %Y %I:%M:%S")
print(type(dateStr))
print(dateStr)

### 34以月为单位的两个日期之间的差异
date1 = datetime.datetime.strptime('2014-01-12 12:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.datetime.strptime('2021-07-15 12:00:00', '%Y-%m-%d %H:%M:%S')
r = relativedelta(date2, date1)
print(r.months + (12 * r.years))

### 35将本地时间字符串转换为 UTC
utc_zone = tz.gettz('UTC')
local_zone = tz.gettz('America/Chicago')

utc_zone = tz.tzutc()
local_zone = tz.tzlocal()

local_time = datetime.datetime.strptime("2020-10-25 15:12:00", '%Y-%m-%d %H:%M:%S')
print(local_time)
local_time = local_time.replace(tzinfo=local_zone)
print(local_time)

utc_time = local_time.astimezone(utc_zone)
print(utc_time)

utc_string = utc_time.strftime('%Y-%m-%d %H:%M:%S')
print(utc_string)

### 36获取当月的最后一个星期四
month = calendar.monthcalendar(datetime.datetime.today().year, datetime.datetime.today().month)
thrusday = max(month[-1][calendar.THURSDAY], month[-2][calendar.THURSDAY])
print(thrusday)

### 37从特定日期查找一年中的第几周
dt = pendulum.parse('2015-05-18')
print(dt.week_of_year)

dt = pendulum.parse('2019-12-01')
print(dt.week_of_year)

dt = pendulum.parse('2018-01-21')
print(dt.week_of_year)

### 38从给定日期获取星期几
dt = datetime.datetime(2021, 4, 25, 23, 24, 55, 173504)
print(calendar.day_name[dt.weekday()])

### 39用 AM PM 打印当前时间
print(datetime.datetime.today().strftime("%I:%M %p"))

### 40获得一个月的最后一天
print(calendar.monthrange(2002, 1)[1])
print(calendar.monthrange(2008, 6)[1])
print(calendar.monthrange(2012, 2)[1])
print(calendar.monthrange(2015, 2)[1])

### 41从工作日值中获取工作日名称
print(calendar.day_name[0])
print(calendar.day_name[1])
print(calendar.day_name[2])
print(calendar.day_name[3])
print(calendar.day_name[4])
print(calendar.day_name[5])
print(calendar.day_name[6])

### 42将 N 小时数添加到当前日期时间
d = datetime.datetime.today() + timedelta(hours=18)
print(d)

### 43从当前日期获取年、月、日、小时、分钟
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

### 44获取特定月份和年份的最后一个星期日
month = calendar.monthcalendar(2021, 2)

last_sunday = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
print(last_sunday)

### 45查找特定日期的年份中的哪一天
dt = pendulum.parse('2015-05-18')
print(dt.day_of_year)

dt = pendulum.parse('2019-12-01')
print(dt.day_of_year)

dt = pendulum.parse('2018-01-21')
print(dt.day_of_year)

### 46查找当前日期是工作日还是周末
weekno = datetime.datetime.today().weekday()
if weekno < 5:
    print("Weekday")
else:  ### 5 Sat, 6 Sun
    print("Weekend")

### 47组合 datetime.date 和 datetime.time 对象
d = datetime.datetime.combine(datetime.date(2020, 11, 14),
                              datetime.time(10, 23, 15))

print(d)

### 48获得每月的第 5 个星期一
c = calendar.Calendar(firstweekday=calendar.SUNDAY)
year = 2016
month = 2
monthcal = c.monthdatescalendar(year, month)

try:
    fifth_monday = [day for week in monthcal for day in week if
                    day.weekday() == calendar.MONDAY and day.month == month][4]
    print(fifth_monday)
except IndexError:
    print('No date found')

### 49将日期时间对象转换为日期对象
datetime_obj = datetime.datetime(2020, 12, 15, 10, 15, 45, 321474)
print(datetime_obj)

date_obj = datetime_obj.date()
print(date_obj)

### 50获取没有微秒的当前日期时间
print(datetime.datetime.now().isoformat(' ', 'seconds'))

### 51将 N 秒数添加到特定日期时间
a = datetime.datetime(2020, 12, 31, 23, 59, 45)
b = a + datetime.timedelta(seconds=30)

print(a)
print(b)

### 52从当前日期获取两位数的月份和日期
dt = datetime.datetime.now()

print(dt.strftime('%m'))
print('{:02d}'.format(dt.month))
print(f'{dt.month:02d}')
print('%02d' % dt.month)

print(dt.strftime('%d'))
print('{:02d}'.format(dt.day))
print(f'{dt.day:02d}')
print('%02d' % dt.day)

### 53从特定日期获取月份数据的开始和结束日期
dt = pendulum.datetime(2012, 9, 5)

start = dt.start_of('month')
print(start.to_datetime_string())

end = dt.end_of('month')
print(end.to_datetime_string())

### 54以周为单位的两个日期之间的差异
date1 = datetime.date(2020, 12, 23)
date2 = datetime.date(2021, 5, 11)

days = abs(date1 - date2).days
print(days // 7)

### 55将字符串格式的日期转换为 Unix 时间戳
stime = '15/05/2021'
print(datetime.datetime.strptime(stime, "%d/%m/%Y").timestamp())


### 56获取最后一个周日和周六的日期
def prior_week_end():
    return datetime.datetime.now() - timedelta(days=((datetime.datetime.now().isoweekday() + 1) % 7))


def prior_week_start():
    return prior_week_end() - timedelta(days=6)


print('Sunday', format(prior_week_start()))
print('Saturday', format(prior_week_end()))

### 57检查对象是否属于 datetime.date 类型
x = '2012-9-1'
y = datetime.date(2012, 9, 1)

print(isinstance(x, datetime.date))
print(isinstance(y, datetime.date))

### 58获取特定日期的周数
print(datetime.date(2020, 5, 15).isocalendar()[1])

### 59获取 UTC 时间
dt = datetime.datetime.utcnow()

### 60获取本周的开始和结束日期
today = pendulum.now()

start = today.start_of('week')
print(start.to_datetime_string())

end = today.end_of('week')
print(end.to_datetime_string())

### 61两个日期之间的差异（以分钟为单位）

fmt = '%Y-%m-%d %H:%M:%S'
d1 = datetime.datetime.strptime('2010-01-01 17:31:22', fmt)
d2 = datetime.datetime.strptime('2010-01-03 17:31:22', fmt)

days_diff = d2 - d1
print(days_diff.days * 24 * 60)

### 62将日期时间对象转换为日期字符串
t = datetime.datetime(2020, 12, 23)
x = t.strftime('%m/%d/%Y')
print(x)

### 63获得上周五
today = date.today()
offset = (today.weekday() - 4) % 7
friday = today - timedelta(days=offset)
print(friday)

### 64将 3 周添加到任何特定日期
dt = pendulum.datetime(2012, 2, 15)
dt = dt.add(weeks=3)
print(dt.to_date_string())


### 65在其他两个日期之间生成一个随机日期
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)


print(random_date("1/1/2020 1:10 PM", "1/1/2021 1:10 AM", random.random()))

### 66查找从今天开始的第一个星期一的日期

next_monday = rrule(freq=WEEKLY, dtstart=date.today(), byweekday=MO, count=1)[0]
print(next_monday)

### 67两个日期之间的差异（以天为单位）

d1 = datetime.date(2019, 8, 18)
d2 = datetime.date(2021, 12, 10)

days_diff = d2 - d1
print(days_diff.days)

### 68向当前日期添加六个月

date = datetime.datetime.now()
print(date)

date = date + relativedelta(months=+6)
print(date)

### 69将数据时间对象转换为 Unix（时间戳）
### Saturday, October 10, 2015 10:10:00 AM
date_obj = datetime.datetime(2015, 10, 10, 10, 10)
print("Unix Timestamp: ", (time.mktime(date_obj.timetuple())))

### 70将年、月、日、时、分、秒的 N 个数字添加到当前日期时间
add_days = datetime.datetime.today() + relativedelta(days=+6)
add_months = datetime.datetime.today() + relativedelta(months=+6)
add_years = datetime.datetime.today() + relativedelta(years=+6)

add_hours = datetime.datetime.today() + relativedelta(hours=+6)
add_mins = datetime.datetime.today() + relativedelta(minutes=+6)
add_seconds = datetime.datetime.today() + relativedelta(seconds=+6)

print("Current Date Time:", datetime.datetime.today())
print("Add 6 days:", add_days)
print("Add 6 months:", add_months)
print("Add 6 years:", add_years)
print("Add 6 hours:", add_hours)
print("Add 6 mins:", add_mins)
print("Add 6 seconds:", add_seconds)

### 71获取指定开始日期和结束日期之间的日期范围
start = datetime.datetime.strptime("2016-06-15", "%Y-%m-%d")
end = datetime.datetime.strptime("2016-06-30", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end - start).days))

for date_object in date_array:
    print(date_object.strftime("%Y-%m-%d"))

### 71减去 N 个年、月、日、时、分、秒到当前日期时间
sub_days = datetime.datetime.today() + relativedelta(days=-6)
sub_months = datetime.datetime.today() + relativedelta(months=-6)
sub_years = datetime.datetime.today() + relativedelta(years=-6)

sub_hours = datetime.datetime.today() + relativedelta(hours=-6)
sub_mins = datetime.datetime.today() + relativedelta(minutes=-6)
sub_seconds = datetime.datetime.today() + relativedelta(seconds=-6)

print("Current Date Time:", datetime.datetime.today())
print("Subtract 6 days:", add_days)
print("Subtract 6 months:", add_months)
print("Subtract 6 years:", add_years)
print("Subtract 6 hours:", add_hours)
print("Subtract 6 mins:", add_mins)
print("Subtract 6 seconds:", add_seconds)

### 72获取指定年份和月份的月份第一天的工作日和月份的天数
print("Year:2002 - Month:2")
month_range = calendar.monthrange(2002, 2)
print("Weekday of first day of the month:", month_range[0])
print("Number of days in month:", month_range[1])
print()
print("Year:2010 - Month:5")
month_range = calendar.monthrange(2010, 5)
print("Weekday of first day of the month:", month_range[0])
print("Number of days in month:", month_range[1])

### 73打印特定年份的所有星期一
year = 2018
date_object = datetime.date(year, 1, 1)
date_object += timedelta(days=1 - date_object.isoweekday())

while date_object.year == year:
    print(date_object)
    date_object += timedelta(days=7)

### 74打印特定年份的日历

cal_display = calendar.TextCalendar(calendar.MONDAY)
### Year: 2019
### Column width: 1
### Lines per week: 1
### Number of spaces between month columns: 0
### No. of months per column: 2
print(cal_display.formatyear(2019, 1, 1, 0, 2))

### 75从月份编号中获取月份名称

### Month name from number
print("Month name from number 5:")
month_num = 1
month_abre = datetime.date(2015, month_num, 1).strftime('%b')
month_name = datetime.date(2015, month_num, 1).strftime('%B')
print("Short Name:", month_abre)
print("Full  Name:", month_name)

print("\nList of all months from calendar")
### Print list of all months from calendar
for month_val in range(1, 13):
    print(calendar.month_abbr[month_val], "-", calendar.month_name[month_val])

### 76从给定日期获取一周的开始和结束日期
date_str = '2018-01-14'
date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')

start_of_week = date_obj - timedelta(days=date_obj.weekday())  ### Monday
end_of_week = start_of_week + timedelta(days=6)  ### Sunday
print(start_of_week)
print(end_of_week)

### 77根据当前日期查找上一个和下一个星期一的日期
today = datetime.date.today()
last_monday = today - timedelta(days=today.weekday())
coming_monday = today + timedelta(days=-today.weekday(), weeks=1)
print("Today:", today)
print("Last Monday:", last_monday)
print("Coming Monday:", coming_monday)

### 78获取当前季度的第一个日期和最后一个日期
current_date = datetime.datetime.now()
current_quarter = round((current_date.month - 1) / 3 + 1)
first_date = datetime.datetime(current_date.year, 3 * current_quarter - 2, 1)
last_date = datetime.datetime(current_date.year, 3 * current_quarter + 1, 1) \
            + timedelta(days=-1)

print("First Day of Quarter:", first_date)
print("Last Day of Quarter:", last_date)
