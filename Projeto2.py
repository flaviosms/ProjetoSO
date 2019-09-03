def fifo(filename):
    arq = open(filename)
    lista=[]
    flag=1
    c=0
    for line in arq:
      if (flag):
        tam= int(line)
        flag=0
        continue
      if (line in lista):
        continue
      else:
        c+=1
        if (len(lista) >= tam):
          lista.pop(0)
          lista.append(line)
          continue
        else:
          lista.append(line)
    return c

def lru(filename):
    arq = open(filename)
    lista=[]
    flag=1
    c=0
    for line in arq:
        if (flag):
            tam= int(line)
            flag=0
            continue
        if (line in lista):
            lista.pop(lista.index(line))
            lista.append(line)
            continue
        else:
            c+=1
            if (len(lista) >= tam):
                lista.pop(0)
                lista.append(line)
                continue
            else:
                lista.append(line)
    return c

def otm(filename):
    arq = open(filename)
    array=[]
    flag=1
    for line in arq:
        if (flag):
            tam= int(line)
            flag=0
            continue
        else:
            array.append(line.strip())
    listauso=[]
    usage=[0 for x in array]
    for index,page1 in enumerate(array):
        for page2 in array[index+1:]:
            if(page1==page2):
                usage[index]+=1
        listauso.append([page1,usage[index]])
    lista=[]
    c=0
    for page in listauso:
        found=0
        for x in lista:
            if(x[0]==page[0]):
                print(x[0])
                print(lista)
                x[1]-=1
                print(lista)
                found=1
        if(not found):
            c+=1
            if (len(lista) >= tam):
                lista.sort(key=lambda tup: tup[1])
                lista.pop(0)
                lista.append(page)
                continue
            else:
                lista.append(page)
    return c
filename="entrada2.txt"
print(fifo(filename))
print(lru(filename))
otm(filename)
