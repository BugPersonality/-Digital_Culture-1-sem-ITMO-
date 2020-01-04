import networkx as nx
import matplotlib.pyplot as plt


in_file = open("check_graph", "r")
out_file = open("lab5_out", "w")

array = []      #изначальный массив
revers_array = []       #reversed(изначальный массив)

for i in range(0, 2537):
    i = list(map(int, in_file.readline().split()))      #заношу в массив данные из файла
    revers_array.append(list(reversed(i)))
    array.append(i)

array_0 = []    #массив для эллементов из array c indx 0
array_1 = []    #массив для эллементов из array c indx 1
check = []      #все вершины, которые не являются изолятами

for i in range(len(array) - 1):
    array_0.append(array[i][0])
    array_1.append(array[i][1])

help_array = list(set(array_1 + array_0))

dict = {x: [] for x in help_array}    #словарь в format : {key = врешина : [все связанные с ней вершины]}
for i in array:
    if i[0] in dict:
        dict[i[0]].append(i[1])     #заношу в словарь все связанные вершины
for j in revers_array:
    if j[0] in dict and j[1] not in dict[j[0]]:     #заношу в словарь все связанные вершины
        dict[j[0]].append(j[1])

print(dict)

g = nx.MultiGraph()
for i in array:
    g.add_edge(i[0], i[1], distance=1)
print("робит ? : ", nx.single_source_dijkstra(g, 0, 94))

pos = nx.draw_circular(g, with_labels=True)

fig = plt.gcf()
fig.set_size_inches(20, 20, forward=True)

plt.title("Граф digital culture")
plt.savefig('graph.png')
plt.show()
