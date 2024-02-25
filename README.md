# KonTest
Replication Package for KonTest

KonTest is an automated testing framework for evaluating the consistency of large language models (LLMs). It leverages an external knowledge base to craft queries to a target LLM and identifies both metamorphic and ontological errors in the LLM's output.

## Requirements

### Python Packages Required

* time
* bigtree
* pickle
* timeit
* random
* pprint
* itertools
* llm
* math
* networkx
* copy
* pathlib
* textwrap

### LLM Specific Packages

#### Google Gemini

```
import google.generativeai as genai
```

Note: Credentials cannot be embedded in code. A service key is required.
It can be created using GCP by following the linked procedure.

Link: [Gemini Credentials](https://aistudio.google.com/app/apikey)

#### OpenAI GPT3.5


Note: Credentials cannot be embedded in code. A service key is required.
It can be created at the OpenAI website.

Link: [OpenAI Website](https://openai.com/)

#### Falcon and Llama2

```
llm install llm-gpt4all
```

Note: The models need to be installed prior to usage. Full documentation is available below.

Link: [LLM Documentation](https://llm.datasette.io/en/stable/other-models.html)


## Usage

The code consists of 2 sections, Knowledge Base Generation and LLM Query.

##### kgConstruct.py

It constructs the knowledge base for the selected list of countries.

##### gitQueryCopy.py

Queries the LLM and finds the number of errors for the selected target LLM.
