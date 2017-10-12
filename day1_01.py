# -*- coding: cp936 -*-
import random
f=open("game.txt")
times=0
score=f.read().split()
game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])
f.close
if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0
print ("你已经玩了%d次，最少%d轮猜出答案，平均%.2f猜出答案"%(game_times,min_times,avg_times))
num=random.randint(1,100)
bingo=False
print ('Guest what i think')
game_times+=1
while bingo==False:
    answer=int(input())
    times+=1
    if num>answer:
        print ("to small")
    if num<answer:
        print ("to big")
    if num==answer:
        print ("Bingo!")
        bingo=True
if game_times == 0 or times < min_times:
   min_times = times
total_times+=1
result='%d %d %d'%(game_times,min_times,total_times)
print (result)
with open('game.txt','w') as f:
    f.write(result)
f.close

        



