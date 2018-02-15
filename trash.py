import node
import network

import operator
import random
import igraph as ig
import json
import urllib2
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout
import plotly.plotly as py
from plotly.graph_objs import *



def order_nodes(node_list, max_neighbours):
	##
	## Order the nodes present in node_list by proximity,
	## return a dictionary node to neighbours where
	## each node from the node_list is map to it's neighbours.
	##
	## -> node_list is a list of nodes object
	## -> max_neighbours is an int, number of neighbours allowed for a node
	##

	## init data structure
	node_to_node_to_distance = {}
	node_to_neighbours = {}
	
	## compute distance between nodes
	for node in node_list:
		node_to_node_to_distance[node.id] = {}
		for node_2 in node_list:
			node_to_node_to_distance[node.id][node_2.id] = abs(node.value - node_2.value)

	## get the n best neighbours
	for node in node_to_node_to_distance.keys():
		node_to_distance = node_to_node_to_distance[node]
		best_neighbours = []
		sorted_node_to_distance = sorted(node_to_distance.items(), key=operator.itemgetter(1))
		for element in sorted_node_to_distance:
			if(node != element[0] and node not in best_neighbours and len(best_neighbours) < max_neighbours):
				best_neighbours.append(element[0])
		node_to_neighbours[node] = best_neighbours

	## return the node to neighbours dictionnary
	return node_to_neighbours


def generate_random_nodes(number_of_nodes):
	##
	## Generate a random list of nodes.
	## number_of_nodes is an int, the number of nodes
	## to generate (Yeah, it's so tricky)
	##
	## return a list of nodes object
	##

	list_of_generated_nodes = []

	for x in xrange(0, number_of_nodes):
		node_id = "node_"+str(x)
		node_value = random.randint(0,100)
		n = node.Node(node_id, node_value)
		list_of_generated_nodes.append(n)

	return list_of_generated_nodes





def test_plot(data_file_name):
	##
	## IN PROGRESS
	##
	## TODO:
	##	- drop unnecesasry stuff in graphe construction
	##	- add some parameters, graphe title, color ...
	##	- deal with group stuff
	##

	## read input data
	data = []
	input_file = open(str(data_file_name), "r")
	input_data = input_file.readline()
	input_file.close()

	data = json.loads(input_data)
	N=len(data['nodes'])
	L=len(data['links'])
	Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]
	G=ig.Graph(Edges, directed=False)
	labels=[]
	group=[]
	for node in data['nodes']:
	    labels.append(node['name'])
	    group.append(node['group'])


	## Build the Graphe
	layt=G.layout('kk', dim=3)
	Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
	Yn=[layt[k][1] for k in range(N)]# y-coordinates
	Zn=[layt[k][2] for k in range(N)]# z-coordinates
	Xe=[]
	Ye=[]
	Ze=[]
	for e in Edges:
	    Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
	    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
	    Ze+=[layt[e[0]][2],layt[e[1]][2], None]



	trace1=Scatter3d(x=Xe,
	               y=Ye,
	               z=Ze,
	               mode='lines',
	               line=Line(color='rgb(125,125,125)', width=1),
	               hoverinfo='none'
	               )
	trace2=Scatter3d(x=Xn,
	               y=Yn,
	               z=Zn,
	               mode='markers',
	               name='actors',
	               marker=Marker(symbol='dot',
	                             size=6,
	                             color=group,
	                             colorscale='Viridis',
	                             line=Line(color='rgb(50,50,50)', width=0.5)
	                             ),
	               text=labels,
	               hoverinfo='text'
	               )

	axis=dict(showbackground=False,
	          showline=False,
	          zeroline=False,
	          showgrid=False,
	          showticklabels=False,
	          title=''
	          )



	layout = Layout(
	         title="Tardis",
	         width=1000,
	         height=1000,
	         showlegend=False,
	         scene=Scene(
	         xaxis=XAxis(axis),
	         yaxis=YAxis(axis),
	         zaxis=ZAxis(axis),
	        ),
	     margin=Margin(
	        t=100
	    ),
	    hovermode='closest',
	    annotations=Annotations([
	           Annotation(
	           showarrow=False,
	            text="",
	            xref='paper',
	            yref='paper',
	            x=0,
	            y=0.1,
	            xanchor='left',
	            yanchor='bottom',
	            font=Font(
	            size=14
	            )
	            )
	        ]),    )


	## plot figure
	data=Data([trace1, trace2])
	fig=Figure(data=data, layout=layout)
	plot(fig)




def create_json_file(node_to_neighbours):
	##
	## IN PROGRESS
	##
	## TODO:
	##	- create json file
	##

	print "Picvert"



##------------##
## TEST SPACE ##
##------------##

grid = network.Network("test", 3)

node_list = []

a = node.Node("tardis", 5)
b = node.Node("picvert", 4)
c = node.Node("choucroute", 6)
d = node.Node("falcon", 1)
e = node.Node("machine", 2)
f = node.Node("cheesecake", 9)

node_list.append(a)
node_list.append(b)
node_list.append(c)
node_list.append(d)
node_list.append(e)
node_list.append(f)

truc = generate_random_nodes(100)
machin = order_nodes(truc, 5)
test_plot("data_test.json")