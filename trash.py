import node
import network


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

def order_nodes(node_list):
	##
	## IN PROGRESS 
	##

	node_to_node_to_distance = {}

	for node in node_list:
		node_to_node_to_distance[node.id] = {}
		for node_2 in node_list:
			node_to_node_to_distance[node.id][node_2.id] = abs(node.value - node_2.value)



	print node_to_node_to_distance



order_nodes(node_list)