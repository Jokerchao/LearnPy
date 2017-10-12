# -*- coding: utf-8 -*-
height=float(input("请输入你的身高:\n"))
weight=float(input("请输入你的体重:\n"))
def bmi(height=1.75,weight=80.5):
    return weight/height**2

result=float(bmi(height,weight))

print (result)
if result<18.5:
    print ("过轻")
elif result>=18.5 and result<25:
    print ("正常")
elif result>=25 and result<28:
    print ("过重")
elif result>=28 and result<32:
    print ("肥胖")
elif result>=32:
    print ("严重肥胖")


    
