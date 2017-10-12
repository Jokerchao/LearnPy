from random import randint
def isEqual(num1,num2):
    if num1==num2:
        print ('bingo')
        return True
    if num1>num2:
        print ('to big')
        return False
    if num1<num2:
        print ('to small')
        return true


num=randint(1,100)

print ("Guest what i think?")
bingo=False
while bingo==False:
    answer=input()
    bingo=isEqual(num,answer)
