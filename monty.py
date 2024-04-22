from random import randint

k = int(input('monti time : '))

def montihol(time) :

    suc = 0 #자동차를 고른 횟수
    fail = 0 #염소를 고른 횟수

    for i in range(time) :
        car = randint(0, 2)
        
        doors = [0, 0, 0]

        doors[car] +=1

        choice = randint(0, 2)

        if doors[choice] == 0 :
            doors[choice] +=2
        else:
            doors[choice] = 3

        doors.remove(0)

        if 2 in doors:
            suc+=1
        else :
            fail +=1
    arr = [suc,fail,suc+fail,suc/(suc+fail)]
    return arr

arr = montihol(k)

print('suc %d번, fail %d번, suc_percent %f%%.'%(arr[0],arr[1],arr[3]*100))

