# KonTest
Replication Package for Knowledge-based Consistency Testing of Large Language Models

![KonTest Overview](overview-approach.png)

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

## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Citing KonTest

'''
@inproceedings{rajan2024knowledge,
  title={Knowledge-based Consistency Testing of Large Language Models},
  author={Rajan, Sai Sathiesh and Soremekun, Ezekiel and Chattopadhyay, Sudipta},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2024},
  year={2024}
}
'''
