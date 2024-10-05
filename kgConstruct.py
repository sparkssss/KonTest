#Specify the list of initial nodes

#Domain considered by KonTest (Choose between "Places" and "Music")
domainName = "Places"

#List of countries used by KonTest
initList = ['Q32', 'Q27', 'Q20', 'Q39', 'Q334', 'Q846', 'Q30', 'Q189', 'Q35', 'Q408']

#List of Musical Acts used by KonTest
#initList = ['Q26876','Q5608','Q33240','Q47447','Q160009','Q2121062','Q23215','Q45188','Q36844','Q261','Q36153','Q21621919','Q483802','Q11975','Q182223','Q2831','Q134541','Q467526','Q356487','Q10708','Q29564107','Q1450','Q559819','Q153694','Q15935','Q483507','Q34086','Q23884740','Q15862','Q391348','Q29561472','Q121507','Q3626966','Q165911','Q1299','Q1744','Q19848','Q52151598','Q753598','Q130798','Q153056','Q43432','Q151892','Q30449','Q4235','Q549981','Q42493','Q41076','Q47875','Q6060','Q218992','Q5105','Q47871','Q106648','Q41594','Q396','Q315547','Q155700','Q40715','Q2808','Q380927','Q215546','Q366584','Q62766','Q259254','Q21914464','Q175097','Q483718','Q34424','Q273055','Q44333953','Q220730','Q13605596','Q308816','Q94831','Q18233','Q80424','Q215215','Q195439','Q63243883','Q142636','Q15897','Q228909','Q158175','Q47122','Q202550','Q39639','Q297097','Q15123969','Q131433','Q218083','Q11895','Q472595','Q28561969','Q166197','Q204018','Q5108148','Q182655','Q16210722','Q303','Q464241','Q37150','Q1777698','Q50527563','Q15615','Q42402','Q170599','Q130799','Q409','Q6405079','Q485811','Q51120673','Q240767','Q1225','Q23771950','Q17140','Q200577','Q3445057','Q7857806','Q139154','Q146027','Q482444','Q193676','Q15920','Q482477','Q162202','Q34389','Q154454','Q17198340','Q27593','Q11036','Q873384','Q382890','Q81698554','Q11998','Q236549','Q189991','Q483379','Q282531','Q42315001','Q32849','Q28816483','Q22151','Q36490532','Q6107','Q78754352','Q1438730','Q180224','Q38257','Q131366','Q13580495','Q266496','Q277551','Q192486','Q161877','Q929683','Q155079','Q3644642','Q214227','Q34584','Q953918','Q102385','Q45165','Q389870','Q14045','Q181484','Q1869293','Q256732','Q617932','Q11617','Q188407','Q189635','Q43259','Q80304','Q11649','Q832086','Q1200415','Q193710','Q200586','Q25177','Q1661036','Q168992','Q154222','Q44857','Q5383','Q845790','Q483203','Q254371','Q309843','Q464749','Q2306','Q42775','Q231233','Q134233','Q151241','Q2331','Q18534249','Q310763','Q269813','Q223769']


import time
    
from bigtree import Node, tree_to_dot, print_tree, tree_to_nested_dict, nested_dict_to_tree


#Function for building KG of Places as in KonTest

def recurseChild_Places(parent, count, curTree):
    
    runQuery = True
    retry = False
    
    if count==3:
        
        return None
    
    else:
        
        while (runQuery):
    
            url = 'https://query.wikidata.org/sparql'
            headers = {'User-Agent': 'KGPlacesBuildBot/0.0 (anon@anon.com)'}

            #Entity specific Queries using SPARQL
            query = """
            SELECT DISTINCT
              ?country ?countryLabel WHERE {
              hint:Query hint:optimizer "None".
              ?country wdt:P131 wd:""" + parent + """.
              ?country wdt:P31/wdt:P279* wd:Q56061.
              FILTER NOT EXISTS {?country wdt:P576 ?abolished}
              SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
            }
            group by ?country ?countryLabel
            """
            r = requests.get(url, headers=headers, params = {'format': 'json', 'query': query})
            
            if (r.status_code == 200):
                
                retry = False
                
                data = r.json()
                
                #counter = 0
                
                for elem in data['results']['bindings']:
                    
                    #counter = counter + 1
                    
                    entityVal = elem['country']['value']
                    new_string = entityVal.removeprefix("http://www.wikidata.org/entity/")
                    #print(new_string)
                    
                    entityName = elem['countryLabel']['value']
                    
                    #print(entityName)
                    
                    if entityName!=new_string:
                        
                        curChild = Node(new_string, parent=curTree)
                    
                        recurseChild(new_string, count+1, curChild)
                    else:
                        
                        return None
                    
            elif (r.status_code == 429):
                
                time.sleep(int(r.headers["Retry-After"]))
                print(int(r.headers["Retry-After"]))
                retry = True
                    
            else:
                #print("Error from server: " + str(r.content))
                
                retry = False
                
                pass
        
            if (retry==True):
                
                runQuery = True
                
            else:
                
                runQuery = False
            
        return None

#Function for building KG of Music as in KonTest
    
def recurseChild_Music(parent, count, curTree):
    
    runQuery = True
    retry = False
    
    if count==2:
        
        return None
    
    elif count==0:
        
        while (runQuery):
    
            url = 'https://query.wikidata.org/sparql'
            headers = {'User-Agent': 'KGPlacesBuildBot/0.0 (anon@anon.com)'}
            
            query = """

            SELECT DISTINCT

              ?album ?albumLabel WHERE {

              hint:Query hint:optimizer "None".

              ?album wdt:P175 wd:""" + parent + """.

              ?album wdt:P31/wdt:P279* wd:Q482994.

              SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }

            }

            group by ?album ?albumLabel

            """
            r = requests.get(url, headers=headers, params = {'format': 'json', 'query': query})
            
            if (r.status_code == 200):
                
                retry = False
                
                data = r.json()
                
                #counter = 0
                
                for elem in data['results']['bindings']:
                    
                    #counter = counter + 1
                    
                    entityVal = elem['album']['value']
                    new_string = entityVal.removeprefix("http://www.wikidata.org/entity/")
                    #print(new_string)
                    
                    entityName = elem['albumLabel']['value']
                    
                    #print(entityName)
                    
                    if entityName!=new_string:
                        
                        curChild = Node((new_string, "Album"), parent=curTree)
                    
                        recurseChild(new_string, count+1, curChild)
                    else:
                        
                        return None
                    
            elif (r.status_code == 429):
                
                time.sleep(int(r.headers["Retry-After"]))
                print(int(r.headers["Retry-After"]))
                retry = True
                    
            else:
                #print("Error from server: " + str(r.content))
                
                retry = False
                
                pass
        
            if (retry==True):
                
                runQuery = True
                
            else:
                
                runQuery = False
            
        return None
    
    elif count==1:
        
        while (runQuery):
    
            url = 'https://query.wikidata.org/sparql'
            headers = {'User-Agent': 'KGPlacesBuildBot/0.0 (anon@anon.com)'}
            
            query = """
            SELECT DISTINCT
              ?song ?songLabel WHERE {

              VALUES ?songTypes { wd:Q134556 wd:Q2188189 }
              hint:Query hint:optimizer "None".

              ?song wdt:P361 wd:""" + parent + """.

              ?song wdt:P31/wdt:P279* ?songTypes.
              SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
            }

            group by ?song ?songLabel
            """
            r = requests.get(url, headers=headers, params = {'format': 'json', 'query': query})
            
            if (r.status_code == 200):
                
                retry = False
                
                data = r.json()
                
                #counter = 0
                
                for elem in data['results']['bindings']:
                    
                    #counter = counter + 1
                    
                    entityVal = elem['song']['value']
                    new_string = entityVal.removeprefix("http://www.wikidata.org/entity/")
                    #print(new_string)
                    
                    entityName = elem['songLabel']['value']
                    
                    #print(entityName)
                    
                    if entityName!=new_string:
                        
                        curChild = Node((new_string, "Song"), parent=curTree)
                    
                        recurseChild(new_string, count+1, curChild)
                    else:
                        
                        return None
                    
            elif (r.status_code == 429):
                
                time.sleep(int(r.headers["Retry-After"]))
                print(int(r.headers["Retry-After"]))
                retry = True
                    
            else:
                #print("Error from server: " + str(r.content))
                
                retry = False
                
                pass
        
            if (retry==True):
                
                runQuery = True
                
            else:
                
                runQuery = False
            
        return None


import pickle

if domainName == "Places":

    for elemList in initList:
        
        root = Node(elemList)

        childNodes = recurseChild_Places(elemList, 0, root)

        nestDict = tree_to_nested_dict(root, all_attrs=True)
        
        with open(elemList + '.pkl', 'wb') as file:
          
            # A new file will be created
            pickle.dump(nestDict, file)

elif domainName == "Music":
            
    for elemList in initList:
        
        root = Node((elemList, "Artist"))

        childNodes = recurseChild_Music(elemList, 0, root)

        nestDict = tree_to_nested_dict(root, all_attrs=True)
        
        with open('ArtistsKG/' + elemList + '.pkl', 'wb') as file:
          
            # A new file will be created
            pickle.dump(nestDict, file)
