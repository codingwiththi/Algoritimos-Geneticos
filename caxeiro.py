from sys import maxsize
num_v = 5
all_cam = {}
out = []


def caxeiroViajante(graph, s):
    vertex = []

    for i in range(num_v):
        if i != s:
            vertex.append(i)

    # all_vertex.append(vertex)
    caminho_min = maxsize
    while True:
        custo_atual = 0
        k = start
        for i in range(len(vertex)):
            custo_atual += graph[k][vertex[i]]
            k = vertex[i]
        custo_atual += graph[k][s]
        caminho_min = min(caminho_min, custo_atual)
        out = vertex[:]
        all_cam[custo_atual] = out

        if not permutacao(vertex):
            break

    return caminho_min


def permutacao(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True


graph = [[0, 2, 9, 3, 6], [2, 0, 4, 3, 8], [
    9, 4, 0, 7, 3], [3, 3, 7, 0, 3], [6, 8, 3, 3, 0]]

start = 0

res = caxeiroViajante(graph, start)
print(res)
# print(all_cam)
print(all_cam[res])
