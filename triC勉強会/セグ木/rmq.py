from typing import List


class RMQ_SegmentTree:
    e = 2**31 - 1

    def __init__(self, A: List[int]) -> None:
        # 配列の大きさ以上の最小の 2 のべき乗を探す
        n = 1
        while n < len(A):
            n *= 2

        # 二分木のサイズは 2N
        self.N = n
        self.A = [self.e for _ in range(self.N * 2)]

        # Aで初期化
        for i in range(len(A)):
            self.update(i, A[i])

    def update(self, i: int, x: int) -> None:
        # iをセグ木の番号に直す
        i += self.N
        # i番目を更新
        self.A[i] = x
        # 親を辿りながら更新
        i //= 2
        while i > 0:
            self.A[i] = min(self.A[i*2], self.A[i*2 + 1])
            i //= 2

    def find(self, left: int, right: int) -> int:
        return self._find(left, right, 1, 0, self.N)

    def _find(self, left: int, right: int, i: int, a: int, b: int) -> int:
        """
        find(l, r)
        今見ているノードが i
        今見ているノードが担当している範囲が [a, b)
        """
        # 今見ている区間がクエリから完全に外れているとき
        if right <= a or b <= left:
            return self.e
        # 今見ている区間がクエリに完全に含まれているとき
        if left <= a and b <= right:
            return self.A[i]
        # 今見ている区間がクエリに一部含まれているとき
        left_value = self._find(left, right, i * 2, a, (a + b) // 2)
        right_value = self._find(left, right, i * 2 + 1, (a + b) // 2, b)
        return min(left_value, right_value)

    def debug(self) -> List[int]:
        print(self.A)


if __name__ == "__main__":
    n, q = map(int, input().split())
    A = [2**31 - 1 for _ in range(n)]

    segtree = RMQ_SegmentTree(A)

    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            segtree.update(x, y)
        else:
            ans = segtree.find(x, y + 1)
            print(ans)

    # segtree.debug()
