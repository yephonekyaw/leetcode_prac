from collections import deque

def findCircleNum(isConnected):
    visited = [False] * len(isConnected)
    province = 0

    def dfs(node):
        visited[node] = True
        for j in range(len(isConnected)):
            if isConnected[node][j] == 1 and not visited[j]:
                dfs(j)


    for i in range(len(isConnected)):
        if not visited[i]:
            province += 1
            dfs(i)
    return province

def main():
    isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(findCircleNum(isConnected))

main()