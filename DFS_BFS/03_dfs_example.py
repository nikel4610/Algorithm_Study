# N x M 크기의 얼음 틀에 아이스크림을 만들때 나오는 아이스크림의 총 갯수
# 0은 구멍 1은 칸막이 로 막혀있는 부분
# 00110 일때 총 3개의 아이스크림이 나온다
# 00011
# 11111
# 00000

# DFS로 해결 가능하다!

# n, m을 공백으로 구분하여 받는다
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드 방문 이후 연결된 모든 노드 방문
def dfs(x ,y):
    # 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문 안했을 때
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 위치 모두 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 위치에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)

# 4 5
# 00110
# 00011
# 11111
# 00000
# 3
