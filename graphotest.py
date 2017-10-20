# NETWORKX
try:
    import networkx as nx
except ImportError:
    raise ImportError("Networkx required for graph()")
except RuntimeError:
    print("Networkx unable to open")
    raise

############
import grapho
import graphoshow as oshow
import graphoscore as oscore
import graphopanda as opanda
import graphoxnet as oxnet
import graphoquery as oquery

inputFile = "cooperh.csv"
outputFile = "cooperh.gph"

dataframe = opanda.read(inputFile)
randomVarNames = opanda.getRandomVarNames(dataframe)
print "RANDOM VAR NAMES: " + str(randomVarNames)

############
# BASIC TESTS
varValueDict = opanda.getRandomVarDictionary(dataframe)
print "VAR VALUE DICTIONARY: " + str(varValueDict)

############
# NETWORK 1: x1 -> x2 -> x3
net1Name = "net1"
net1OutputFile = outputFile + "-" + net1Name

net1Graph = oxnet.getNewGraph(net1Name)
net1Graph = grapho.addRandomVarNodesToGraph(net1Graph, randomVarNames)

net1Graph.add_edge("x1", "x2")
net1Graph.add_edge("x2", "x3")
opanda.getUniqueRandomVarValues(dataframe, "x1")

net1ProductorialScore = oscore.getCooperHerscovitsBayesianScore(net1Graph, dataframe, net1Name)
print net1Name + " Productorial SCORE: " + str(net1ProductorialScore)

net1LogScore = oscore.getLogBayesianScore(net1Graph, dataframe, net1Name)
print net1Name + " Log SCORE: " + str(net1ProductorialScore)

oshow.plotGraph(net1Graph, net1OutputFile)
oshow.toString(net1Graph)
oshow.write(net1OutputFile, net1Graph)

net1Dict = opanda.getRandomVarDictionary(dataframe)
print "NET1 VAR VALUE DICTIONARY " + str(net1Dict)
x1Net1Distribution = oquery.getVarDistribution("x1", net1Dict)
print "NET1 DISTRIBUTION: " + str(x1Net1Distribution)
net1ParentDistribution = oquery.getParentsJointDistribution(["x2"], net1Dict)
print "NET1 PARENT DISTRIBUTION: " + str(net1ParentDistribution)
# xmValues = ("mx", "my")
# xnValues = ("nx", "ny")
xmValues = ("mx", "my", "mz")
xnValues = ("nx", "ny", "nz")
net1Dict["xm"] = xmValues
net1Dict["xn"] = xnValues
print "NET1 MODIFIED DICT: " + str(net1Dict)
#
net1Modified1ParentDistribution = oquery.getParentsJointDistribution(["x2"], net1Dict)
print "NET1 MODIFIED ONE PARENT DISTRIBUTION: " + str(len(net1Modified1ParentDistribution)) # + str(net1Modified1ParentDistribution)
for join in net1Modified1ParentDistribution:
    print "1x parent join: " + str(join)

net1Modified2ParentDistribution = oquery.getParentsJointDistribution(["x2", "xm"], net1Dict)
print "NET1 MODIFIED TWO PARENT DISTRIBUTION: " + str(len(net1Modified2ParentDistribution)) # + str(net1Modified2ParentDistribution)
for join in net1Modified2ParentDistribution:
    print "2x parent join: " + str(join)

net1Modified3ParentDistribution = oquery.getParentsJointDistribution(["x2", "xm", "xn"], net1Dict)
print "NET1 MODIFIED THREE PARENT DISTRIBUTION: " + str(len(net1Modified3ParentDistribution)) # + str(net1Modified3ParentDistribution)
for join in net1Modified3ParentDistribution:
    print "3x join: " + str(join)

############
# NETWORK 2: x1 -> x2, x1 -> x3
net2Name = "net2"
net2OutputFile = outputFile + "-" + net2Name

net2Graph = oxnet.getNewGraph(net2Name)
net2Graph = grapho.addRandomVarNodesToGraph(net2Graph, randomVarNames)

net2Graph.add_edge("x1", "x2")
net2Graph.add_edge("x1", "x3")

net2ProductorialScore = oscore.getCooperHerscovitsBayesianScore(net2Graph, dataframe, net2Name)
print net2Name + " Productorial SCORE: " + str(net2ProductorialScore)

net2LogScore = oscore.getLogBayesianScore(net2Graph, dataframe, net2Name)
print net2Name + " Log SCORE: " + str(net2LogScore)

oshow.plotGraph(net2Graph, net2OutputFile)
oshow.toString(net2Graph)
oshow.write(net2OutputFile, net2Graph)

############
# COMPARE ALGORITHMS
productorialComp = net1ProductorialScore/net2ProductorialScore
print "net1 better than n2? Productorial " + str(productorialComp>1)

logComp = net1ProductorialScore-net2ProductorialScore
print "net1 better than n2? Log " + str(logComp>0)


############
# VERIFY NETWORK 1: with Decisions Under Uncertainty, page 47, log formula 2.83
values = [(2, [[5, 5]]), (2, [[1, 4], [4, 1]]), (2, [[4, 1], [0, 5]])]

alphaIJ = oscore.getAlphaij0Hyperparam(values)
print "ALPHA: " + str(alphaIJ)

mIJ0 = oscore.getMij0Count(values)
print "Mij0: " + str(mIJ0)

mIJ0grouped = oscore.getMij0GroupedCount(values)
print "Mij0 grouped: " + str(mIJ0grouped)

randomVarNames = opanda.getRandomVarNames(dataframe)
n = oscore.getNumRandomVars(randomVarNames)
print "max I: " + str(n)

parents = oxnet.getRandomVarParents("x2", net1Graph)
qi = oscore.getNumRandmVarParents(parents)
print "max J with parent: " + str(qi)

parents = oxnet.getRandomVarParents("x1", net1Graph)
qi = oscore.getNumRandmVarParents(parents)
print "max J without parent: " + str(qi)

ri = oscore.getNumRandomVarValues(dataframe, "x2")
print "max K: " + str(ri)
