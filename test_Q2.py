import Q2 as q

def test_Q2():
	l = q.subsets_less_than_x([1, 2, 3, 4, 5], 7)
	ls = sorted([sorted(s) for s in l])
	assert ls == [[], [1], [1, 2], [1, 2, 3], [1, 3], [1, 4], [1, 5], [2], [2, 3], [2, 4], [3], [4], [5]]
