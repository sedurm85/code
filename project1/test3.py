# -*- coding: utf-8 -*-
import os
from urllib.request import urlretrieve
import csv
import matplotlib.pyplot as plt


#### path & sample download
base_path, sub_dirs, fnames = next(os.walk(os.getcwd()))
base_dpath = '.'
down_sname = 'file4.csv'
url = 'https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002287094&fileDetailSn=1&insertDataPrcus=N'
if not os.path.isfile(os.path.join(base_dpath,down_sname)):
	urlretrieve(url, os.path.join(base_dpath,down_sname))


#### data_sort from .csv file
with open(os.path.join(base_dpath,down_sname),'r',encoding='euc-kr') as f0:
	lines = csv.reader(f0)
	headers = next(lines)
	header = headers[9],headers[13],headers[15:17]
	records = []
	for line in lines:
		record = line[9],line[13],line[15:17]
		records.append(record)

#### data_sort index & records view
print("header structure \n{}\n".format(header))
print("record structure \n{}\n".format(records[0]))


#### data separate for plot
x1 = []
x2 = []
for record in records:
	x1.append(record[2][0])
	x2.append(record[2][1])

#### subplot : histogram
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(1, 3, 1)
plt.hist(x1, bins=100, width=0.9, color="blue")
plt.title('Histogram_Tall')
plt.xlabel('cm')
plt.ylabel('person')
ax2 = fig.add_subplot(1, 3, 2)
plt.hist(x2, bins=100, width=0.9, color="red")
plt.title('Histogram_Weight')
plt.xlabel('kg')
plt.ylabel('person')

#### subplot : scatter
ax3 = fig.add_subplot(1, 3, 3)
plt.scatter(x2,x1, marker='o', color="green")
plt.title('Scatter Plot for weight vs tall')
plt.xlabel('weight(kg)')
plt.ylabel('tall(cm)')
plt.show()
