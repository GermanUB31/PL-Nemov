god=int(input('vvedite god: '))
if god%4!=0:
    print('god ne wisokosniy')
elif god%100==0:
    if god%400==0:
        print('god wisokosny')
    else:
        print('god ne wisokosniy')
else:
    print('god wisokosny')
