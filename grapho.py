# https://networkx.github.io/documentation/networkx-1.9/tutorial/tutorial.html
import networkx as nx

# NETWORKX
try:
    import networkx as nx
except ImportError:
    raise ImportError("Networkx required for graph()")
except RuntimeError:
    print("Networkx unable to open")
    raise

# MATPLOTLIB
try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib required for draw()")
except RuntimeError:
    print("Matplotlib unable to open")
    raise


# SYSTEM
try:
    import sys
except ImportError:
    raise ImportError("SYS required for ARGUMENTS()")
except RuntimeError:
    print("SYS unable to open")
    raise

# CSV
try:
    import csv
except ImportError:
    raise ImportError("CSV required for read()")
except RuntimeError:
    print("CSV unable to open")
    raise

# PANDAS
try:
    import pandas as pd
except ImportError:
    raise ImportError("PANDAS required for read()")
except RuntimeError:
    print("PANDAS unable to open")
    raise

# GRAPH: that is used to find best
# initialGraph = nx.DiGraph()

# COMPUTE: method called to perform the whole job
# TODO: output both png and gph files
def compute(infile, outfile):
    graph = read(infile)
    plotGraph(graph, outfile + ".png")
    toString(graph)
    write(outfile)
    pass

# READ: a dataframe from a CSV inputfile
def read(infile):
    inputDF = getInputDF(infile)
    graph = getNewGraph("first")
    graph = addGraphNodes(graph, inputDF)
    return graph
    # print(graph.node['fare'])
    # nx.connected_components(graph)
    # graph.adj

    #print(inputDF)

    # .values
    # df.head()
    pass

# Graph vs DiGraph
# name=graphName
def getNewGraph(graphName):
    graph = nx.Graph(name=graphName)
    return graph


def query(dataframe):
    #print(inputDF.loc[(inputDF['age']==1) & (inputDF['sex']==2)])
    #print(inputDF.loc[(inputDF['age']==1) & (inputDF['sex']==2)][['age', 'sex']])
    pass

# READ: get dataframe, inferring columns
def getInputDF(infile):
    inputDF = pd.read_csv(infile, header='infer')
    return inputDF

def addGraphNodes(graph, dataframe):
    for col in list(dataframe):
        # len()
        unique = dataframe[col].unique()
        print"{} \t\t UNIQUE: \t\t {} ".format(col, unique)
        graph.add_node(col)
        # graph.add_edge('age', col)
        #graph.add_nodes_from([2, 3])
        #print(dataframe.col)
    return graph


# WRITE: a gph output file
def write(outfile):
    with open(outfile, 'wb') as csvfile:
        gph_writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        gph_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
        gph_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    pass

def analizeGraph(graph):
    # degree()
    nx.connected_components
    # graph.adj

# PRINT nodes, graphs, edges, neighbors
def toString(graph):
    print "GRAPH: {} ".format(graph.graph)
    print "NODES: {}".format(graph.nodes())
    print "EDGES: {}".format(graph.edges())
    for node in graph.nodes():
        print "{} EDGES: {}".format(node, graph[node])
        print "{} NEIGHTBORS: {}".format(node, graph.neighbors(node))

# PLOT graph: nodes, edges, labesl
def plotGraph(graph, filename):
    # POSITIONS
    pos = nx.spring_layout(graph)  # positions for all nodes
    # NODES
    nx.draw_networkx_nodes(graph, pos,
                           nodelist=graph.nodes(),
                           node_color='r', node_size=500) # alpha=0.8,
    # EDGES
    nx.draw_networkx_edges(graph, pos,
                           edgelist=graph.edges(),
                           edge_color='b') # alpha=0.5, width=8,
    # LABELS
    labels = {}
    for node in graph.nodes():
        labels[str(node)] = str(node)
    nx.draw_networkx_labels(graph, pos, labels, font_size=10)
    # DRAW ALL
    plt.axis('off')
    plt.savefig(filename)
    # plt.show()


# FUTURE WORK
#