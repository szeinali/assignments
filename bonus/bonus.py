import networkx as nx


def jaccard_wt(graph, node):
  """
  The weighted jaccard score, defined above.
  Args:
    graph....a networkx graph
    node.....a node to score potential new edges for.
  Returns:
    A list of ((node, ni), score) tuples, representing the 
              score assigned to edge (node, ni)
              (note the edge order)
  """
    a_neighbors = graph.neighbors(node)
    a_degrees = graph.degree(a_neighbors)
    a_degree_sum = sum(a_degrees.values())
    jaccard_list = []
    
    for n in graph.nodes():
        if n is not node and not graph.has_edge(n,node):
            b_neighbors = graph.neighbors(n)
            b_degrees = graph.degree(b_neighbors)
            b_degree_sum = sum(b_degrees.values())
            if(n&node != 0):
                ab_neighbors = graph.neighbors(n & node)
                ab_degrees = graph.degree(ab_neighbors)
                ab_degree_sum = sum(ab_degrees.values())
                jaccard_score = (1.0/ab_degree_sum)/((1.0/b_degree_sum)*(1.0/a_degree_sum))
            else:
                jaccard_score = 0
            jaccard_list.append(((node, n),jaccard_score))
           
    return jaccard_list
