#for num in range(2,301):
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num,end=' ')

list=[1]*300
list[0:2]=[0,0]
for i in range(2,300):
    if list[i] == 1 :
        for j in range(2,i):
            if i % j ==0:
                list[i] = 0
for i in range(2,300):
    if list[i] ==1:
        print(i,end=' ')