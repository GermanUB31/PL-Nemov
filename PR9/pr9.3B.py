def vivod357itd():
    x=int(input())
    if x > 0:
        if x%2:
            print('Вывести число:',x)
            vivod357itd()
        else:
            vivod357itd()
vivod357itd()
