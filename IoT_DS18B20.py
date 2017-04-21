import os
import glob
import time
import paho.mqtt.client as mqtt

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c

while True:
        temp_file=open("temperature_reading.txt","w") #Clears the text file
        temp_file.close()

	client = mqtt.Client()
	client.connect("test.mosquitto.org", 1883, 60)

        for i in range(1,100):
                temp_val=read_temp()

                temp_file=open("temperature_reading.txt","a")
                str1=str(temp_val)
                temp_file.writelines(str1 + '\n')
                print (i)
                time.sleep(1)
		client.publish("IoT/DS18B20/2017/PhD/GDGU",temp_val)

        temp_file=open("temperature_reading.txt","r")
        temp_file.seek(0,0)
        print temp_file.read()
        time.sleep(1)
        temp_file.close()
