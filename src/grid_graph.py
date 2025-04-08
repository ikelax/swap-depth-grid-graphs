def grid_graph(n: int):
    if n < 1:
        return [[]]

    return [[(j, n - i - 1) for j in range(n)] for i in range(n)]
