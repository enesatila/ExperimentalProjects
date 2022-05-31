from asyncio.base_subprocess import BaseSubprocessTransport


List = []
a = input('Variable 1: ')
b = input('Variable 2: ')
c = input('Variable 3: ')

List.append(a)
List.append(b)
List.append(c)
if(a == b):
    print('repating word : ' + a)
else:
    pass
if(c == b):
    print('repeating word : ' + b)
else:
    pass
if(a == c):
    print('repeating word : ' + c)
else:
    pass


List1 = set(List)

print('repeating words count : ' + str(len(List)-len(List1)))

print(List1)
#Hocam burdan aşşağısı aslında tam olarak yukarıdakinin aynısını 
#yapmalı ama diffrence kısmında bir şeyler yanlış.
#Acaba atila20@itu.edu.tr mailime feedback verebilir misiniz


'''
list_1 = []

how = int(input('How Many Variables: '))

x = 1

while x <= how:
    my_Input = input('Variable: ')
    list_1.append(my_Input)
    x = x + 1

list_2 = set(list_1)
list_3 = list(list_2)

''''''list_difference = []
for item in list_3:
  if item not in list_1:
    list_difference.append(item)'''''''''

'''
list_difference = [item for item in list_3 if item not in list_1]

print(list_difference)


print(list_1)
print(list_2)
print(list_3)

'''