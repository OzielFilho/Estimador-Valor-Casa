import numpy as np

# Abre o arquivo e coloca cada linha em uma lista
l = []
arquivo = open('housing-train (1).csv')
for i in range(333):
    x = arquivo.readline()
    g = x.strip().split(',')
    l.append(g)
    l[i] = list(map(float, l[i]))
#Separando os que eu preciso

id = []
medv = []
Usar = []
for i in range(len(l)):
    Usar.append(l[i][1:2]+l[i][3:14])
    medv.append(l[i][14])
    id.append(l[i][0])
# Ajeita os valores da lista
def Avl(l):
    minimo = np.min(l, axis=0)
    maximo = np.max(l, axis=0)
    rng = maximo - minimo
    mm = l / rng
    return np.c_[np.ones(len(mm)), mm]

#Criar uma lista com os pesos
P = [1]*len(l[0])

# Valor estimado e ajeita os pesos
v = []
Al = np.array(l)
medv = np.array(medv)

for i in range(100):
    for j in range(333):
        Ve = sum(P * Al[i])

        e = Ve - medv[i]

        P = P - 0.000001 * e * Ve

for i in range(333):
    Ve = sum(P * Al[i])
    v.append(Ve)

# Criar e ler os arquivos csv

doc = open('New.csv', 'w')
txt = 'cabeçalho\n'
for i in range(333):

    txt += '{},{}\n'.format(id[i], v[i])
doc.writelines(txt)
doc.close()


