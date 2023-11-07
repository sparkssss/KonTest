import pickle
import random
    
from bigtree import Node, tree_to_dot, print_tree, tree_to_nested_dict, nested_dict_to_tree, levelordergroup_iter

#Initial Code Block for extracting the nodes from the generated trees. Running it will generate a random set of nodes. Set used is in the code as foundPaths. 

#Generates the tests for a given LLM. Choose from "Falcon", "Llama2", "GPT3.5", "PALM2".

chosenLLM = "Falcon"

initList = ['Q32', 'Q27', 'Q20', 'Q39', 'Q334', 'Q846', 'Q30', 'Q189', 'Q35', 'Q408']

selNodes = []

megaRoot = Node("WorldRoot")

for countryNode in initList:

    with open(countryNode + '.pkl', 'rb') as file:

            # Call load method to deserialze
            myvar = pickle.load(file)

            root = nested_dict_to_tree(myvar)

            root.parent = megaRoot

for x in range(100):
    
    selGraph = random.choice(initList)
    
    with open('/knowledgeGraphs/' + selGraph + '.pkl', 'rb') as file:
      
        # Call load method to deserialze
        myvar = pickle.load(file)

        root = nested_dict_to_tree(myvar)
    
    nodeList = [[node.name for node in node_group] for node_group in levelordergroup_iter(root)]
    
    lastLevelNodeList = nodeList[-1]
    
    lastLevelNodeList = list(set(lastLevelNodeList))
        
    selNode = random.choice(lastLevelNodeList)
    
    selNodes.append(selNode)
        
print(len(selNodes))

print(selNodes)

selNodes = list(set(selNodes))

print(len(selNodes))


# In[ ]:


parent = root.parent

print(parent)


# In[ ]:


from bigtree import find_names

foundNodes = []

for elemNode in selNodes:
        
    #print(elemNode)

    findRes = find_names(megaRoot, elemNode)

    #print(findRes)

    parentNode = findRes[0]

    nodePath = []

    while (parentNode!=None):

        nodePath.append(parentNode.name)
        parentNode = parentNode.parent
        
    nodePath = nodePath[:-1]
    foundNodes.append(nodePath)
    
print(foundNodes)


foundPaths = [['Garnich', 'Garnich', 'Canton of Capellen', 'Luxembourg'], ['Lusail', 'Doha', 'Ad Dawhah', 'Qatar'], ['Ballintra (Ballyshannon)', 'County Donegal', 'Ulster', 'Ireland'], ['Munkebo Parish', 'Kerteminde Municipality', 'Southern Denmark', 'Denmark'], ['Rago National Park', 'Sørfold', 'Nordland', 'Norway'], ['Haw Par Villa', 'Queenstown, Singapore', 'Central Region', 'Singapore'], ['Yarrari', 'Gunnedah Shire', 'New South Wales', 'Australia'], ['Dalvík', 'Dalvíkurbyggð', 'Northeastern Region', 'Iceland'], ['Northumberland', 'Saratoga County', 'New York', 'United States of America'], ['Vacy', 'New South Wales', 'Australia'], ['Voldby Parish', 'Norddjurs Municipality', 'Central Denmark Region', 'Denmark'], ['Castlebar', 'County Mayo', 'Connacht', 'Ireland'], ['Kværndrup Parish', 'Faaborg-Midtfyn Municipality', 'Southern Denmark', 'Denmark'], ['Bluff', 'Hay Shire', 'New South Wales', 'Australia'], ['Byrkije', 'Grane', 'Nordland', 'Norway'], ['Haslen', 'Schlatt-Haslen', 'Appenzell Innerrhoden', 'Switzerland'], ['Gombak', 'Bukit Batok', 'West Region', 'Singapore'], ['Guelehtstjahkenvaellie', 'Røyrvik', 'Trøndelag', 'Norway'], ['Bourke', 'Bourke Shire', 'New South Wales', 'Australia'], ['Rochester Township', 'Kingman County', 'Kansas', 'United States of America'], ['Bellavary', 'County Mayo', 'Connacht', 'Ireland'], ['Churchill', 'Allegheny County', 'Pennsylvania', 'United States of America'], ['Storekvina', 'Kvinesdal', 'Agder', 'Norway'], ['Brunvær', 'Steigen Municipality', 'Nordland', 'Norway'], ['Klejtrup', 'Viborg Municipality', 'Central Denmark Region', 'Denmark'], ['Dundalk Upper', 'County Louth', 'Leinster', 'Ireland'], ['Dalaåsen', 'Sandefjord Municality', 'Vestfold og Telemark', 'Norway'], ['Rossinver', 'County Sligo', 'Connacht', 'Ireland'], ['Hüslers (AI-1755)', 'Schlatt-Haslen', 'Appenzell Innerrhoden', 'Switzerland'], ['Limestone County School District', 'Limestone County', 'Alabama', 'United States of America'], ['Kelsey Township', 'St. Louis County', 'Minnesota', 'United States of America'], ['Stenstad', 'Nome', 'Vestfold og Telemark', 'Norway'], ['Laugardalur', 'Reykjavík', 'Capital Region', 'Iceland'], ['Richmond', 'Jefferson County', 'Ohio', 'United States of America'], ['Faaborg', 'Faaborg-Midtfyn Municipality', 'Southern Denmark', 'Denmark'], ['Rodenbourg', 'Junglinster', 'Canton of Grevenmacher', 'Luxembourg'], ['Schwiedelbrouch', 'Rambrouch', 'Canton of Redange', 'Luxembourg'], ['Bolungarvík', 'Bolungarvíkurkaupstaður', 'Westfjords', 'Iceland'], ['Háaleiti og Bústaðir', 'Reykjavík', 'Capital Region', 'Iceland'], ['Vienna, Hunters Hill', 'New South Wales', 'Australia'], ['Flåbekkåsen', 'Namsos Municipality', 'Trøndelag', 'Norway'], ['Vester Åby', 'Faaborg-Midtfyn Municipality', 'Southern Denmark', 'Denmark'], ['Kinawley', 'County Cavan', 'Ulster', 'Ireland'], ['Kloster St. Ottilia', 'Oberegg', 'Appenzell Innerrhoden', 'Switzerland'], ['Hou Parish', 'Aalborg Municipality', 'North Denmark Region', 'Denmark'], ['Itzig', 'Hesperange', 'Canton of Luxembourg', 'Luxembourg'], ['Skalmen', 'Smøla', 'Møre og Romsdal', 'Norway'], ['Tingaringy', 'Croajingolong', 'Victoria', 'Australia'], ['Boufferdanger Muer', 'Sandweiler', 'Canton of Luxembourg', 'Luxembourg'], ['Fister', 'Hjelmeland', 'Rogaland', 'Norway'], ['Hattmoenget', 'Høylandet Municipality', 'Trøndelag', 'Norway'], ['Sandsvågen', 'Sande', 'Møre og Romsdal', 'Norway'], ['Doontrusk', 'County Mayo', 'Connacht', 'Ireland'], ['Haller', 'Waldbillig', 'Canton of Echternach', 'Luxembourg'], ['Hacketstown', 'Holmpatrick', 'Fingal', 'Ireland'], ['Agat Invasion Beach', 'Hågat', 'Guam', 'United States of America'], ['Hoscheid', 'Parc Hosingen', 'Canton of Clervaux', 'Luxembourg'], ['Dolphin Point', 'New South Wales', 'Australia'], ['Kyle', 'Gloucester', 'New South Wales', 'Australia'], ['Hagen', 'Steinfort', 'Canton of Capellen', 'Luxembourg'], ['Kilbride', 'Middle Third', 'Munster', 'Ireland'], ['Laugarvatn', 'Bláskógabyggð', 'Southern Region', 'Iceland'], ['Seven Mile Beach National Park', 'Municipality of Kiama', 'New South Wales', 'Australia'], ['Lempster', 'Sullivan County', 'New Hampshire', 'United States of America'], ['Old Midland Junction School', 'City of Swan', 'Western Australia', 'Australia'], ['Anholt Parish', 'Norddjurs Municipality', 'Central Denmark Region', 'Denmark'], ['Bukit Batok South', 'Bukit Batok', 'West Region', 'Singapore'], ['Vindfarholmen', 'Volda', 'Møre og Romsdal', 'Norway'], ['Miðborg', 'Reykjavík', 'Capital Region', 'Iceland'], ['Rosport', 'Rosport-Mompach', 'Canton of Echternach', 'Luxembourg'], ['Fernvale, Singapore', 'Sengkang', 'North-East Region', 'Singapore'], ['Snow City', 'Jurong East', 'West Region', 'Singapore'], ['Ammans Crossing', 'Kendall County', 'Texas', 'United States of America'], ['Siglufjörður', 'Fjallabyggð', 'Northeastern Region', 'Iceland'], ['Vejgaard Parish', 'Aalborg Municipality', 'North Denmark Region', 'Denmark'], ['Sinding', 'Silkeborg Municipality', 'Central Denmark Region', 'Denmark'], ['Appenzell Meistersrüte', 'Appenzell', 'Appenzell Innerrhoden', 'Switzerland'], ['Royal Exchange Hotel', 'Western Australia', 'Australia'], ['Kølstrup Parish', 'Kerteminde Municipality', 'Southern Denmark', 'Denmark'], ['Westlake', 'Ohio', 'United States of America'], ['Morse Township', 'St. Louis County', 'Minnesota', 'United States of America'], ['Skreen', 'County Sligo', 'Connacht', 'Ireland'], ['Lawson', 'New South Wales', 'Australia'], ['Untereisenbach', 'Parc Hosingen', 'Canton of Clervaux', 'Luxembourg'], ['Schlatt', 'Schlatt-Haslen', 'Appenzell Innerrhoden', 'Switzerland'], ['Ehner', 'Saeul', 'Canton of Redange', 'Luxembourg'], ['Sheridan Township', 'Mecosta County', 'Michigan', 'United States of America'], ['Crosskeys', 'County Cavan', 'Ulster', 'Ireland'], ['Grudevatn', 'Klepp', 'Rogaland', 'Norway'], ['Lower Philipstown', 'County Offaly', 'Leinster', 'Ireland'], ['Bettange-sur-Mess', 'Dippach', 'Canton of Capellen', 'Luxembourg'], ['capuchin convent of Mary of the Angels', 'Appenzell', 'Appenzell Innerrhoden', 'Switzerland']]
# In[ ]:

import pprint
import google.generativeai as palm

#models = [m for m in palm.list_models()]
#model = models[0].name
#print(model)


# In[ ]:


import itertools
import llm
import time

import pprint
import google.generativeai as palm

#model = "models/chat-bison-001"

if (chosenLLM=="Falcon"):

    model = llm.get_model("ggml-model-gpt4all-falcon-q4_0")
elif (chosenLLM=="Llama2"):

    model = llm.get_model("llama-2-7b-chat")
elif (chosenLLM=="GPT3.5"):

    model = llm.get_model("gpt-3.5-turbo")
    model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

'''
#model = llm.get_model("ggml-model-gpt4all-falcon-q4_0")
model = llm.get_model("chat-bison-001")
model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
'''

'''
model = llm.get_model("gpt-3.5-turbo")
model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
'''
#conversation = model.conversation()

#model = llm.get_model("llama-2-7b-chat")

preAmble = "Be concise as possible. Answer with a yes or no response. "

list1 = []
list2 = []

for elemPath in foundPaths[:50]:
    
    combinations = list(itertools.combinations(elemPath, 2))

    for combo in combinations:
        
        parentNode = combo[1]
        childNode = combo[0]
        
        q1 = "Is there a " + childNode + " in " + parentNode + "?"
        q2 = "Does " + parentNode + " have a " + childNode + "?"
        
        
        if (chosenLLM=="Llama2" or chosenLLM=="Falcon"):
        
            response1 = model.prompt(preAmble + q1)
            response2 = model.prompt(preAmble + q2)
        elif (chosenLLM=="GPT3.5"):
        
            loopDone = False
            backoff = 0
            
            while(loopDone!=True):
                
                try:
                    
                    time.sleep(backoff)
                    
                    response1 = model.prompt(
                        q1,
                        system=preAmble,
                        temperature=0
                    )
                    
                    textResp1 = response1.text()
                    loopDone = True
                except:
                    
                    if (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2
           
        
            loopDone = False
            backoff = 0
            
            while(loopDone!=True):
                
                try:
                    
                    time.sleep(backoff)
                    
                    response2 = model.prompt(
                        q2,
                        system=preAmble,
                        temperature=0
                    )
                    
                    textResp2 = response2.text()
                    loopDone = True
                except:
                    
                    if (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2
                        
        elif (chosenLLM=="PALM2"):
        
            response1 = palm.chat(context=preAmble,
                              messages=q1,
                              temperature=0)
            
            response2 = palm.chat(context=preAmble,
                              messages=q2,
                              temperature=0)
        
        
        if (chosenLLM!="PALM2"):
        
            textResp1 = response1.text()
            textResp2 = response2.text()
            
        else:
        
            textResp1 = response1.last
            textResp2 = response2.last
        
        if (textResp1!=None):
            
            textResp1 = textResp1.strip()
        
            if ("\n" in textResp1):

                indFind = textResp1.find("\n")

                if (indFind!=-1):

                    textResp1 = textResp1[:indFind]

            if "\r" in textResp1:

                indFind = textResp1.find("\r")

                if (indFind!=-1):

                    textResp1 = textResp1[:indFind]
        else:
            
            textResp1 = "NIL"
                    
        if (textResp2!=None):
            
            textResp2 = textResp2.strip()
                
            if ("\n" in textResp2):

                indFind = textResp2.find("\n")

                if (indFind!=-1):

                    textResp2 = textResp2[:indFind]

            if "\r" in textResp2:

                indFind = textResp2.find("\r")

                if (indFind!=-1):

                    textResp2 = textResp2[:indFind]
                    
        else:
            
            textResp2 = "NIL"
        
        list1.append(q1 + "\n")
        list1.append(textResp1 + "\n")
        
        list2.append(q2 + "\n")
        list2.append(textResp2 + "\n")
        
if (chosenLLM=="Falcon"):

    file1 = open("QueryType1.txt", "w")
    file2 = open("QueryType2.txt", "w")
elif (chosenLLM=="Llama2"):

    file1 = open("llama2Type1.txt", "w")
    file2 = open("llama2Type2.txt", "w")
elif (chosenLLM=="GPT3.5"):

    file1 = open("GPT35Type1.txt", "w")
    file2 = open("GPT35Type2.txt", "w")
elif (chosenLLM=="PALM2"):

    file1 = open("PALMType1.txt", "w")
    file2 = open("PALMType2.txt", "w")
            
list1Res = ''.join(list1)
file1.write(list1Res)

list2Res = ''.join(list2)
file2.write(list2Res)
        
file1.close()
file2.close()


# In[ ]:


foundPaths = [['Garnich', 'Garnich', 'Canton of Capellen', 'Luxembourg'], ['Lusail', 'Doha', 'Ad Dawhah', 'Qatar'], ['Ballintra (Ballyshannon)', 'County Donegal', 'Ulster', 'Ireland'], ['Munkebo Parish', 'Kerteminde Municipality', 'Southern Denmark', 'Denmark'], ['Rago National Park', 'Sørfold', 'Nordland', 'Norway'], ['Haw Par Villa', 'Queenstown, Singapore', 'Central Region', 'Singapore'], ['Yarrari', 'Gunnedah Shire', 'New South Wales', 'Australia'], ['Dalvík', 'Dalvíkurbyggð', 'Northeastern Region', 'Iceland'], ['Northumberland', 'Saratoga County', 'New York', 'United States of America'], ['Vacy', 'New South Wales', 'Australia'], ['Voldby Parish', 'Norddjurs Municipality', 'Central Denmark Region', 'Denmark'], ['Castlebar', 'County Mayo', 'Connacht', 'Ireland'], ['Kværndrup Parish', 'Faaborg-Midtfyn Municipality', 'Southern Denmark', 'Denmark'], ['Bluff', 'Hay Shire', 'New South Wales', 'Australia'], ['Byrkije', 'Grane', 'Nordland', 'Norway'], ['Haslen', 'Schlatt-Haslen', 'Appenzell Innerrhoden', 'Switzerland'], ['Gombak', 'Bukit Batok', 'West Region', 'Singapore'], ['Guelehtstjahkenvaellie', 'Røyrvik', 'Trøndelag', 'Norway'], ['Bourke', 'Bourke Shire', 'New South Wales', 'Australia'], ['Rochester Township', 'Kingman County', 'Kansas', 'United States of America'], ['Bellavary', 'County Mayo', 'Connacht', 'Ireland'], ['Churchill', 'Allegheny County', 'Pennsylvania', 'United States of America'], ['Storekvina', 'Kvinesdal', 'Agder', 'Norway'], ['Brunvær', 'Steigen Municipality', 'Nordland', 'Norway'], ['Klejtrup', 'Viborg Municipality', 'Central Denmark Region', 'Denmark'], ['Dundalk Upper', 'County Louth', 'Leinster', 'Ireland'], ['Dalaåsen', 'Sandefjord Municality', 'Vestfold og Telemark', 'Norway'], ['Rossinver', 'County Sligo', 'Connacht', 'Ireland'], ['Hüslers (AI-1755)', 'Schlatt-Haslen', 'Appenzell Innerrhoden', 'Switzerland'], ['Limestone County School District', 'Limestone County', 'Alabama', 'United States of America'], ['Kelsey Township', 'St. Louis County', 'Minnesota', 'United States of America'], ['Stenstad', 'Nome', 'Vestfold og Telemark', 'Norway'], ['Laugardalur', 'Reykjavík', 'Capital Region', 'Iceland'], ['Richmond', 'Jefferson County', 'Ohio', 'United States of America'], ['Faaborg', 'Faaborg-Midtfyn Municipality', 'Southern Denmark', 'Denmark'], ['Rodenbourg', 'Junglinster', 'Canton of Grevenmacher', 'Luxembourg'], ['Schwiedelbrouch', 'Rambrouch', 'Canton of Redange', 'Luxembourg'], ['Bolungarvík', 'Bolungarvíkurkaupstaður', 'Westfjords', 'Iceland'], ['Háaleiti og Bústaðir', 'Reykjavík', 'Capital Region', 'Iceland'], ['Vienna, Hunters Hill', 'New South Wales', 'Australia'], ['Flåbekkåsen', 'Namsos Municipality', 'Trøndelag', 'Norway'], ['Vester Åby', 'Faaborg-Midtfyn Municipality', 'Southern Denmark', 'Denmark'], ['Kinawley', 'County Cavan', 'Ulster', 'Ireland'], ['Kloster St. Ottilia', 'Oberegg', 'Appenzell Innerrhoden', 'Switzerland'], ['Hou Parish', 'Aalborg Municipality', 'North Denmark Region', 'Denmark'], ['Itzig', 'Hesperange', 'Canton of Luxembourg', 'Luxembourg'], ['Skalmen', 'Smøla', 'Møre og Romsdal', 'Norway'], ['Tingaringy', 'Croajingolong', 'Victoria', 'Australia'], ['Boufferdanger Muer', 'Sandweiler', 'Canton of Luxembourg', 'Luxembourg'], ['Fister', 'Hjelmeland', 'Rogaland', 'Norway'], ['Hattmoenget', 'Høylandet Municipality', 'Trøndelag', 'Norway'], ['Sandsvågen', 'Sande', 'Møre og Romsdal', 'Norway'], ['Doontrusk', 'County Mayo', 'Connacht', 'Ireland'], ['Haller', 'Waldbillig', 'Canton of Echternach', 'Luxembourg'], ['Hacketstown', 'Holmpatrick', 'Fingal', 'Ireland'], ['Agat Invasion Beach', 'Hågat', 'Guam', 'United States of America'], ['Hoscheid', 'Parc Hosingen', 'Canton of Clervaux', 'Luxembourg'], ['Dolphin Point', 'New South Wales', 'Australia'], ['Kyle', 'Gloucester', 'New South Wales', 'Australia'], ['Hagen', 'Steinfort', 'Canton of Capellen', 'Luxembourg'], ['Kilbride', 'Middle Third', 'Munster', 'Ireland'], ['Laugarvatn', 'Bláskógabyggð', 'Southern Region', 'Iceland'], ['Seven Mile Beach National Park', 'Municipality of Kiama', 'New South Wales', 'Australia'], ['Lempster', 'Sullivan County', 'New Hampshire', 'United States of America'], ['Old Midland Junction School', 'City of Swan', 'Western Australia', 'Australia'], ['Anholt Parish', 'Norddjurs Municipality', 'Central Denmark Region', 'Denmark'], ['Bukit Batok South', 'Bukit Batok', 'West Region', 'Singapore'], ['Vindfarholmen', 'Volda', 'Møre og Romsdal', 'Norway'], ['Miðborg', 'Reykjavík', 'Capital Region', 'Iceland'], ['Rosport', 'Rosport-Mompach', 'Canton of Echternach', 'Luxembourg'], ['Fernvale, Singapore', 'Sengkang', 'North-East Region', 'Singapore'], ['Snow City', 'Jurong East', 'West Region', 'Singapore'], ['Ammans Crossing', 'Kendall County', 'Texas', 'United States of America'], ['Siglufjörður', 'Fjallabyggð', 'Northeastern Region', 'Iceland'], ['Vejgaard Parish', 'Aalborg Municipality', 'North Denmark Region', 'Denmark'], ['Sinding', 'Silkeborg Municipality', 'Central Denmark Region', 'Denmark'], ['Appenzell Meistersrüte', 'Appenzell', 'Appenzell Innerrhoden', 'Switzerland'], ['Royal Exchange Hotel', 'Western Australia', 'Australia'], ['Kølstrup Parish', 'Kerteminde Municipality', 'Southern Denmark', 'Denmark'], ['Westlake', 'Ohio', 'United States of America'], ['Morse Township', 'St. Louis County', 'Minnesota', 'United States of America'], ['Skreen', 'County Sligo', 'Connacht', 'Ireland'], ['Lawson', 'New South Wales', 'Australia'], ['Untereisenbach', 'Parc Hosingen', 'Canton of Clervaux', 'Luxembourg'], ['Schlatt', 'Schlatt-Haslen', 'Appenzell Innerrhoden', 'Switzerland'], ['Ehner', 'Saeul', 'Canton of Redange', 'Luxembourg'], ['Sheridan Township', 'Mecosta County', 'Michigan', 'United States of America'], ['Crosskeys', 'County Cavan', 'Ulster', 'Ireland'], ['Grudevatn', 'Klepp', 'Rogaland', 'Norway'], ['Lower Philipstown', 'County Offaly', 'Leinster', 'Ireland'], ['Bettange-sur-Mess', 'Dippach', 'Canton of Capellen', 'Luxembourg'], ['capuchin convent of Mary of the Angels', 'Appenzell', 'Appenzell Innerrhoden', 'Switzerland']]


# In[ ]:


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
elif (chosenLLM=="PALM2"):

    fileNameConv1 = 'PALMType1.txt'
    fileNameConv2 = 'PALMType2.txt'
    fileNameConv12 = 'PALMType12.txt'
    fileNameConv21 = 'PALMType21.txt'

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



# In[ ]:


print(len(case1Res))
print(len(case2Res))


# In[ ]:


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


# In[ ]:

#No. of Valid Queries and no. of Type 1 Errors.

print(regCount) #Comp 1 with 2
print(errorCount)
print(case1ErrArr)


# In[ ]:


import itertools
import llm
import time

#model = llm.get_model("ggml-model-gpt4all-falcon-q4_0")

model = llm.get_model("llama-2-7b-chat")

'''
model = llm.get_model("gpt-3.5-turbo")
model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
'''

#conversation = model.conversation()

import pprint
import google.generativeai as palm

#model = "models/chat-bison-001"

if (chosenLLM=="Falcon"):

    model = llm.get_model("ggml-model-gpt4all-falcon-q4_0")
elif (chosenLLM=="Llama2"):

    model = llm.get_model("llama-2-7b-chat")
elif (chosenLLM=="GPT3.5"):

    model = llm.get_model("gpt-3.5-turbo")
    model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'


preAmble = "Be concise as possible. Answer with a yes or no response. "

list1 = []
list2 = []

for elemPath in foundPaths[:50]:
    
    combinations = list(itertools.combinations(elemPath, 2))
    
    for combo in combinations:
        
        parentNode = combo[1]
        childNode = combo[0]
        
        q1 = "Is there a " + childNode + " in " + parentNode + "?"
        q2 = "Does " + parentNode + " have a " + childNode + "?"
        
        
        if (chosenLLM=="Llama2" or chosenLLM=="Falcon"):
        
            conversation1 = model.conversation()
            
            response1 = conversation1.prompt(preAmble + q1)
            textResp1 = response1.text()
            
            response2 = conversation1.prompt(preAmble + q2)
            textResp2 = response2.text()
        elif (chosenLLM=="PALM2"):
        
            response1 = palm.chat(context=preAmble,
                                  messages=q1,
                                  temperature=0
                                 )
        elif (chosenLLM=="GPT3.5"):

            loopDone = False
            backoff = 0
            
            while(loopDone!=True):
                
                try:
                    
                    time.sleep(backoff)
                    
                    conversation1 = model.conversation()
                    
                    response1 = conversation1.prompt(
                        q1,
                        system=preAmble,
                        temperature=0
                    )
                    textResp1 = response1.text()
                    
                    response2 = conversation1.prompt(
                        q2,
                        system=preAmble,
                        temperature=0
                    )
                    textResp2 = response2.text()
                    
                    loopDone = True
                except:
                    
                    if (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2
                        
        if (chosenLLM=="PALM2"):
        
            if (response1.last!=None):
                response2 = response1.reply(q2)
                textResp1 = response1.last
                textResp2 = response2.last
            else:
                
                textResp1 = "NIL"
                textResp2 = "NIL"

        if (textResp1!=None):
            
            textResp1 = textResp1.strip()
            if ("\n" in textResp1):

                indFind = textResp1.find("\n")

                if (indFind!=-1):

                    textResp1 = textResp1[:indFind]

            if "\r" in textResp1:

                indFind = textResp1.find("\r")

                if (indFind!=-1):

                    textResp1 = textResp1[:indFind]
        else:
            
            textResp1 = "NIL"
        
        if (textResp2!=None):
            
            textResp2 = textResp2.strip()
            if ("\n" in textResp2):

                indFind = textResp2.find("\n")

                if (indFind!=-1):

                    textResp2 = textResp2[:indFind]

            if "\r" in textResp2:

                indFind = textResp2.find("\r")

                if (indFind!=-1):

                    textResp2 = textResp2[:indFind]
                    
        else:
            
            textResp2 = "NIL"
        
        list1.append(q1 + "\n")
        list1.append(textResp1 + "\n")
        list1.append(q2 + "\n")
        list1.append(textResp2 + "\n")
        
        
        if (chosenLLM=="Llama2" or chosenLLM=="Falcon"):
        
            conversation2 = model.conversation()
            
            response1 = conversation2.prompt(preAmble + q2)
            textResp1 = response1.text()
            
            response2 = conversation2.prompt(preAmble + q1)
            textResp2 = response2.text()
        elif (chosenLLM=="PALM2"):
        
            response1 = palm.chat(context=preAmble,
                              messages=q2,
                              temperature=0)
        elif (chosenLLM=="GPT3.5"):
        
            loopDone = False
            backoff = 0
            
            while(loopDone!=True):
                
                try:
                    
                    time.sleep(backoff)
                    
                    conversation2 = model.conversation()
                    
                    response1 = conversation2.prompt(
                        q2,
                        system=preAmble,
                        temperature=0
                    )
                    textResp1 = response1.text()
                    
                    response2 = conversation2.prompt(
                        q1,
                        system=preAmble,
                        temperature=0
                    )
                    textResp2 = response2.text()
                    
                    loopDone = True
                except:
                    
                    if (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2
        
        
        if (chosenLLM=="PALM2"):

            if (response1.last!=None):
                response2 = response1.reply(q1)
                textResp1 = response1.last
                textResp2 = response2.last
            else:
                
                textResp1 = "NIL"
                textResp2 = "NIL"
        
        if (textResp1!=None):
            
            textResp1 = textResp1.strip()
            if ("\n" in textResp1):

                indFind = textResp1.find("\n")

                if (indFind!=-1):

                    textResp1 = textResp1[:indFind]

            if "\r" in textResp1:

                indFind = textResp1.find("\r")

                if (indFind!=-1):

                    textResp1 = textResp1[:indFind]
        else:
            
            textResp1 = "NIL"
                
        if (textResp2!=None):
            
            textResp2 = textResp2.strip()
            if ("\n" in textResp2):

                indFind = textResp2.find("\n")

                if (indFind!=-1):

                    textResp2 = textResp2[:indFind]

            if "\r" in textResp2:

                indFind = textResp2.find("\r")

                if (indFind!=-1):

                    textResp2 = textResp2[:indFind]
        else:
            
            textResp2 = "NIL"
        
        list2.append(q2 + "\n")
        list2.append(textResp1 + "\n")
        list2.append(q1 + "\n")
        list2.append(textResp2 + "\n")
        
if (chosenLLM=="Falcon"):

    file1 = open("QueryType12.txt", "w")
    file2 = open("QueryType21.txt", "w")
elif (chosenLLM=="Llama2"):

    file1 = open("llama2Type12.txt", "w")
    file2 = open("llama2Type21.txt", "w")
elif (chosenLLM=="GPT3.5"):

    file1 = open("GPT35Type12.txt", "w")
    file2 = open("GPT35Type21.txt", "w")
elif (chosenLLM=="PALM2"):

    file1 = open("PALMType12.txt", "w")
    file2 = open("PALMType21.txt", "w")
            
list1Res = ''.join(list1)
file1.write(list1Res)

list2Res = ''.join(list2)
file2.write(list2Res)
        
file1.close()
file2.close()


# In[ ]:


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


# In[ ]:


print(len(case12Res))
print(len(case21Res))


# In[ ]:


errorCount = 0
regCount = 0

case1ErrArr = []

for count, item1 in enumerate(case1Res):
    
    item2 = case12Res[count*2]
    
    case1Err = -1
    
    if (item1!=-1):
        
        if (item2!=-1):
            
            case1Err = 0
            
            regCount = regCount + 1
        
            if (item1!=item2):

                errorCount = errorCount+1
                
                case1Err = 1
                
    case1ErrArr.append(case1Err)


# In[ ]:

#Valid Test Count and Error Count when comparing Template 1 Sentences with Template 1 followed by Template 2 in Sequence

print(regCount) #Comp 1 with 12
print(errorCount)
print(case1ErrArr)


# In[ ]:


errorCount = 0
regCount = 0

case2ErrArr = []

for count, item1 in enumerate(case2Res):
    
    case2Err = -1
    
    item2 = case21Res[count*2]
    
    if (item1!=-1):
        
        if (item2!=-1):
            
            case2Err = 0
            
            regCount = regCount + 1
        
            if (item1!=item2):
                
                case2Err = 1

                errorCount = errorCount+1
                
                print(item1)
                print(item2)
                
    case2ErrArr.append(case2Err)


# In[ ]:

#Valid Test Count and Error Count when comparing Template 2 Sentences with Template 2 followed by Template 1 in Sequence

print(regCount) #Comp 2 with 21
print(errorCount)
print(case2ErrArr)


# In[ ]:


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


# In[ ]:

#Valid Test Count and Error Count when comparing Template 1 Sentences with Template 2 followed by Template 1 in Sequence

print(regCount) #Comp 1 with 21
print(errorCount)
print(case21ErrArr)


# In[ ]:


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


# In[ ]:

#Valid Test Count and Error Count when comparing Template 2 Sentences with Template 1 followed by Template 2 in Sequence

print(regCount) #Comp 2 with 12
print(errorCount)
print(case12ErrArr)


# In[ ]:


errorCount = 0
regCount = 0

flip = True

case1221ErrArr = []

for count, item1 in enumerate(case12Res):
        
    item2 = case21Res[count]
        
    if (flip==True):
        
        fir1 = item1
        fir2 = item2
    else:
        
        sec1 = item1
        sec2 = item2
        
    if (flip==False):
        
        case1221Err = -1
    
        if (fir1!=-1 and fir2!=-1 and sec1!=-1 and sec2!=-1):
            
            case1221Err = 0
            regCount = regCount + 1

            if (fir1!=fir2) or (sec1!=sec2):

                errorCount = errorCount+1
                
                case1221Err = 1
        
        case1221ErrArr.append(case1221Err)
                
    flip = not flip
    


# In[ ]:

#Valid Test Count and Error Count when comparing Template 1 Sentences followed by Template 2 in Sequence with Template 2 followed by Template 1 in Sequence

print(regCount) #Comp 12 with 21
print(errorCount)
print(case1221ErrArr)


# In[ ]:


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
            
print(regCount) #Comp 12
print(errorCount)
print(case12ErrArr)


# In[ ]:


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
            
print(regCount) #Comp 21
print(errorCount)
print(case21ErrArr)


# In[ ]:


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


# In[ ]:

#Coverage Count for Template 1

print(totCoverCount) #Type 1 Onto
print(coverCount)


# In[ ]:


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


# In[ ]:

#Invalid Test Count and Onto Error Count for Template 1

print(totCount) #Type 1 Onto Atomic
print(ontoError)
print(invalidCount)
print(perPathErrorCount)
print(onto1ErrArr)


# In[ ]:


from math import comb
import networkx as nx
import itertools

'''
depth = 4
orderList = range(1, depth+1)
combinations = list(itertools.combinations(orderList, 2))
'''

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


# In[ ]:

#Coverage Count for Template 1

print(totCoverCount)
print(coverCount)


# In[ ]:


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


# In[ ]:

#Invalid Test Count and Onto Error Count for Template 1

print(totCount)
print(ontoError)
print(invalidCount)
print(perPathErrorCount)
print(onto2ErrArr)


# In[ ]:


print(len(overlapArr1))
print((overlapArr2))


# In[ ]:

#Overlap Computation

overlapCounter = 0
over1Counter = 0
over2Counter = 0
noneCounter = 0

for count, elem1 in enumerate(overlapArr1):
    
    elem2 = overlapArr2[count]
    
    if ((elem1==True) and (elem2==True)):
        
        overlapCounter = overlapCounter + 1
    elif (elem1==True):
        
        over1Counter = over1Counter + 1
    elif (elem2==True):
        
        over2Counter = over2Counter + 1
    else:
        
        noneCounter = noneCounter + 1


# In[ ]:


print(overlapCounter)
print(over1Counter)
print(over2Counter)
print(noneCounter)


# In[ ]:


gap1 = 0
gap2 = 0
gapIntersect = 0
noGap = 0

for count, elem1 in enumerate(overlapArr1):
    
    elem2 = overlapArr2[count]
    
    if ((elem1==False) and (elem2==False)):
        
        gapIntersect = gapIntersect + 1
    elif (elem1==False):
        
        gap1 = gap1 + 1
    elif (elem2==False):
        
        gap2 = gap2 + 1
    else:
        
        noGap = noGap + 1


# In[ ]:


print(gapIntersect)
print(gap1)
print(gap2)
print(noGap)


# In[ ]:




