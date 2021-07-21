#if else statements
a = 10
b = 15.4
c = a+b

if(type(c) is int):
    print('it is an integer')
elif(type(c) is float):
    print('it is a float')
elif(type(c) is str):
    print('it is a string')
else:
    print('unknown value, probably a boolean or a collection')


    # nested for loops
for i in range(1, 5):
    print(i)
    for j in range(i, i + 2):
        if ((i + j) % 2 == 0):
            print('hello')
        else:
            continue

            #for loop with a while loop

for var in range(5,1,-1):
    var2=var
while(var2==var):
    print('hi', var*var2)
    var+=1
    if(var+var2)>10:
        continue
        print(i**2)
    else:
        print('for loop execution is successful')




