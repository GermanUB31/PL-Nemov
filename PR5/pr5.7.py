st='привет привет привет привет'
n=len(st)
n=round(n/2)
for i in range(n):
    for g in st:
        st=st.replace('п','*',n)
print(st)
