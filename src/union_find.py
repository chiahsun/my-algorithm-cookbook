class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.cnt = [1] * N

    def make_union(self, a, b):
        ra, rb = self.find_root(a), self.find_root(b)
        if ra == rb:
            return
        if self.cnt[ra] < self.cnt[rb]:
            ra, rb = rb, ra
        self.cnt[ra] += self.cnt[rb]
        self.parent[rb] = ra

    def find_root(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a


if __name__ == "__main__":
    uf = UnionFind(6)
    uf.make_union(1, 2)
    uf.make_union(2, 3)
    uf.make_union(4, 5)
    assert uf.find_root(0) != uf.find_root(1)
    assert uf.find_root(0) != uf.find_root(4)
    assert uf.find_root(1) == uf.find_root(2)
    assert uf.find_root(2) == uf.find_root(3)
    assert uf.find_root(4) == uf.find_root(5)
    assert uf.find_root(1) != uf.find_root(4)

