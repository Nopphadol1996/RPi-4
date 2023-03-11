import csv

def writetocsv(data):
   # data = [25.66,50.66]
   # data = [[25.66,50.66],[20.33,20.55]] writerows แบบมี s
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file wirter 
        fw.writerow(data)

writetocsv([20,55])