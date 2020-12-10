f = open("text.txt", "r")
list = []
while(True):
    linea = f.readline()
    list.append(linea)
    print(linea)
    if not linea:
        break
f.close()
print(list)