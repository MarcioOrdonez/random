def principal():
    fileCreate()
    x=fileRead()
    #print(x)

def fileCreate():
    file=open('/tmp/usuarios.txt','w')
    usuarios='''alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125'''
    file.write(usuarios)
    file.close()

def fileRead():
    file=open('/tmp/usuarios.txt','r')
    lista=file.readlines()
    relatorio=[]
    x=[]
    print(lista)
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(lista[i][j]=='\n'):
                relatorio.append(x)
                x=[]
            else:
                x.append(lista[i][j])
    return memoriaUsada(relatorio)



#funcao quebrada falta arrumar
def memoriaUsada(relatorio):
    for i in range (len(relatorio)):
        x=[]
        x=relatorio[i]
        x=''.join(map(str,x))
        #','.join(x)
        print(x)
        #x[2]=x[2]/1000000
        #relatorio[i]=x
        #print(x)


principal()
