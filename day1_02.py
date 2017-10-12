from random import randint
num=randint(1,100)
bingo=False
print ('Guest what i think')

while bingo==False:
    answer=int(input())
    if num>answer:
        print ("to small")
    if num<answer:
        print ("to big")
    if num==answer:
        print ("Bingo!")
        bingo=True
