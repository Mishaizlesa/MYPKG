str="юосяыбыэ"
k="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
c=""
for i in range (1,33):
    print(c,end=" ")
    c=""
    for elem in str:
        if k.index(elem)+i>32:
            c+=k[k.index(elem)+i-33]
        else:
            c+=k[k.index(elem)+i]