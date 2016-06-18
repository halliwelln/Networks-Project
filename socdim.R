setwd("~/Desktop")
library(igraph)
set.seed(123)
#load data
nodes <- read.csv("flickr-nodes.csv", header = FALSE)
edges <- read.csv("flickr-edges.csv", header=FALSE)
groups <- as.vector(read.csv("flickr-groups.csv", header=FALSE))
group.edges <- as.vector(read.csv("flickr-group-edges.csv", header=FALSE))

#create graph object
get.graph <- graph_from_data_frame(edges, vertices=nodes, directed = FALSE)

#create adjacency matrix
adjacency <- get.adjacency(get.graph)

#create modularity matrix
cluster <- cluster_leading_eigen(get.graph)
modularity.matrix <- mod.matrix(get.graph, membership=cluster$membership)

#eigen
get.eigen <- eigen(modularity.matrix)$vectors
get.eigen <- get.eigen[,1:500]

write.csv(get.eigen, file="data.csv")