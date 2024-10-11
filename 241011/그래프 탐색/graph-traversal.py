N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]

graph = [[0] for _ in range(N+1)]
# print(graph)

for i in range(len(lines)):
    vertex_1, vertex_2 = lines[i][0], lines[i][1]
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)
# print(graph)

visited = [False] * (N+1)
ans = []

def DFS(vertex):
    for curr_v in graph[vertex]:
        if curr_v != 0 and not visited[curr_v]:
            if curr_v != 1:
                ans.append(curr_v)
            visited[curr_v] = True
            DFS(curr_v)

DFS(1)
# print(ans)
print(len(ans))