import networkx as nx
from operator import itemgetter


def get_name(namelist):
	result = ""
	for word in namelist:
		result += word.decode("utf-8")
		result += ' '
	return result


f = open('ownership.txt', 'r')
names = open('names.txt', 'rb')
# name_dict maps node id to company name
name_dict = {}

for line in names:
	line = line.split()
	if len(line) > 1:
		name_dict[line[-1].decode("utf-8")] = line[0:-1]
G = nx.DiGraph()

# create graph G where directed edge from A to B means A is owned by B
for line in f:
	edge = line.split()
	G.add_edge(edge[1], edge[0])

# calculate pagerank of G, return dict mapping node to pagerank
pagerank = nx.pagerank(G)

# sort pagerank by values and get top and bottom 10 results
sorted_pr = sorted(pagerank.items(), key = itemgetter(1), reverse = True)
top_10 = sorted_pr[0:10]
bottom_10 = sorted_pr[-10:]

# print results
print("Top 10 most influential companies by pagerank:")
for i in top_10:
	print(get_name(name_dict[i[0]]), ": pagerank = ", i[1])

print()

print("Top 10 least influential companies by pagerank:")
for i in bottom_10:
	print(get_name(name_dict[i[0]]), ": pagerank = ", i[1])


