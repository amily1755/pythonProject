import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[5])
        low=int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
print(highs)

# 根据最高温度绘制图形
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red')
ax.plot(dates,lows,c='blue')

# 设置图形格式
ax.set_title("2018年每日最高温度",fontsize=24)
ax.set_xlabel(' ',fontsize=16)
fig.autofmt_xdate() #绘制倾斜的日期标签
ax.set_ylabel('温度(F)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.show()

