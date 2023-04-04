class Node:
    def __init__(self, id: int) -> None:
        self._id = id
        self._successor_nodes = []
        
class Arc:
    def __init__(self, from_node: Node, to_node: Node) -> None:
        self._from_node = from_node
        self._to_node = to_node

class DAG:
    def __init__(self, data) -> None:
        self._nodes = dict()
        self._arcs = []

        for from_node_id, to_node_id in data:
            f_n = None
            t_n = None
            if from_node_id not in self._nodes:
                f_n = Node(from_node_id)
                self._nodes[from_node_id] = f_n
            else:
                f_n = self._nodes[from_node_id]
            if to_node_id not in self._nodes:
                t_n = Node(to_node_id)
                self._nodes[to_node_id] =  t_n
            else:
                t_n = self._nodes[to_node_id]
            
            self._arcs.append(Arc(f_n, t_n))
            f_n._successor_nodes.append(t_n)

    def has_path_between_nodes(self, from_node_id: int, to_node_id: int) -> bool:
        pass
