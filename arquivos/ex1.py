#encoding: utf-8
def principal():
    fileCreate()
    x=fileRead()
    formata(x)

def fileCreate():
    file=open('/tmp/usuarios.txt','w')
    usuarios='''alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
'''
    file.write(usuarios)
    file.close()

def fileRead():
    file=open('/tmp/usuarios.txt','r')
    lista=file.readlines()
    relatorio=[]
    x=[]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if(lista[i][j]=='\n'):
                relatorio.append(x)
                x=[]
            else:
                x.append(lista[i][j])
    file.close()
    return memoriaUsada(relatorio)



#funcao quebrada falta arrumar
def memoriaUsada(relatorio):
    totalMemoria=0
    for i in range (len(relatorio)):
        x=[]
        m=[]
        novo=[]
        x=relatorio[i]
        x=''.join(map(str,x))
        m=x[15:-1]
        m=float(m)
        m=m/(100000)
        x=x[0:15]
        totalMemoria=totalMemoria+m
        novo.append(x)
        novo.append(m)
        relatorio[i]=novo
    return pctMemoria(totalMemoria,relatorio)

def pctMemoria(totalMemoria,relatorio):
    for i in range (len(relatorio)):
        pct=[]
        pct=(relatorio[i][1]/totalMemoria)*100
        relatorio[i].append(pct)
    return relatorio

def formata(x):
    file=open('/tmp/usuarios.txt','w')
    formato='''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''
    file.write(formato)
    for i in range (len(x)):
        #formato='''{i+1}   {x[i][0]}        {x[i][1]}     %{x[i][2]}
#'''
        formato='''{}   {}        {}     %{}
        '''.format((i),(x[i][0]),(x[i][1]),(x[i][2]))
        file.write(formato)
    file.close()


principal()
