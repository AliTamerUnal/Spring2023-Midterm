import Q3 as q

def test_Q3_1():
	d = q.DAG([(1,2), (2,3), (1,3), (3,4)])
	assert d.has_path_between_nodes(1,4) == True

def test_Q3_2():
	d = q.DAG([(1,2), (2,3), (1,3), (3,4)])
	assert d.has_path_between_nodes(2,1) == False