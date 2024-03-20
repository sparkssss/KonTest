import pickle
import random
    
from bigtree import Node, tree_to_dot, print_tree, tree_to_nested_dict, nested_dict_to_tree, levelordergroup_iter

#Initial Code Block for extracting the nodes from the generated trees. Running it will generate a random set of nodes. Set used is in the code as foundPaths. 

#Generates the tests for a given LLM. Choose from "Falcon", "Llama2", "GPT3.5", "Gemini".

#Generates the tests for a given Domain. Choose from "Places", "Artists".

chosenDomain = "Places"

chosenLLM = "Falcon"

if chosenDomain=="Places":

    initList = ['Q32', 'Q27', 'Q20', 'Q39', 'Q334', 'Q846', 'Q30', 'Q189', 'Q35', 'Q408']
elif chosenDomain=="Artists":

    initList = ['Q26876','Q5608','Q33240','Q47447','Q160009','Q2121062','Q23215','Q45188','Q36844','Q261','Q36153','Q21621919','Q483802','Q11975','Q182223','Q2831','Q134541','Q467526','Q356487','Q10708','Q29564107','Q1450','Q559819','Q153694','Q15935','Q483507','Q34086','Q23884740','Q15862','Q391348','Q29561472','Q121507','Q3626966','Q165911','Q1299','Q1744','Q19848','Q52151598','Q753598','Q130798','Q153056','Q43432','Q151892','Q30449','Q4235','Q549981','Q42493','Q41076','Q47875','Q6060','Q218992','Q5105','Q47871','Q106648','Q41594','Q396','Q315547','Q155700','Q40715','Q2808','Q380927','Q215546','Q366584','Q62766','Q259254','Q21914464','Q175097','Q483718','Q34424','Q273055','Q44333953','Q220730','Q13605596','Q308816','Q94831','Q18233','Q80424','Q215215','Q195439','Q63243883','Q142636','Q15897','Q228909','Q158175','Q47122','Q202550','Q39639','Q297097','Q15123969','Q131433','Q218083','Q11895','Q472595','Q28561969','Q166197','Q204018','Q5108148','Q182655','Q16210722','Q303','Q464241','Q37150','Q1777698','Q50527563','Q15615','Q42402','Q170599','Q130799','Q409','Q6405079','Q485811','Q51120673','Q240767','Q1225','Q23771950','Q17140','Q200577','Q3445057','Q7857806','Q139154','Q146027','Q482444','Q193676','Q15920','Q482477','Q162202','Q34389','Q154454','Q17198340','Q27593','Q11036','Q873384','Q382890','Q81698554','Q11998','Q236549','Q189991','Q483379','Q282531','Q42315001','Q32849','Q28816483','Q22151','Q36490532','Q6107','Q78754352','Q1438730','Q180224','Q38257','Q131366','Q13580495','Q266496','Q277551','Q192486','Q161877','Q929683','Q155079','Q3644642','Q214227','Q34584','Q953918','Q102385','Q45165','Q389870','Q14045','Q181484','Q1869293','Q256732','Q617932','Q11617','Q188407','Q189635','Q43259','Q80304','Q11649','Q832086','Q1200415','Q193710','Q200586','Q25177','Q1661036','Q168992','Q154222','Q44857','Q5383','Q845790','Q483203','Q254371','Q309843','Q464749','Q2306','Q42775','Q231233','Q134233','Q151241','Q2331','Q18534249','Q310763','Q269813','Q223769']


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

foundPaths = [[("It's Enough!", 'Song'), ('Raise Vibration', 'Album'), ('Lenny Kravitz', 'Artist')], [('I Love You', 'Song'), ('When We All Fall Asleep, Where Do We Go?', 'Album'), ('Billie Eilish', 'Artist')], [('Whiskey Glasses', 'Song'), ('If I Know Me', 'Album'), ('Morgan Wallen', 'Artist')], [("Don't Sit Down 'Cause I've Moved Your Chair", 'Song'), ('Suck It and See', 'Album'), ('Arctic Monkeys', 'Artist')], [('BTS, the Best', 'Album'), ('BTS', 'Artist')], [('Every River', 'Song'), ('Steers & Stripes', 'Album'), ('Brooks & Dunn', 'Artist')], [('Wheel in the Sky', 'Song'), ('Infinity', 'Album'), ('Journey', 'Artist')], [("What's It Gonna Be", 'Song'), ('Dangerously in Love', 'Album'), ('Beyoncé', 'Artist')], [('Higher Window', 'Song'), ('Illuminations', 'Album'), ('Josh Groban', 'Artist')], [("How's It Goin' Down", 'Song'), ("It's Dark and Hell Is Hot", 'Album'), ('DMX', 'Artist')], [('Choker', 'Song'), ('Scaled and Icy', 'Album'), ('Twenty One Pilots', 'Artist')], [('Back in the Day', 'Song'), ('Under Construction', 'Album'), ('Missy Elliott', 'Artist')], [('Hey Porsche', 'Song'), ('M.O.', 'Album'), ('Nelly', 'Artist')], [('Roller Coaster', 'Song'), ('Journals', 'Album'), ('Justin Bieber', 'Artist')], [('Front Back', 'Song'), ('King', 'Album'), ('T.I.', 'Artist')], [('Butterfly', 'Song'), ('Butterfly', 'Album'), ('Mariah Carey', 'Artist')], [('Blinding Lights', 'Song'), ('After Hours', 'Album'), ('The Weeknd', 'Artist')], [('Candy', 'Song'), ('Amala', 'Album'), ('Doja Cat', 'Artist')], [("Dell'amore non si sa", 'Song'), ('Andrea', 'Album'), ('Andrea Bocelli', 'Artist')], [('We Owned the Night', 'Song'), ('Own the Night', 'Album'), ('Lady A', 'Artist')], [('Waking Up in Vegas', 'Song'), ('One of the Boys', 'Album'), ('Katy Perry', 'Artist')], [('Regresa A Mí', 'Song'), ('Il Divo', 'Album'), ('Il Divo', 'Artist')], [('E.T.', 'Song'), ('Teenage Dream', 'Album'), ('Katy Perry', 'Artist')], [('I Want Tomorrow', 'Song'), ('Enya', 'Album'), ('Enya', 'Artist')], [('Stickwitu', 'Song'), ('PCD', 'Album'), ('The Pussycat Dolls', 'Artist')], [('Am I the Only One', 'Song'), ('Home', 'Album'), ('Dierks Bentley', 'Artist')], [('Godzilla', 'Song'), ('Music to Be Murdered By', 'Album'), ('Eminem', 'Artist')], [('Take Me Away', 'Song'), ('Stanley Climbfall', 'Album'), ('Lifehouse', 'Artist')], [('Here Without You', 'Song'), ('Away from the Sun', 'Album'), ('3 Doors Down', 'Artist')], [('I Wish I Was Crazy Again', 'Song'), ('I Would Like to See You Again', 'Album'), ('Johnny Cash', 'Artist')], [("P.D.A. (We Just Don't Care)", 'Song'), ('Once Again', 'Album'), ('John Legend', 'Artist')], [('Hey Baby', 'Song'), ('Full Frequency', 'Album'), ('Sean Paul', 'Artist')], [('Nobody but Me', 'Song'), ('Nobody but Me', 'Album'), ('Michael Bublé', 'Artist')], [('What About Now', 'Song'), ('Lonely Grill', 'Album'), ('Lonestar', 'Artist')], [('Vivere', 'Song'), ('The Best of Andrea Bocelli: Vivere', 'Album'), ('Andrea Bocelli', 'Artist')], [('Saturday (Oooh Oooh!)', 'Song'), ('Word of Mouf', 'Album'), ('Ludacris', 'Artist')], [("How I'm Feeling Now", 'Song'), ('Broken by Desire to Be Heavenly Sent', 'Album'), ('Lewis Capaldi', 'Artist')], [('Enough Cryin', 'Song'), ('The Breakthrough', 'Album'), ('Ashley Washington', 'Artist')], [('Let Yourself Go', 'Song'), ('Speedway', 'Album'), ('Elvis Presley', 'Artist')], [("Big Ol' Truck", 'Song'), ('Boomtown', 'Album'), ('Toby Keith', 'Artist')], [('Ignition (Remix)', 'Song'), ('Chocolate Factory', 'Album'), ('R. Kelly', 'Artist')], [('Breaking the Habit', 'Album'), ('Linkin Park', 'Artist')], [('Stuck with Me', 'Song'), ('Insomniac', 'Album'), ('Green Day', 'Artist')], [("I Can't Get Over You", 'Song'), ('If You See Her', 'Album'), ('Brooks & Dunn', 'Artist')], [("Don't Make Me Wait", 'Song'), ('44/876', 'Album'), ('Sting', 'Artist')], [('Beautiful People', 'Song'), ('No.6 Collaborations Project', 'Album'), ('Ed Sheeran', 'Artist')], [('Panic Station', 'Song'), ('The 2nd Law', 'Album'), ('Muse', 'Artist')], [("I Didn't Know My Own Strength", 'Song'), ('I Look to You', 'Album'), ('Whitney Houston', 'Artist')], [('Starboy', 'Song'), ('Starboy', 'Album'), ('The Weeknd', 'Artist')], [('Who Would Imagine a King', 'Song'), ("The Preacher's Wife - Original Soundtrack Album", 'Album'), ('Whitney Houston', 'Artist')], [('Mad As Rabbits', 'Song'), ('Pretty. Odd.', 'Album'), ('Panic! At The Disco', 'Artist')], [('Victim of Love', 'Song'), ('Victim of Love', 'Album'), ('Elton John', 'Artist')], [('What If I Never Get Over You', 'Song'), ('Ocean (Lady Antebellum album)', 'Album'), ('Lady A', 'Artist')], [('Rolling in the Deep', 'Song'), ('21', 'Album'), ('Adele', 'Artist')], [('Bad Blood', 'Song'), ('1989', 'Album'), ('Taylor Swift', 'Artist')], [('One', 'Song'), ('The Breakthrough', 'Album'), ('Ashley Washington', 'Artist')], [('There Goes My Life', 'Song'), ('When the Sun Goes Down', 'Album'), ('Kenny Chesney', 'Artist')], [('Roll On', 'Song'), ('Rock n Roll Jesus', 'Album'), ('Kid Rock', 'Artist')], [('The Masterplan', 'Song'), ('The Masterplan', 'Album'), ('Oasis', 'Artist')], [('Pardon Me', 'Song'), ('Make Yourself', 'Album'), ('Incubus', 'Artist')], [('Hold It Against Me', 'Song'), ('Femme Fatale', 'Album'), ('Britney Spears', 'Artist')], [('Serious', 'Song'), ('Love. Angel. Music. Baby.', 'Album'), ('Gwen Stefani', 'Artist')], [('The Best of BTS – Japan Edition', 'Album'), ('BTS', 'Artist')], [('Goodbye Town', 'Song'), ('Golden', 'Album'), ('Lady A', 'Artist')], [('Outside', 'Song'), ('Break the Cycle', 'Album'), ('Staind', 'Artist')], [('Come Over', 'Song'), ('I Care 4 U', 'Album'), ('Aaliyah', 'Artist')], [('Sexy Sadie', 'Song'), ('The Beatles', 'Album'), ('The Beatles', 'Artist')], [('Believe', 'Song'), ('Wilder Mind', 'Album'), ('Mumford & Sons', 'Artist')], [('I Hate This Part', 'Song'), ('Doll Domination', 'Album'), ('The Pussycat Dolls', 'Artist')], [('Wishing Well', 'Song'), ('Legends Never Die', 'Album'), ('Juice WRLD', 'Artist')], [('How to Rob', 'Song'), ('Power of the Dollar', 'Album'), ('50 Cent', 'Artist')], [('I Care', 'Song'), ('4', 'Album'), ('Beyoncé', 'Artist')], [('Southern Girl', 'Song'), ('Two Lanes of Freedom', 'Album'), ('Tim McGraw', 'Artist')], [('Bad!', 'Song'), ('Skins', 'Album'), ('XXXTentacion', 'Artist')], [('Black Summer', 'Song'), ('Unlimited Love', 'Album'), ('Red Hot Chili Peppers', 'Artist')], [('Sweet Sacrifice', 'Song'), ('The Open Door', 'Album'), ('Evanescence', 'Artist')], [('Missing', 'Song'), ('Anywhere but Home', 'Album'), ('Evanescence', 'Artist')], [("Chasin' You", 'Song'), ('If I Know Me', 'Album'), ('Morgan Wallen', 'Artist')], [('The Long Run', 'Song'), ('The Long Run', 'Album'), ('Eagles', 'Artist')], [('Nobody but You', 'Song'), ("Fully Loaded: God's Country", 'Album'), ('Blake Shelton', 'Artist')], [('Last Resort', 'Song'), ('Infest', 'Album'), ('Papa Roach', 'Artist')], [('Church Heathen', 'Song'), ('Intoxication', 'Album'), ('Shaggy', 'Artist')], [('More Like Her', 'Song'), ('Crazy Ex-Girlfriend', 'Album'), ('Miranda Lambert', 'Artist')], [('T-R-O-U-B-L-E', 'Song'), ('Today', 'Album'), ('Elvis Presley', 'Artist')], [('Use Somebody', 'Song'), ('Only by the Night', 'Album'), ('Kings of Leon', 'Artist')], [('My Heart Is Open', 'Song'), ('V', 'Album'), ('Maroon 5', 'Artist')], [('New Kid in Town', 'Song'), ('Hotel California', 'Album'), ('Eagles', 'Artist')], [('Nightmare', 'Song'), ('Manic', 'Album'), ('Halsey', 'Artist')], [("Let's Make Love", 'Song'), ('Breathe', 'Album'), ('Faith Hill', 'Artist')], [('Fly with Me', 'Song'), ('Lines, Vines and Trying Times', 'Album'), ('Jonas Brothers', 'Artist')], [('Stronger Than Me', 'Song'), ('Frank', 'Album'), ('Amy Winehouse', 'Artist')], [("Can't Get You Off My Mind", 'Song'), ('Circus', 'Album'), ('Lenny Kravitz', 'Artist')], [('Gasoline', 'Song'), ('Badlands', 'Album'), ('Halsey', 'Artist')], [('Talk Shows on Mute', 'Song'), ('A Crow Left of the Murder...', 'Album'), ('Incubus', 'Artist')], [('But I Will', 'Song'), ('Take Me as I Am', 'Album'), ('Faith Hill', 'Artist')], [('Never Never', 'Song'), ('The Paradigm Shift', 'Album'), ('Korn', 'Artist')], [('How Low', 'Song'), ('Battle of the Sexes', 'Album'), ('Ludacris', 'Artist')], [('Come Around', 'Song'), ('Who Do You Trust?', 'Album'), ('Papa Roach', 'Artist')]]

# In[ ]:

import pprint

#models = [m for m in palm.list_models()]
#model = models[0].name
#print(model)


# In[ ]:


import itertools
import llm
import time

import pprint

import pathlib
import textwrap

import google.generativeai as genai

#model = "models/chat-bison-001"

if (chosenLLM=="Falcon"):

    model = llm.get_model("ggml-model-gpt4all-falcon-q4_0")
elif (chosenLLM=="Llama2"):

    model = llm.get_model("llama-2-7b-chat")
elif (chosenLLM=="GPT3.5"):

    model = llm.get_model("gpt-3.5-turbo")
    model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
elif (chosenLLM=="Gemini"):

    genai.configure(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxx')
    model = genai.GenerativeModel('gemini-pro')
    

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
    
        if chosenDomain=="Places":
        
            parentNode = combo[1]
            childNode = combo[0]
            
            q1 = "Is there a " + childNode + " in " + parentNode + "?"
            q2 = "Does " + parentNode + " have a " + childNode + "?"
        elif chosenDomain=="Artists":
        
            parentNode = combo[1]
            childNode = combo[0]
            
            parentEntity = parentNode[1]
            childEntity = childNode[1]
            
            if (parentEntity=='Artist' and childEntity=="Album"):
                
                q1 = "Is \"" + childNode[0] + "\" an album by " + parentNode[0] + "?"
                q2 = "Does " + parentNode[0] + " have an album called \"" + childNode[0] + "\"?"
            elif (parentEntity=='Artist' and childEntity=="Song"):
                
                q1 = "Is \"" + childNode[0] + "\" a song by " + parentNode[0] + "?"
                q2 = "Does " + parentNode[0] + " have a song called \"" + childNode[0] + "\"?"
            elif (parentEntity=='Album' and childEntity=="Song"):
                
                q1 = "Is \"" + childNode[0] + "\" in the album, \"" + parentNode[0] + "\"?"
                q2 = "Does the album, \"" + parentNode[0] + "\" have a song called \"" + childNode[0] + "\"?"
        
        
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
                        
        elif (chosenLLM=="Gemini"):
        
            loopDone = False
            backoff = 0
            backOffCount = 0
            
            while(loopDone!=True):
                
                backOffCount = backOffCount + 1
                
                try:
                    
                    time.sleep(backoff)

                    chat1 = model.start_chat(history=[])
                    response1 = chat1.send_message(preAmble + q1,
                                    safety_settings=[
                                        {
                                            "category": "HARM_CATEGORY_HARASSMENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_HATE_SPEECH",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                    ],
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=0
                                    )
                                )

                    chat2 = model.start_chat(history=[])
                    response2 = chat2.send_message(preAmble + q2,
                                    safety_settings=[
                                        {
                                            "category": "HARM_CATEGORY_HARASSMENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_HATE_SPEECH",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                    ],
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=0
                                    )
                                )

                    loopDone = True
                
                except Exception as e:
                    
                    if (backOffCount==10):
                        
                        print(e)
                        break
                    elif (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2
        
        
        if (chosenLLM!="Gemini"):
        
            textResp1 = response1.text
            textResp2 = response2.text
            
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
elif (chosenLLM=="Gemini"):

    file1 = open("GeminiType1.txt", "w")
    file2 = open("GeminiType2.txt", "w")
            
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

import pathlib
import textwrap

import google.generativeai as genai

#model = "models/chat-bison-001"

if (chosenLLM=="Falcon"):

    model = llm.get_model("ggml-model-gpt4all-falcon-q4_0")
elif (chosenLLM=="Llama2"):

    model = llm.get_model("llama-2-7b-chat")
elif (chosenLLM=="GPT3.5"):

    model = llm.get_model("gpt-3.5-turbo")
    model.key = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
elif (chosenLLM=="Gemini"):

    genai.configure(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxx')
    model = genai.GenerativeModel('gemini-pro')


preAmble = "Be concise as possible. Answer with a yes or no response. "

list1 = []
list2 = []

for elemPath in foundPaths[:50]:
    
    combinations = list(itertools.combinations(elemPath, 2))
    
    for combo in combinations:
        
        if chosenDomain=="Places":
        
            parentNode = combo[1]
            childNode = combo[0]
            
            q1 = "Is there a " + childNode + " in " + parentNode + "?"
            q2 = "Does " + parentNode + " have a " + childNode + "?"
        elif chosenDomain=="Artists":
        
            parentNode = combo[1]
            childNode = combo[0]
            
            parentEntity = parentNode[1]
            childEntity = childNode[1]
            
            if (parentEntity=='Artist' and childEntity=="Album"):
                
                q1 = "Is \"" + childNode[0] + "\" an album by " + parentNode[0] + "?"
                q2 = "Does " + parentNode[0] + " have an album called \"" + childNode[0] + "\"?"
            elif (parentEntity=='Artist' and childEntity=="Song"):
                
                q1 = "Is \"" + childNode[0] + "\" a song by " + parentNode[0] + "?"
                q2 = "Does " + parentNode[0] + " have a song called \"" + childNode[0] + "\"?"
            elif (parentEntity=='Album' and childEntity=="Song"):
                
                q1 = "Is \"" + childNode[0] + "\" in the album, \"" + parentNode[0] + "\"?"
                q2 = "Does the album, \"" + parentNode[0] + "\" have a song called \"" + childNode[0] + "\"?"
        
        
        if (chosenLLM=="Llama2" or chosenLLM=="Falcon"):
        
            conversation1 = model.conversation()
            
            response1 = conversation1.prompt(preAmble + q1)
            textResp1 = response1.text()
            
            response2 = conversation1.prompt(preAmble + q2)
            textResp2 = response2.text()
        elif (chosenLLM=="Gemini"):
        
            loopDone = False
            backoff = 0
            backOffCount = 0
            
            while(loopDone!=True):
                
                backOffCount = backOffCount + 1
                
                try:
                    
                    time.sleep(backoff)

                    chat1 = model.start_chat(history=[])
                    response1 = chat1.send_message(preAmble + q1,
                                    safety_settings=[
                                        {
                                            "category": "HARM_CATEGORY_HARASSMENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_HATE_SPEECH",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                    ],
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=0
                                    )
                                )
                    
                    textResp1 = response1.text
                    
                    response2 = chat1.send_message(preAmble + q2,
                                    safety_settings=[
                                        {
                                            "category": "HARM_CATEGORY_HARASSMENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_HATE_SPEECH",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                    ],
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=0
                                    )
                                )
                    
                    textResp2 = response2.text

                    loopDone = True
                
                except Exception as e:
                    
                    if (backOffCount==10):
                        
                        print(e)
                        break
                    elif (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2

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
        elif (chosenLLM=="Gemini"):

            loopDone = False
            backoff = 0
            backOffCount = 0
            
            while(loopDone!=True):
                
                backOffCount = backOffCount + 1
                
                try:
                    
                    time.sleep(backoff)

                    chat2 = model.start_chat(history=[])
                    response1 = chat2.send_message(preAmble + q2,
                                    safety_settings=[
                                        {
                                            "category": "HARM_CATEGORY_HARASSMENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_HATE_SPEECH",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                    ],
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=0
                                    )
                                )
                    
                    textResp1 = response1.text
                    
                    response2 = chat2.send_message(preAmble + q1,
                                    safety_settings=[
                                        {
                                            "category": "HARM_CATEGORY_HARASSMENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_HATE_SPEECH",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                        {
                                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                                            "threshold": "BLOCK_NONE",
                                        },
                                    ],
                                    generation_config=genai.types.GenerationConfig(
                                        temperature=0
                                    )
                                )
                    
                    textResp2 = response2.text

                    loopDone = True
                
                except Exception as e:
                    
                    if (backOffCount==10):
                        
                        print(e)
                        break
                    elif (backoff==0):
                        
                        backoff = 1
                    else:
                        
                        backoff = backoff*2

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
elif (chosenLLM=="Gemini"):

    file1 = open("GeminiType12.txt", "w")
    file2 = open("GeminiType21.txt", "w")
            
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




