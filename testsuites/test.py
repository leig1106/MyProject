import csv,os,time

file = os.getcwd()+'\\imgs\\'+'aa.csv'

with open(file,'a',encoding='gbk') as csvfile:
    w = csv.writer(csvfile,dialect='excel')
    w.writerow(['2018-11-22T17:47:32.013Z','嘿嘿'])

time.sleep(3)


with open(file,'r',encoding='gbk') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        print(row)
