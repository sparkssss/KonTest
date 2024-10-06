import ast

configText = 'CONFIG.txt'

fConfig = open(configText, "r")

while True:
    
    line = fConfig.readline()
    
    if not line:
        break
    
    words = line[:-1]
        
    if words.startswith('chosenDomain'):
        
        intWordInd = words.find('\'')
        
        intWords = words[intWordInd:]
        
        resWords = intWords.split(',')
        
        newResWords = []
        
        for resWord in resWords:
            
            start = resWord.find('\'') + 1
            resWord = resWord[start:]
            end = resWord.find('\'')
            resWord = resWord[:end]
            
            newResWords.append(resWord)
            
        resWords = newResWords
        
        chosenDomain = resWords[0]

    if words.startswith('selNodes'):
        
        intWordInd = words.find('[')
        
        intWords = words[intWordInd:]
        
        resWords = ast.literal_eval(intWords)
        
        foundPaths = resWords
        
fConfig.close()


########################################################################
#Code below stores the results of the atomic query in a list
########################################################################

case1Res = []
case2Res = []

if (chosenLLM=="Falcon"):

    fileNameConv1 = 'QueryType1.txt'
    fileNameConv2 = 'QueryType2.txt'
    fileNameConv12 = 'QueryType12.txt'
    fileNameConv21 = 'QueryType21.txt'
elif (chosenLLM=="Llama2"):

    fileNameConv1 = 'llama2Type1.txt'
    fileNameConv2 = 'llama2Type2.txt'
    fileNameConv12 = 'llama2Type12.txt'
    fileNameConv21 = 'llama2Type21.txt'
elif (chosenLLM=="GPT3.5"):

    fileNameConv1 = 'GPT35Type1.txt'
    fileNameConv2 = 'GPT35Type2.txt'
    fileNameConv12 = 'GPT35Type12.txt'
    fileNameConv21 = 'GPT35Type21.txt'
elif (chosenLLM=="Gemini"):

    fileNameConv1 = 'GeminiType1.txt'
    fileNameConv2 = 'GeminiType2.txt'
    fileNameConv12 = 'GeminiType12.txt'
    fileNameConv21 = 'GeminiType21.txt'

with open(fileNameConv1, encoding='utf8') as f1:
    
    count = 0
    for line in f1:
        
        if (count==0):
            
            count = 1
        else:
            
            count = 0
            
            case1Lower = line.lower()
            
            if case1Lower.startswith('yes'):
                
                case1 = 1
            elif case1Lower.startswith('no'):
                
                case1 = 0
            else:
                
                case1 = -1
            
            case1Res.append(case1)
     
with open(fileNameConv2, encoding='utf8') as f2:
    
    count = 0
    for line in f2:
        
        if (count==0):
            
            count = 1
        else:
            
            count = 0
            
            case2Lower = line.lower()
            
            if case2Lower.startswith('yes'):
                
                case2 = 1
            elif case2Lower.startswith('no'):
                
                case2 = 0
            else:
                
                case2 = -1
            
            case2Res.append(case2)


#print(len(case1Res))
#print(len(case2Res))

########################################################################
#Code below stores the results of the sequential queries in a list
########################################################################


case12Res = []
case21Res = []

import time

with open(fileNameConv12, encoding='utf8') as f1:


    count = 0
    for line in f1:
        
        if (count==0):
            
            count = 1
        else:
            
            count = 0
            
            case12Lower = line.lower()
            
            if case12Lower.startswith('yes'):
                
                case12 = 1
            elif case12Lower.startswith('no'):
                
                case12 = 0
            else:
                
                case12 = -1
            
            case12Res.append(case12)
            
with open(fileNameConv21, encoding='utf8') as f2:

    count = 0
    for line in f2:
        
        if (count==0):
            
            count = 1
        else:
            
            count = 0
            
            case21Lower = line.lower()
            
            if case21Lower.startswith('yes'):
                
                case21 = 1
            elif case21Lower.startswith('no'):
                
                case21 = 0
            else:
                
                case21 = -1
            
            case21Res.append(case21)


#print(len(case12Res))
#print(len(case21Res))

##########################################################################################################
#Code below finds the atomic errors in the LLM Responses
##########################################################################################################


errorCount = 0
regCount = 0

case1ErrArr = []

for count, item1 in enumerate(case1Res):
    
    item2 = case2Res[count]
    
    case1Err = -1
    
    if (item1!=-1):
        
        if (item2!=-1):
            
            case1Err = 0
            
            regCount = regCount + 1
        
            if (item1!=item2):

                errorCount = errorCount+1
                case1Err = 1
                
    case1ErrArr.append(case1Err)


#No. of Valid Queries and no. of atomic Errors.

print("Number of Valid Queries (atomic):")
print(regCount) #Number of valid tests
print("Number of Errors (atomic):")
print(errorCount) #Number of Errors
#print(case1ErrArr)

##########################################################################################################
#Code below finds the sequential-inter errors in the LLM Responses
##########################################################################################################

errorCount = 0
regCount = 0

case21ErrArr = []

for count, item1 in enumerate(case1Res):
    
    item2 = case21Res[count*2+1]
    
    case21Err = -1
    
    if (item1!=-1):
        
        if (item2!=-1):
            
            case21Err = 0
            
            regCount = regCount + 1
        
            if (item1!=item2):

                errorCount = errorCount+1
                
                case21Err = 1
                
    case21ErrArr.append(case21Err)

#Valid Test Count and Error Count when comparing Template 1 Sentences with Template 2 followed by Template 1 in Sequence

'''
print(regCount) #No. of Valid Tests
print(errorCount) #No. of Errors
#print(case21ErrArr)
'''

storeRegCount = regCount
storeErrorCount = errorCount

errorCount = 0
regCount = 0

case12ErrArr = []

for count, item1 in enumerate(case2Res):
    
    item2 = case12Res[count*2+1]
    
    case12Err = -1
    
    if (item1!=-1):
        
        if (item2!=-1):
            
            case12Err = 0
            
            regCount = regCount + 1
        
            if (item1!=item2):

                errorCount = errorCount+1
                
                case12Err = 1
                
    case12ErrArr.append(case12Err)

#Valid Test Count and Error Count when comparing Template 2 Sentences with Template 1 followed by Template 2 in Sequence

'''
print(regCount) #No. of Valid Tests
print(errorCount) #No. of Errors
#print(case12ErrArr)
'''

storeRegCount = storeRegCount + regCount
storeErrorCount = storeErrorCount + errorCount

print("Number of Valid Queries (sequential-inter):")
print(storeRegCount) #Number of valid tests
print("Number of Errors (sequential-inter):")
print(storeErrorCount) #Number of Errors

##########################################################################################################
#Code below finds the sequential-intra errors in the LLM Responses
##########################################################################################################

errorCount = 0
regCount = 0

flip = True

case12ErrArr = []

for count, item1 in enumerate(case12Res):
    
    if (flip!=False):
        
        item2 = case12Res[count+1]
        
        case12Err = -1
        
        if (item1!=-1 and item2!=-1):
            
            case12Err = 0

            regCount = regCount + 1

            if (item1!=item2):

                errorCount = errorCount+1
                
                case12Err = 1
                
        case12ErrArr.append(case12Err)
                
    flip = not flip
            
#Valid Test Count and Error Count when comparing within Template 1 Sentences followed by Template 2 in Sequence

'''
print(regCount) #No. of Valid Tests
print(errorCount) #No. of Errors
#print(case12ErrArr)
'''

storeRegCount = regCount
storeErrorCount = errorCount

errorCount = 0
regCount = 0

flip = True

case21ErrArr = []

for count, item1 in enumerate(case21Res):
    
    if (flip!=False):
        
        item2 = case21Res[count+1]
        
        case21Err = -1
        
        if (item1!=-1 and item2!=-1):
            
            case21Err = 0

            regCount = regCount + 1

            if (item1!=item2):

                errorCount = errorCount+1
                
                case21Err = 1
                
        case21ErrArr.append(case21Err)
                
    flip = not flip
    
#Valid Test Count and Error Count when comparing within Template 2 Sentences followed by Template 1 in Sequence

'''
print(regCount) #No. of Valid Tests
print(errorCount) #No. of Errors
#print(case21ErrArr)
'''

storeRegCount = storeRegCount + regCount
storeErrorCount = storeErrorCount + errorCount

print("Number of Valid Queries (sequential-intra):")
print(storeRegCount) #Number of valid tests
print("Number of Errors (sequential-intra):")
print(storeErrorCount) #Number of Errors


##########################################################################################################
#Code below finds the ontological errors in the LLM Responses
##########################################################################################################


from math import comb
import networkx as nx
import itertools


depth = 4
orderList = range(1, depth+1)
combinations = list(itertools.combinations(orderList, 2))

graphList = []
graphListInDet = []

count = -1
printer = 0

totCoverCount = 0
coverCount = 0

overlapArr1 = []

for elemPath in foundPaths[:50]:
    
    G = nx.DiGraph()
    GInDet = nx.DiGraph()
    
    lenComb = len(elemPath)
    
    orderList = range(1, lenComb+1)
    combinations = list(itertools.combinations(orderList, 2))
    
    for combo in combinations:
        
        overLap = False
        
        totCoverCount = totCoverCount + 1
        
        count = count + 1
        
        comb1 = combo[0]
        comb2 = combo[1]
        
        if (G.has_node(comb1)==False):
            
            G.add_node(comb1)
            GInDet.add_node(comb1)
            
        if (G.has_node(comb2)==False):
            
            G.add_node(comb2)
            GInDet.add_node(comb2)
        
        relation = case1Res[count]
        
        if (relation==1):
            
            G.add_edge(comb1, comb2)
            coverCount = coverCount + 1
            
            overLap = True
            
        if (relation==-1):
            
            GInDet.add_edge(comb1, comb2)
            
        overlapArr1.append(overLap)
        
    graphList.append(G)
    graphListInDet.append(GInDet)


#Coverage Count for Template 1
'''
print(totCoverCount)
print(coverCount)
'''

import copy

from networkx import has_path

totCount = 0
ontoError = 0

invalidCount = 0

count = -1
loop = -1

perPathErrorCount = 0
prevOntoError = 0

onto1ErrArr = []

for graphCount, g in enumerate(graphList):
    
    onto1Err = False
    
    loop = loop + 1
    
    elemPath = foundPaths[loop]
    
    lenComb = len(elemPath)
    
    orderList = range(1, lenComb+1)
    combinations = list(itertools.combinations(orderList, 2))
    
    allCheck = False

    for combo in combinations:
        
        errCheck = False
        
        count = count + 1
        
        comb1 = combo[0]
        comb2 = combo[1]
        
        if (comb2!=comb1+1):
            
            totCount = totCount + 1
            
            gCopy = copy.deepcopy(g)
            
            dirPath = case1Res[count]
            
            if gCopy.has_edge(comb1, comb2):
                
                gCopy.remove_edge(comb1, comb2)
            
            pathExist = has_path(gCopy, comb1, comb2)

            if (pathExist):
                
                if (dirPath==0):
                    
                    ontoError = ontoError + 1
                    
                    allCheck = True
                    
                    #print(count)
                    #print(elemPath)
                    errCheck = True
            
            if (errCheck==False):
                if (dirPath==-1):

                    invalidCount = invalidCount + 1
                else:
                    
                    gInDet = graphListInDet[graphCount]
                    gInDetCopy = copy.deepcopy(gInDet)
                    
                    pathExistInDet = has_path(gInDetCopy, comb1, comb2)
                    
                    if (pathExistInDet):
                        
                        invalidCount = invalidCount + 1
                        
    if (ontoError>prevOntoError):
        
        perPathErrorCount = perPathErrorCount + 1
        prevOntoError = ontoError
        
    onto1ErrArr.append(allCheck)


#Invalid Test Count and Onto Error Count for Template 1
'''
print(totCount) #Total number of tests
print(ontoError) #No. of Ontological Errors
print(invalidCount) #No. of Invalid Tests
print(perPathErrorCount) #Per-Path Error Count
print(onto1ErrArr)
'''

storeRegCount = totCount - invalidCount
storeErrorCount = ontoError


from math import comb
import networkx as nx
import itertools

graphList = []
graphListInDet = []

count = -1
printer = 0

totCoverCount = 0
coverCount = 0

overlapArr2 = []

for elemPath in foundPaths[:50]:
    
    G = nx.DiGraph()
    GInDet = nx.DiGraph()
    
    lenComb = len(elemPath)
    
    orderList = range(1, lenComb+1)
    combinations = list(itertools.combinations(orderList, 2))
    
    for combo in combinations:
        
        overLap = False
        
        totCoverCount = totCoverCount + 1
        
        count = count + 1
        
        comb1 = combo[0]
        comb2 = combo[1]
        
        if (G.has_node(comb1)==False):
            
            G.add_node(comb1)
            GInDet.add_node(comb1)
            
        if (G.has_node(comb2)==False):
            
            G.add_node(comb2)
            GInDet.add_node(comb2)
        
        relation = case2Res[count]
        
        if (relation==1):
            
            G.add_edge(comb1, comb2)
            coverCount = coverCount + 1
            
            overLap = True
            
        if (relation==-1):
            
            GInDet.add_edge(comb1, comb2)
            
        overlapArr2.append(overLap)
            
    graphList.append(G)
    graphListInDet.append(GInDet)

#Coverage Count for Template 2
'''
print(totCoverCount)
print(coverCount)
'''

import copy


from networkx import has_path

totCount = 0
ontoError = 0

invalidCount = 0

count = -1
loop = -1

perPathErrorCount = 0
prevOntoError = 0

onto2ErrArr = []

for graphCount, g in enumerate(graphList):
    
    loop = loop + 1
    
    elemPath = foundPaths[loop]
    
    lenComb = len(elemPath)
    
    orderList = range(1, lenComb+1)
    combinations = list(itertools.combinations(orderList, 2))
    
    allCheck = False

    for combo in combinations:
        
        count = count + 1
        
        comb1 = combo[0]
        comb2 = combo[1]
        
        if (comb2!=comb1+1):
            
            errCheck = False
            
            totCount = totCount + 1
            
            gCopy = copy.deepcopy(g)
            
            dirPath = case2Res[count]
            
            if gCopy.has_edge(comb1, comb2):
                
                gCopy.remove_edge(comb1, comb2)
            
            pathExist = has_path(gCopy, comb1, comb2)

            if (pathExist):
                
                if (dirPath==0):
                    
                    allCheck = True
                    
                    ontoError = ontoError + 1
                    
                    #print(elemPath)
                    errCheck = True
            
            if (errCheck==False):
                if (dirPath==-1):

                    invalidCount = invalidCount + 1
                else:
                    
                    gInDet = graphListInDet[graphCount]
                    gInDetCopy = copy.deepcopy(gInDet)
                    
                    pathExistInDet = has_path(gInDetCopy, comb1, comb2)
                    
                    if (pathExistInDet):
                        
                        invalidCount = invalidCount + 1
                        
    if (ontoError>prevOntoError):
        
        perPathErrorCount = perPathErrorCount + 1
        prevOntoError = ontoError
        
    onto2ErrArr.append(allCheck)

#Invalid Test Count and Onto Error Count for Template 2
'''
print(totCount) #Total number of tests
print(ontoError) #No. of Ontological Errors
print(invalidCount) #No. of Invalid Tests
print(perPathErrorCount) #Per-Path Error Count
print(onto2ErrArr)
'''

storeRegCount = storeRegCount + totCount - invalidCount
storeErrorCount = storeErrorCount + ontoError

print("Number of Valid Queries (Onto):")
print(storeRegCount) #Number of valid tests
print("Number of Errors (Onto):")
print(storeErrorCount) #Number of Errors
