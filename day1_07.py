f=open('day1_07.txt')
data=f.read()
print (data)
out=open('day1_07_2.txt','w')
out.write(data)
f.close()
out.close()

