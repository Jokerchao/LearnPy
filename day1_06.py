from random import choice
direction=['left','middle','right']
score=[0,0]
def kick():
    print ("====You Kick!====")
    print ("====Choose A direction to kick:")
    print ("left,middle,right")
    you=input()
    if you==choice(direction):
        print("====Oops!====")
    else :
        print ("====Goal!====")
        score[0]+=1
    print ("====%d(you)-%d(com)===="%(score[0],score[1]))
    print ("====You Saved!====")
    print ("====Choose A direction to save:")
    print ("left,middle,right")
    you=input()
    if you==choice(direction):
        print("====Oops!====")
    else :
        print ("====Goal!====")
        score[1]+=1
    print ("====%d(you)-%d(com)===="%(score[0],score[1]))
for i in range(5):
    print ('==== Round %d ====' % (i+1))
    kick()
if score[0]>score[1]:
    print ("You win!")
else :
    print ("You Lose.")

