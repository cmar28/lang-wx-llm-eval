from langchain_core.prompts import PromptTemplate

template = """<s>[INST]<<SYS>> You are a criteria evaluator assessing whether a submission, based on an input, is compliant with a set of criteria. 
Your output includes a step by step reasoning and an overall answer, in the following format:

Step by step reasoning: <Does the submission meet the Criteria? Write out in a step by step manner your reasoning about each criterion to be sure that your conclusion is correct>

Answer:  <a single character "Y" or "N" (without quotes or punctuation). "Y" if the submission meets all the criteria, "N" if the submission doesn't meet one or more of the criteria.>
<</SYS>>

[Input]: {input}

[Submission]: {output}

[Criteria]: {criteria}

Respond only with "Step by step reasoning" and "Answer"
[/INST] """

OS_PROMPT = PromptTemplate(
    input_variables=["input", "output", "criteria"], template=template
)

template = """<s>[INST]<<SYS>> You are a criteria evaluator assessing whether a submission, based on an input, is compliant with a set of criteria. Base your answer only on the reference data provided.
Your output includes a step by step reasoning and an overall answer, in the following format:

Step by step reasoning: <Does the submission meet the Criteria, on the basis of the reference? Write out in a step by step manner your reasoning about each criterion to be sure that your conclusion is correct>

Answer: <a single character "Y" or "N" (without quotes or punctuation), based on the step by step reasoning>
<</SYS>>

[Input]: {input}

[Submission]: {output}

[Criteria]: {criteria}

[Reference]: {reference}

Respond only with "Step by step reasoning" and "Answer". Do not add anything else.
[/INST] """

OS_PROMPT_WITH_REFERENCES = PromptTemplate(
    input_variables=["input", "output", "criteria", "reference"], template=template
)