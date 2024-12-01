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

list1.sort()
list2.sort()
dif = []

for i in range(len(list1)):
    dif.append(abs(list1[i] - list2[i]))

result = sum(dif)
print(result)