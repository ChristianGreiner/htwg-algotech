verticies = 4
INF = 999

def floyd(graph):
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))
    for r in range(verticies):
        for j in range(verticies):
            for k in range(verticies):
                dist[j][k] = min(dist[j][k], dist[j][r] + dist[r][k])

    return dist

graph = [
    [0, 5, INF, INF],
    [50, 0, 15, 5],
    [30, INF, 0, 15],
    [15, INF, 5, 0]
]
dist = floyd(graph)

print("----------------------------")
for p in range(verticies):
    for q in range(verticies):
        if(dist[p][q] == INF):
            print("INF", end=" ")
        else:
            print(dist[p][q], end="  ")
    print(" ")
print("----------------------------")
