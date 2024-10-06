import pprint

import itertools
import llm
import time

import pprint

import pathlib
import textwrap

import google.generativeai as genai

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
        
    if words.startswith('chosenLLM'):
        
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
        
        chosenLLM = resWords[0]
        
fConfig.close()

########################################################################################################
#Code block below contains the keys for the different LLMs
########################################################################################################


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

########################################################################################################
#Code block below generates the atomic queries with the chosen LLM
########################################################################################################

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
        elif chosenDomain=="Music":
        
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

########################################################################################################
#Code block below generates the sequential queries with the chosen LLM
########################################################################################################

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
        elif chosenDomain=="Music":
        
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
