from collections import defaultdict

def calcEquation(equations, values, queries):
    """
        {
            'a': {'b': 2.0}, 
            'b': {'a': 0.5, 'c': 3.0}, 
            'c': {'b': 0.3333333333333333}
        }
    """
    # initializing by creating relations between vertices
    graph = defaultdict(dict)
    for idx, (src, dest) in enumerate(equations):
        graph[src][dest] = values[idx]
        graph[dest][src] = 1 / values[idx]

    print(graph)

    def dfs(src, dest, res, visited):
        if src not in graph or dest not in graph:
            return -1
        if src == dest:
            return res

        if src not in visited:
            visited.append(src)
            for nei, val in graph[src].items():
                temp = dfs(nei, dest, res * val, visited)
                # if found 
                if temp != -1:
                    return temp
        return -1

    ans = []
    for src, dest in queries:
        ans.append(dfs(src, dest, 1, []))
    return ans


def main():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))


main()
