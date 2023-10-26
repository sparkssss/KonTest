import time
    
from bigtree import Node, tree_to_dot, print_tree, tree_to_nested_dict, nested_dict_to_tree
    
def recurseChild(parent, count, curTree):
    
    runQuery = True
    retry = False
    
    if count==3:
        
        return None
    
    else:
        
        while (runQuery):
    
            url = 'https://query.wikidata.org/sparql'
            headers = {'User-Agent': 'KGPlacesBuildBot/0.0 (anon@anon.com)'}
            
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


import pickle
import timeit

start = timeit.timeit()

initList = ['Q32', 'Q27', 'Q20', 'Q39', 'Q334', 'Q846', 'Q30', 'Q189', 'Q35', 'Q408']

for elemList in initList:
    
    root = Node(elemList)

    childNodes = recurseChild(elemList, 0, root)

    nestDict = tree_to_nested_dict(root, all_attrs=True)
    
    with open(elemList + '.pkl', 'wb') as file:
      
        # A new file will be created
        pickle.dump(nestDict, file)
        
end = timeit.timeit()

print("Time")
print(end - start)
    
#%%
