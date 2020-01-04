import networkx as nx
# import matplotlib.pyplot as plt

def dijkstra_as_networkx(a, b):     #функция для поиска минимального расстояния между двумя вершинами
    global graph
    distance = nx.single_source_dijkstra(graph, a, b)
    return (distance)

def search_of_degree(a):    #поиск степени вершины
    global array_0
    global array_1
    count = 0
    for i in array_0:
        if i == a:
            count += 1
    for j in array_1:
        if j == a:
            count += 1
    return count

# def search_of_min_distance(a, b):       #функция для поиска минимального расстояния между двумя вершинами
#     global dict
#     count = 0
#     stack = []
#     visited = []
#     visited.append(a)
#     stack.extend(dict[a])
#     flag = True
#     while flag:
#         if count != 999 or not(b in stack):
#             visited.append(stack[0])
#             key = visited[len(visited) - 1]
#             stack.extend(dict[key])
#             stack = list(set(stack) - set(visited))
#             count += 1
#         else:
#             flag = False
#     return count + 1

in_file = open("check_graph", "r")
out_file = open("lab5_out", "w")

array_1 = []      #изначальный массив
array = []      #изначальный массив v.2.0
revers_array = []       #reversed(изначальный массив)

for i in range(0, 2461):
    i = list(map(int, in_file.readline().split()))      #заношу в массив данные из файла
    revers_array.append(list(reversed(i)))
    array_1.append(i)

symbols = [422, 905, 458, 622, 276, 788, 982, 957]      #символы для удаления

for i in range(len(array_1) - 1):
    if not((array_1[i][0] % 17 == 0 or array_1[i][0] in symbols) or (array_1[i][1] % 17 == 0 or array_1[i][1] in symbols)):
        array.append(array_1[i])

print("amount of edges in a graph : \n", len(array), file=out_file)     #вывожу кол-во ребер

array_0 = []    #массив для эллементов из array c indx 0
array_1 = []    #массив для эллементов из array c indx 1
check = []      #все вершины, которые не являются изолятами
flushed_array = []      #массив изолятов

for i in range(len(array) - 1):
    array_0.append(array[i][0])
    array_1.append(array[i][1])

help_array = list(set(array_1 + array_0))
mass_1_999 = [i for i in range(1000)]

for i in mass_1_999:        #поиск изолятов
    if i in help_array or i in symbols or i % 17 == 0:
    # if i in help_array:
        j = "opa"
    else:
        flushed_array.append(i)

print("flushed_array : \n", flushed_array, file=out_file)

top_degree = []     #массив в формате [вершина, ее степень]
out_top_degree = []
max_degree = 0
max_top = 0
for i in help_array:
    degree = search_of_degree(i)    #заполняю массив значениями в формате [вершина, ее степень]
    top_degree.append([i, degree])
    if degree > max_degree:
        max_degree = degree
        max_top = i

out_top_degree.append([max_top, max_degree])

for i in range(len(top_degree) - 1):
    if top_degree[i][1] == max_degree and top_degree[i][0] != max_top:  #проверяю массив на наличие вершин с max degree
        out_top_degree.append(top_degree[i])

print("array of tops with max degree : \n", out_top_degree, file=out_file)

# dict = {x: [] for x in help_array}    #словарь в format : {key = врешина : [все связанные с ней вершины]}
# for i in array:
#     if i[0] in dict:
#         dict[i[0]].append(i[1])     #заношу в словарь все связанные вершины
# for j in revers_array:
#     if j[0] in dict and j[1] not in dict[j[0]]:     #заношу в словарь все связанные вершины
#         dict[j[0]].append(j[1])
# print("dict : \n", dict, file=out_file)

graph = nx.MultiGraph()     #создаю граф с помощью networkX
for i in array:
    graph.add_edge(i[0], i[1], distance=1)      #заполняю граф
graph = graph.to_undirected()

print("graph diameter : \n", nx.diameter(graph), file=out_file)     #нахожу диаметр графа
print("distance between 681, 774 : \n", dijkstra_as_networkx(681, 774), file=out_file)
print("distance between 818, 628 : \n", dijkstra_as_networkx(818, 628), file=out_file)
print("distance between 878, 244 : \n", dijkstra_as_networkx(878, 244), file=out_file)

# min_max_distance = -1
# k = 0
# distance_array = []
# for i in array_0:
#     for j in array_1:
#         distance_array.append(dijkstra_as_networkx(i, j))
#         k += 1
#     print(k, distance_array)
#
# for i in distance_array:
#     if i > min_max_distance:
#         min_max_distance = i
#
# print("graph diameter = ", min_max_distance)

