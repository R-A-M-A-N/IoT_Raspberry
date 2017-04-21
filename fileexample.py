import time

while True:
	val = [0,1,2,3,4,5,6,7,8,9,10]
	for i in range(0,11):
		f1=open("testfile.txt","a")
		str1 = str(val[i])
		f1.write(str1)
		f1.close

		f1=open("testfile.txt","r")
		f1.seek(0,0)
		print f1.readlines()
		time.sleep(1)
	i = 0


