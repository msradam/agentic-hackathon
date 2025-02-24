import os
import networkx as nx
import nx_arangodb as nxadb
import osmnx as ox

# Safe to use these secrets, since these are default vals for ArongoDB ocontainer
os.environ["DATABASE_HOST"] = "http://localhost:8529"
os.environ["DATABASE_USERNAME"] = "root"
os.environ["DATABASE_PASSWORD"] = "openSesame"
os.environ["DATABASE_NAME"] = "_system"

# OSMNX assembles the graph from a geoquery
G_nx = ox.graph_from_place("Forest Hills, Queens, NY", network_type='all', simplify=True)
G = nxadb.Graph(incoming_graph_data=G_nx,name="QueensGraph")

# G = nxadb.Graph(name="MyGraph")

# G.add_node(1, foo='bar')
# G.add_node(2, bar='foo')
# G.add_edge(1, 2, weight=2)

# res = nx.pagerank(G)

# for k, v in res.items():
#     G.nodes[k]['pagerank'] = v