# LLM output evaluation with Langchain and watsonx

## Overview

This repo shows how to leverage large language models running on IBM watsonx to assess generative AI outputs.

It includes three notebooks:

* The [first one](1.criteria_eval_chain.ipynb) is an introduction to the Lanchain Criteria Evaluation framework and its integration with IBM watsonx
* The other two provide a sample implementation of how to evaluate different aspects of a RAG (Retrieval Augmented Generation) solution. They rely on utility classes that simplify the setup described in the introductory notebook and support the parallel evaluation of multiple records.

## Initial Setup

If you have not used watsonx before please refer to the documentation you find [here](https://www.ibm.com/products/watsonx-ai) to setup a free trial environment.

If you already have access to an environment, follow the steps below:

* Create and .env file with the keys listed in .env-sample. Populate the values with your credentials and watsonx project details.
* Create a virtual python environmnet

  ```
  python3 -m venv venv
  ```
* Activate the environment and install dependencies

  ```
  source venv/bin/activate
  pip install -r requirements.txt --no-cache
  ```
* Associate the notebooks to the python kernel of the virtual environment created above
