import dwavebinarycsp
from hybrid.reference.kerberos import KerberosSampler
from dimod import RandomSampler
import time
import dwave_networkx as dnx
import networkx as nx

G=nx.Graph()
G.add_nodes_from(['L1','L2','L3', 'L4'])
G.add_edges_from([('L1','L2'),('L2','L3'), ('L3','L4'), ('L4','L1')])

print(G.nodes)
print(G.edges)
solution = dnx.algorithms.coloring.min_vertex_color(G,KerberosSampler())
print(solution)
print(set(solution.values()))
# Solve BQM
#solution = KerberosSampler().sample(bqm)


#solution = dnx.algorithms.coloring.min_vertex_color(G, RandomSampler())
#print(bqm)
#solution = RandomSampler.sample(bqm)
#best_solution = solution.first.sample
