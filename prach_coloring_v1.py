import dwavebinarycsp
import time
from hybrid.reference.kerberos import KerberosSampler
import dwave_networkx as dnx
import pickle as pickle

from utilities import visualize_map

with open('G_800_6.pkl', 'rb') as f:
    G = pickle.load(f)


start_time_is = time.time() 
solution = dnx.algorithms.coloring.min_vertex_color(G,KerberosSampler(), max_iter=100, max_time=None, convergence=3, energy_threshold=None,
             sa_reads=1, sa_sweeps=10000, tabu_timeout=500,
             qpu_reads=100, qpu_sampler=None, qpu_params=None,
             max_subproblem_size=50)
end_time_is = time.time()
elapsed_is = end_time_is - start_time_is

#print(solution)
print(elapsed_is)
print(dnx.algorithms.coloring.is_vertex_coloring(G, solution))
print(len(set(solution.values())))
