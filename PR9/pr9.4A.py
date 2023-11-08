num=int(input('число: '))
def summacifr(num):
    if num>9:
        return num%10+summacifr(num%10)
    else:
        return num
print(summacifr(num))
