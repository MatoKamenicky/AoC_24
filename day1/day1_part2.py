# list1 = [3, 4, 2, 1, 3, 3]
# list2 = [4, 3, 5, 3, 9, 3]


f=open('input.txt',"r")
lines=f.readlines()
list1=[]
list2=[]
for x in lines:
    list1.append(int(x.split('  ')[0]))
    list2.append(int(x.split('  ')[1]))
f.close()

times = []
for i in range(len(list1)):
    num = []
    for j in range(len(list2)):
        if list2[j] == list1[i]:
            num.append(j)
    times.append(len(num)*list1[i])

result = sum(times)
print(result)