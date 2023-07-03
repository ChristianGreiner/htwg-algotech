INF = 999

def floyd(graph):
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))
    for r in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
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
for p in range(len(graph)):
    for q in range(len(graph)):
        if(dist[p][q] == INF):
            print("INF", end=" ")
        else:
            print(dist[p][q], end="  ")
    print(" ")
print("----------------------------")
