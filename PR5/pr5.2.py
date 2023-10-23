st='привет : привет : привет : привет : привет'
n=0
for i in st:
    if i==':':
        st=st.replace(':','%')
        n+=1
print(st)
print('количество замен:',n)
