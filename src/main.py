
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


f = open(r"C:\Users\alunok11.UNIFOR\Desktop\trabalho-dfs-bfs\dados\nordeste.txt")
s = 0
V = int(f.readline())
E = int(f.readline())

g = Graph(V)
for i in range(E):
    v, w = f.readline().split()
    g.add_edge(v, w)

dfs = DepthFirstPaths(g, s)
bfs = BreadthFirstPaths(g, s)

X = input("ESTADO DE ORIGEM: ")
Y = input("ESTADO DE DESTINO: ")

x = estados_nordeste[X]
y = estados_nordeste[Y]

print("1. ", end="")
if dfs.has_path_to(y):
    print("sim, é possivel chegar")
else:
    print("não é possivel chegar")
