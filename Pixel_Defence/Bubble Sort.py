tower = [5,2,4,1,3,0]
print(tower)

def BubbleSort(mylist):
    for i in range(0,len(mylist)):
        for j in range(0, len(mylist)-1):
            if mylist[j]>mylist[j+1]:
                x = mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=x
    return mylist

print(BubbleSort(tower))
