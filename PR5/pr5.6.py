st='Шутка отменяется произошли технические трудности'
n=0
for i in st:
    if i=='а':
        st=st.replace('а','')
        n+=1
print(st)
print('кол-во замен:',n)
