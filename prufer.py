
from copy import deepcopy
class pruferTree:
	def __init__(self):
		self.edges = []
	def printTree(self):
		print self.edges


def smallestInMandNotInS(s, m):
	# for each value in m
	for index,value in enumerate(m):
		inS = False
		for i in s:
			# if m[index] is in s
			if i == value:
				inS = True # let us know
		# if m[index] is not in s
		if inS == False:
			return index,value
			

def convertPruferToTree(s):
	newTree = pruferTree()
	m = []
	# make m
	listHolder = deepcopy(s)
	for i in range(len(s)+2):
		m.append(i+1)

	# loop thru s
	for i in range(len(s)):
		# get the smallest element of M, that is not in S
		PopMe, VertexTwo = smallestInMandNotInS(listHolder,m)
		# and the first element in s
		VertexOne = listHolder[0]

		# make this a new edge
		newTree.edges.append([VertexOne,VertexTwo])

		# remove both m[0] and s[0]
		listHolder.pop(0)
		m.pop(PopMe)

	newTree.edges.append([m[0],m[1]])
	return newTree


def TreeToEccentricitySet(pTree):
	# make eccentricity set for each point
	
	nodeConnectionDictionary = {}
	for edge in pTree.edges:
		for node in edge:
			# if point is in set, increment its key->value
			if node in nodeConnectionDictionary.keys():
				nodeConnectionDictionary[node] += 1
			# else add to set with value of 1
			else:
				nodeConnectionDictionary.update({node: 1})
	return nodeConnectionDictionary


def getMinKeywithMinValueFromDict(dictionary):
	my_list = dictionary.items()

	sorted_my_list = sorted(my_list, key=lambda x: x[1])
	min_value = 10000000
	min_key = ""
	for i in sorted_my_list:
		if i[1] < min_value:
			min_value = i[1]
			min_key = i[0]
		elif i[1] == min_value:
			if i[0] < min_key:
				min_key = i[0]
	return min_key


def getConnectedToJ(graph, j):
	# if there is a node in the graph that is connected to j
	#	 return that node
	for i in graph.edges:
		if i[0] == j:
			return i[1]
		elif i[1] == j:
			return i[0]


def removeEdgeWithJ(graph, j):

	for edge in range(0,len(graph.edges)-1):
		for node in range(0,len(graph.edges[edge])-1):
			if graph.edges[edge][0] == j or graph.edges[edge][1] == j:
				del graph.edges[edge]
				return graph
								

def convertTreeToSequence(pTree):

	
	# get connectivity dictionary
	nodeConnectionDictionary = TreeToEccentricitySet(pTree)

	# make copy of tree
	treeCopy = deepcopy(pTree)

	pruferSequence = []

	# while tree has greater than 2 nodes (or 1 edge)
	while len(treeCopy.edges) > 1 :
	#	get node j with both lowest value (i.e. node number) and lowest eccentricity
		j = getMinKeywithMinValueFromDict(nodeConnectionDictionary)
	#	add the node that j is connected to end of list
		connectedtoj = getConnectedToJ(treeCopy,j)
		pruferSequence.append(connectedtoj)
	#	remove j from tree (remove edge connecting j to the tree)
		newtree = removeEdgeWithJ(treeCopy, j)
		treeCopy = deepcopy(newtree)

		#update dictionary
		nodeConnectionDictionary = TreeToEccentricitySet(treeCopy)

	return pruferSequence


def main():
	l = [2,2,2,1]
	print "initial sequence  " + str(l)
	pTree = convertPruferToTree(l)
	print "convert to tree  ",
	pTree.printTree()
	pSequence = convertTreeToSequence(pTree)
	print "back to sequeunce " + str(pSequence)



if __name__ == "__main__":
	main()