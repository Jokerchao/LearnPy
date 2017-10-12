try:
    f=open("none-exit.txt")
    print ("Open Success!!!")
    f.close()
except:
    print ('file not exit!')
print ("Done!")
