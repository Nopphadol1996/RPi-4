import random
import csv

def writetocsv(data,filename='data'):
    with open('{}.csv'.format(filename),'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = file wirter 
        fw.writerow(data)

class Senser:
    """ Sensor Class for IoT """
    def __init__(self,name='DF-101'):
        self.name = name
        self.type = 'DHT22'
    
    def get_temp_humid(self): # ฟังก์ชั่นนี้เรียกว่า method
        t = random.uniform(25,39)
        t = round(t,2)
        h = random.uniform(50,95)
        h = round(h,2)
        return(t,h)

    def show_result(self,writecsv=False):
        temp,humid = self.get_temp_humid()
        print('Temperature: {:.2f}°C\nHumidity: {:.2f}%'.format(temp,humid))

        if writecsv == True:
            data = [temp,humid]
            writetocsv(data, self.name)

        
sensor1 = Senser('A-101')
sensor1.show_result(writecsv=True)

sensor2 = Senser('B-101')
sensor2.show_result(writecsv=True)


sensor3 = Senser('C-101')
sensor3.show_result(writecsv=True)


# print(sensor1.name)
# temp,humid = sensor1.get_temp_humid()
# print(temp,humid)
