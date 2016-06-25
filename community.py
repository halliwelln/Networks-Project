from itertools import combinations

import igraph
import optparse

parser = optparse.OptionParser(usage="%prog [options] infile")
parser.add_option("-k", metavar="K", default=3, type=int,
        help="use a clique size of K")

options, args = parser.parse_args()

g = igraph.Graph.Erdos_Renyi(100, 0.5 , directed=False, loops=False)
k = 3
if not args:
    parser.error("Required input file as first argument")

k = options.k
g = igraph.load(args[0], format="ncol", directed=False)
cls = map(set, g.maximal_cliques(min=k))

edgelist = []
for i, j in combinations(range(len(cls)), 2):
    if len(cls[i].intersection(cls[j])) >= k-1:
        edgelist.append((i, j))

cg = igraph.Graph(edgelist, directed=False)
clusters = cg.clusters()
for cluster in clusters:
    members = set()
    for i in cluster:
        members.update(cls[i])
 
print "\t".join(g.vs[members]["members"])


print g.vs[members][0]