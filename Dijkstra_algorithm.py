from collections import defaultdict
import numpy as np

class Undirected_Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}

    def add_node(self,name):
        self.nodes.append(name)
        
    def add_edge(self,from_node, to_node,distance):
        self.nodes.add(to_node)
        self.nodes.add(from_node)
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
		
        if from_node not in self.distances:
            self.distances[from_node]={to_node:distance}
        else:
            self.distances[from_node][to_node]=distance


        if to_node not in self.distances:
            self.distances[to_node]={from_node:distance}
        else:
            self.distances[to_node][from_node]=distance


class Directed_Graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)
        self.distances={}

    def add_node(self,name):
        self.nodes.append(name)
        
    def add_edge(self,from_node, to_node,distance):
        self.nodes.add(to_node)
        self.nodes.add(from_node)
        self.edges[from_node].append(to_node)

		
        if from_node not in self.distances:
            self.distances[from_node]={to_node:distance}
        else:
            self.distances[from_node][to_node]=distance		


def dijkstra(graph,initial_node):
    visited_path=set()
    sortest_path_wt={}
    sortest_wt=dict(zip(graph.nodes,np.repeat(np.inf,len(graph.nodes))))
    sortest_wt[initial_node]=0
            
    while initial_node:
#        print(sortest_wt,'  ', initial_node,'  ',visited_path, '\n\n')
        for e_end in graph.edges[initial_node]:
            wt=sortest_wt[initial_node]+graph.distances[initial_node][e_end]
            if wt<sortest_wt[e_end]:
                sortest_wt[e_end]=wt
                sortest_path_wt[e_end]=[initial_node,sortest_wt[e_end]]
        visited_path.add(initial_node)

        initial_node_list=[]
        for node in sorted(sortest_wt,key=sortest_wt.get,reverse=False):
            if node not in visited_path:
                initial_node_list.append(node)
        if len(initial_node_list)>=1:
            initial_node=initial_node_list[0]
        else:
            initial_node=None
#        print(initial_node_list)
         
    return visited_path,sortest_wt, sortest_path_wt
    




graph=Directed_Graph()
graph.add_edge('a','b',5)
graph.add_edge('a','c',7)
graph.add_edge('a','d',8)
graph.add_edge('b','f',12)
graph.add_edge('b','c',4)
graph.add_edge('c','d',3)
graph.add_edge('c','e',15)
graph.add_edge('d','e',10)
graph.add_edge('e','f',9)
graph.add_edge('f','g',7.5)
graph.add_edge('g','h',9.5)
graph.add_edge('g','h',9.9)
graph.add_edge('b','h',35)



p,x,y=dijkstra(graph,'c')

path_dict={}

for node in graph.nodes:
#    print(node)
    lt=[]
    i=0
    subkey=node
    while i<len(graph.nodes):
        try:
            
            key=y[subkey][0]
            lt.append(key)
            subkey=key
            i+=1
        except:
            i+=1
          
    if node not in path_dict:
        path_dict[node]=lt

        
print(path_dict)                      




        