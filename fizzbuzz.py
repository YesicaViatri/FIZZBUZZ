lst=[]
for i in range(0,100):
    i=i+1
    if (i % 3 == 0 and i % 5 == 0):
            print(i, " : Es FIZZBUZZ !!")
    elif i % 3 == 0:
        print(i," : Es FIZZ")
    elif i % 5 == 0:
        print(i," : Es BUZZ")
    else:
        print(i)
    lst.append(i)