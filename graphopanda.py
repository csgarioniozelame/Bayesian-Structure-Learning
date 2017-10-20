# Operate on Python Pandas dataframe


# PANDAS
try:
    import pandas as pd
except ImportError:
    raise ImportError("PANDAS required for filter()")
except RuntimeError:
    print("PANDAS unable to open")
    raise

# CSV
try:
    import csv
except ImportError:
    raise ImportError("CSV required for read()")
except RuntimeError:
    print("CSV unable to open")
    raise


import graphoquery as oquery

# READ: a dataframe from a CSV inputfile
def read(infile):
    inputDF = getInputDF(infile)
    return inputDF

# READ: get dataframe, inferring columns
def getInputDF(infile):
    inputDF = pd.read_csv(infile, header='infer')
    return inputDF

def getRandomVarNames(dataframe):
    varNames = list(dataframe)
    # print "Var NAMES: " + str(varNames)
    return varNames

### VAR VALUES: get possible values from the dataset
def getUniqueRandomVarValues(dataframe, varName):
    unique = dataframe[varName].unique()
    # print"{} \t\t UNIQUE: \t\t {} ".format(str(varName), str(unique))
    return unique

### VAR DICTIONARY: get dictionary of every random var and their possible values
# output: {'x2': array([0, 1]), 'x3': array([0, 1]), 'x1': array([1, 0])}
def getRandomVarDictionary(dataframe):
    varValuesDict = {}
    varNames = getRandomVarNames(dataframe)
    for name in varNames:
        varValuesDict[name] =  getUniqueRandomVarValues(dataframe, name)
    return varValuesDict

# JOINT QUERY RESULT
# execute queries in the array one by one to arrive at a filtered dataframe
def getJointQueryResult(dataframe, queryArray):
    # print "getJointQueryResult query: " + str(queryArray) + " " + str(len(queryArray))
    filteredDF = dataframe
    fieldNames = []
    if len(queryArray)>1: # random var has parents
        for querySingle in queryArray:
            for queryTuple in querySingle:
                updatedTuple = [queryTuple[0], queryTuple[1]]
                filteredDF = queryDataframe(filteredDF, updatedTuple)
                fieldName = queryTuple[0]
                fieldNames = getUniqueFieldNames(fieldName, fieldNames, dataframe)
        if len(filteredDF)>0:
            finalDF = filteredDF[fieldNames]    # filter columns only if rows remain
        else:
            finalDF = filteredDF
    else:
        queryTuple = oquery.getFlatendList(queryArray)
        finalDF = queryDataframe(dataframe, queryTuple)
    return finalDF

# UNIQUE FIELDS: gather a unique set of columns, even if the dataframe is queried multiple times for the same
# query case: [[('x1', 1), ('x2', 0), ('xm', 'mx')], [('x1', 1), ('x2', 0), ('xm', 'my')], [('x1', 1), ('x2', 0), ('xm', 'mz')], [('x1', 1), ('x2', 1), ('xm', 'mx')], [('x1', 1), ('x2', 1), ('xm', 'my')], [('x1', 1), ('x2', 1), ('xm', 'mz')]]
def getUniqueFieldNames(fieldName, fieldNames, dataframe):
    if not fieldName in fieldNames:     # have only unique names in the list
        fieldNames.append(fieldName)
    return fieldNames

# REMOVE UNNECESSARY COLUMNS: remove from field names columns no longer present
# def

# FILTER: reduce the dataframe to the rows that match a query, with only the columns that match the query
# queryArray = [('age', 1), ('sex', 2)]
def queryDataframe(dataframe, tuple):
    # print "FINAL QUERY TUPLE " + str(tuple)
    filteredDF = dataframe
    field_name = tuple[0]
    field_value = tuple[1]
    if field_name in getRandomVarNames(dataframe):
        filteredDF = filteredDF.loc[(filteredDF[field_name] == field_value)]
        return filteredDF
    else:   # skip filtering vars that are not present in the dataframe
        return dataframe

