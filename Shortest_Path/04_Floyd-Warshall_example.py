# 1번부터 N번까지의 회사가 있는데 특정 회사끼리 서로 도로를 통해 연결되어 있다
# 1번 회사에서 시작하여 X번 회사에 방문하려고 한다
# 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램 작성

INF = int(1e9)

# 노드의 개수 및 간선 개수 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현) 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 받아 그 값으로 초기화
for _ in range(m):
    # a와 b가 서로에게 가는 비용은 1이라고 설정
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드의 최종 목적지 노드 K 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1 출력
if distance >= INF:
    print("-1")
# 도달할 수 있다면 최단 거리 출력
else:
    print(distance)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# 
# 3
