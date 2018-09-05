import comp_set as cs

for n, k, a in [(5, 3, 4), (60, 20, 9999), (3, 2, 0), (6, 3, 19)]:
    l = cs.l_cs(n, k, a)
    assert(len(l) == k), f"wrong length: {n}, {k}, {a}"
    assert(cs.cs(n, l) == a), f"cs not roundtripping: {n}, {k}, {a}"

seen = set()
n = 20
k = 7
for a in range(cs.choose(n, k)):
    t = tuple(cs.it_cs(n, k, a))
    assert(t not in seen), f"repeated result: {n}, {k}, {a}"
    assert(cs.cs(n, t) == a), f"cs not roundtripping: {n}, {k}, {a}"
    seen.add(t)


orange = lambda s: list(range(s))
for n, l in [(10, orange(5)), (30, orange(4)), (100, []), (40, orange(40)), (5, [1, 3, 4]), (10, [0, 4, 5, 8, 9])]:
    a = cs.cs(n, l)
    assert(a < cs.choose(n, len(l))), f"cs out of bounds: {n}, {l}, {a}"
    assert(cs.l_cs(n, len(l), a) == l), f"cs not roundtripping: {n}, {l}, {a}"

print("all tests succeeded")
