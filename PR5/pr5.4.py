st= 'аоаоаоаоаоаоаоаоао'
n=0
for i in st:
    if i=='а':
        st=st.replace('а','о')
        n+=1
print(st)
print('кол-во замен:',n)
print('кол-во символов:',len(st))
