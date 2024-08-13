def minReorder(n, connections):
    # I need to learn this after solving others
    T = Hashable
    Direction = bool
    Graph = Mapping[T, Iterable[tuple[T, Direction]]]

    def min_flips(graph: Graph, u: T, parent: T | None = None) -> int:
        return sum(min_flips(graph, v, u) + d for v, d in graph[u] if v != parent)

    g = defaultdict(list)
    for u, v in connections:
        g[u].append((v, True))
        g[v].append((u, False))
    return min_flips(g, 0)


def main():
    n = 10
    connections = [[0, 1], [2, 1], [3, 2], [0, 4],
                   [5, 1], [2, 6], [5, 7], [3, 8], [8, 9]]
    print(minReorder(n, connections))


main()
