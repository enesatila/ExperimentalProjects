list_1 = []

how = int(input('How Many Variables: '))

x = 1

while x <= how:
    my_Input = input('Variable: ')
    list_1.append(my_Input)
    x = x + 1


print('Repeating words and how many times they repeat = ')
x = list(set(list_1))
x.sort()
for i in range(len(x)):
    print("Repeating word",x[i],"repeats",list_1.count(x[i]),"times.")
    
