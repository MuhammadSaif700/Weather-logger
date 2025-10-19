import sys
from collections import defaultdict

def solve_one(A, B):
    n = len(A)
    # Quick impossible checks
    for i in range(n):
        if A[i] > B[i]:
            return None  # impossible
    # need[v] = list of indices that must be changed to v (1-based indices)
    need = defaultdict(list)
    for i, bv in enumerate(B, start=1):
        if A[i-1] != bv:
            need[bv].append(i)
    # every value in need must exist in initial A
    setA = set(A)
    for v in need:
        if v not in setA:
            return None
    # cur[v] = list of indices that currently have value v (start with initial A)
    cur = defaultdict(list)
    for i, av in enumerate(A, start=1):
        cur[av].append(i)
    ops = []
    # process required values in ascending order
    for v in sorted(need.keys()):
        if not cur.get(v):
            return None
        source = cur[v][-1]  # pick any current index that has temperature v
        for target in need[v]:
            # perform operation: warm up target (colder) to source (hotter)
            ops.append((source, target))
            cur[v].append(target)  # now target also has value v
    return ops

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for tc in range(1, T+1):
        n = int(next(it))
        A = [int(next(it)) for _ in range(n)]
        B = [int(next(it)) for _ in range(n)]
        ops = solve_one(A, B)
        if ops is None:
            out_lines.append(f"Case #{tc}: -1")
        else:
            out_lines.append(f"Case #{tc}: {len(ops)}")
            for s, t in ops:
                out_lines.append(f"{s} {t}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
