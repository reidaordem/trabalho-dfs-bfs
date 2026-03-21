
import sys
from graph import Graph
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths

estados_nordeste = {
    "AL":0,
    "BA":1,
    "CE":2,
    "MA":3,
    "PB":4,
    "PE":5,
    "PI":6,
    "RN":7,
    "SE":8,
}


f = open(r"C:\Users\Usuario\Desktop\trabalho-dfs-bfs\trabalho-dfs-bfs\dados\nordeste.txt")
s = 0
V = int(f.readline())
E = int(f.readline())

g = Graph(V)
for i in range(E):
    v, w = f.readline().split()
    g.add_edge(v, w)

print("Digite as siglas dos Estados em caixa alta , exemplo: CE")
X = input("ESTADO DE ORIGEM: ")
Y = input("ESTADO DE DESTINO: ")



x = estados_nordeste[X]
y = estados_nordeste[Y]

dfs = DepthFirstPaths(g, x)
bfs = BreadthFirstPaths(g, x)

print("1. É possível sair do estado de origem X e chegar ao estado de destino Y atravessando apenas fronteiras terrestres?", end="\n")
if dfs.has_path_to(y):
    print("COM DFS: sim, é possivel chegar")
else:
    print("COM DFS: não é possivel chegar")

if bfs.has_path_to(y):
    print("COM BFS: sim, é possivel chegar")
else:
    print("COM BFS: não é possivel chegar")


print("2. Qual caminho foi encontrado pela DFS do estado de origem X até o estado de destino Y?",end="\n")
if dfs.has_path_to(y):
    print("caminho encontrado pelo DFS",dfs.path_to(y))
else:
    print("não existe caminho ")


print("3. Qual caminho foi encontrado pela BFS do estado de origem X até o estado de destino Y?",end="\n")

if bfs.has_path_to(y):
    print("caminho encontrado pelo BFS", bfs.path_to(y))
else:
    print("não existe caminho")


print("4. Quais estados são alcançáveis a partir do estado de origem X?",end="\n")
print("COM DFS")
for v in range(len(dfs.marked)):
    if dfs.marked[v]:
        print(v)

print("\n")

print("4. Quais estados são alcançáveis a partir do estado de origem X?",end="\n")
print("COM BFS")
for v in range(len(bfs._marked)):
    if bfs._marked[v]:
        print(v)



print("5. Qual foi a ordem de visita dos estados na execução da DFS a partir de X?",end="\n")
print(dfs.visit_order)






print("6. Qual foi a ordem de visita dos estados na execução da BFS a partir de X?",end="\n")
print(bfs.visit_order)