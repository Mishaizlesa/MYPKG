def countlines(name):
    global k
    k=name.readlines()
    print(len(k))
def countchars(name, c=0):
    for elem in k:
        c+=len(elem)
    print(c)
def test(name=open("input.txt")):
    countlines(name)
    countchars(name)
test()
