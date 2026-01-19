from itertools import product

def main():
    K, L, M, N = map(int, input().split())
    q = int(input())

    sources = set()
    for _ in range(q):
        x, y, z, w = map(int, input().split())
        sources.add((x, y, z, w))

    offsets = [(dx, dy, dz, dw)
               for dx, dy, dz, dw in product((-1, 0, 1), repeat=4)
               if not (dx == dy == dz == dw == 0)]

    sum_neigh = 0
    adj = 0

    for x, y, z, w in sources:
        cx = min(K, x + 1) - max(1, x - 1) + 1
        cy = min(L, y + 1) - max(1, y - 1) + 1
        cz = min(M, z + 1) - max(1, z - 1) + 1
        cw = min(N, w + 1) - max(1, w - 1) + 1

        cube = cx * cy * cz * cw
        sum_neigh += cube - 1

        for dx, dy, dz, dw in offsets:
            nx, ny, nz, nw = x + dx, y + dy, z + dz, w + dw
            if 1 <= nx <= K and 1 <= ny <= L and 1 <= nz <= M and 1 <= nw <= N:
                if (nx, ny, nz, nw) in sources:
                    adj += 1

    print(sum_neigh - adj)

if __name__ == "__main__":
    main()

