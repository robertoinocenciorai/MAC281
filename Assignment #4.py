#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx        # a graph generator functions and facilities to read and write graphs in many formats

import matplotlib.pyplot as plt # a graph drawing package but basic drawing with Matplotlib as well as an interface

 
G1 = nx.Graph() # Create empty graph G for Krackhardt kite based on Assignment#4
                    # a collection of nodes (vertices) along with identified pairs of nodes

 
#Adding vertices(names) and edges number based on Assignment#4
#modified vertices to Alphabet instead of names

G1.add_node('A', pos = (2, 5))

G1.add_node('B', pos = (1, 4))

G1.add_node('C', pos = (3, 4))

G1.add_node('D', pos = (2, 3))

G1.add_node('E', pos = (1, 2))

G1.add_node('F', pos = (3, 2))

G1.add_node('G', pos = (2, 1))

G1.add_node('H', pos = (4, 3))

G1.add_node('I', pos = (5, 3))

G1.add_node('J', pos = (6, 3))

G1.add_edges_from([  ('A', 'B'), ('A', 'C'), ('A', 'G'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('E', 'D'), ('E', 'F'), ('E', 'G'), ('C', 'D'), ('C', 'H'), ('C', 'F'), ('F', 'D'), ('F', 'H'), ('F', 'G'),
('G', 'D'), ('I', 'H'), ('I', 'J') ])


pos = nx.get_node_attributes(G1, 'pos') #print/show 'edges'

nx.draw(G1, pos, with_labels = True) #print Alphabet vertices

plt.show() #show the drawing/grah created with Alphabet vertices and network package


# In[ ]:




