import grapho
import graphoshow as oshow

# NETWORKX
try:
    import networkx as nx
except ImportError:
    raise ImportError("Networkx required for graph()")
except RuntimeError:
    print("Networkx unable to open")
    raise


inputFile = "cooperh.csv"
outputFile = "cooperh.gph"

# grapho.compute("cooperh.csv", "cooperh.gph")

inputDF = grapho.read(inputFile)

# NETWORK 1: x1 -> x2 -> x3
net1Name = "net1"
net1OutputFile = outputFile + "-" + net1Name

net1Graph = grapho.getNewGraph(net1Name)
net1Graph = grapho.addRandomVarNodesToGraph(net1Graph, inputDF)

net1Graph.add_edge("x1", "x2")
net1Graph.add_edge("x2", "x3")

oshow.plotGraph(net1Graph, net1OutputFile)
oshow.toString(net1Graph)
oshow.write(net1OutputFile, net1Graph)

# NETWORK 2: x1 -> x2, x1 -> x3
net2Name = "net2"
net2OutputFile = outputFile + "-" + net2Name

net2Graph = grapho.getNewGraph(net2Name)
net2Graph = grapho.addRandomVarNodesToGraph(net2Graph, inputDF)

net2Graph.add_edge("x1", "x2")
net2Graph.add_edge("x1", "x3")

oshow.plotGraph(net2Graph, net2OutputFile)
oshow.toString(net2Graph)
oshow.write(net2OutputFile, net2Graph)
