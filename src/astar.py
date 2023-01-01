import queue
from copy import deepcopy


def estimated_cost(P, T):
    return abs(P[0]-T[0]) + abs(P[1]-T[1])


def cost_function(g, h, algo=0):
    if algo == 0:
        return g+h  # A*
    elif algo == 1:
        return g    # Dijkstra
    return h        # Greedy

def find_shortest_path(G, algo=0, debug=False):
    S, T, M, N = None, None, len(G), len(G[0])
    for i in range(M):
        for k in range(N):
            if S is None and G[i][k] == 'S':
                S = (i, k)
            if T is None and G[i][k] == 'T':
                T = (i, k)
    D = None
    if debug:
        D = [[None] * N for _ in range(M)]
    q, visited = queue.PriorityQueue(), {S}
    h = estimated_cost(S, T)
    q.put((cost_function(0, h, algo=algo), 0, S))
    D[S[0]][S[1]] = (cost_function(0, h, algo=algo), 0, h)
    while not q.empty():
        f, g, P = q.get()
        if P == T:
            return g, D
        x, y = P[0], P[1]
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x+dx, y+dy
            g2, P2 = g+1, (nx, ny)
            if 0 <= nx < M and 0 <= ny < N and G[nx][ny] != 'X' and P2 not in visited:
                visited.add(P2)
                h2 = estimated_cost(P2, T)
                f2 = cost_function(g2, h2, algo=algo)
                q.put((f2, g2, P2))
                D[P2[0]][P2[1]] = (f2, g2, h2)
                if P2 == T:
                    return g2, D
    return -1, D

# https://stackoverflow.com/questions/13214809/pretty-print-2d-list
def pretty_print(G):
    s = [[str(e) for e in row] for row in G]
    lens = [max(map(len, col)) for col in zip(*s)]
    max_len = max(lens)
    # fmt = '  '.join('{{:{}}}'.format(x) for x in lens)
    fmt = '  '.join(f'{{:^{max_len}}}' for _ in range(len(lens)))
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


if __name__ == "__main__":
    grids = [
        ['.', '.', '.', '.', '.', 'T', '.', '.'],
        ['.', '.', '.', 'X', 'X', 'X', 'X', '.'],
        ['.', '.', '.', 'S', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]

    for algo, name in [[0, 'A*'], [1, 'Dijkstra'], [2, 'Best-first']]:
        d, history = find_shortest_path(grids, algo=algo, debug=True)
        print(f'{name} with distance: {d}')
        history_view = deepcopy(grids)
        for i in range(len(history)):
            for k in range(len(history[0])):
                if history[i][k] is not None:
                    history_view[i][k] = ','.join(map(str, history[i][k]))
                for symbol in ['S', 'T']:
                    if grids[i][k] == symbol:
                        history_view[i][k] += f'({symbol})'
        pretty_print(grids)
        print()
        pretty_print(history_view)
        print()