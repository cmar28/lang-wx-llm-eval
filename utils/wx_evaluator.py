from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes
from langchain.evaluation import load_evaluator as lang_load_evaluator
from langchain.evaluation import EvaluatorType
from langchain.evaluation import Criteria
from utils.prompt import OS_PROMPT, OS_PROMPT_WITH_REFERENCES
from utils.custom_criteria import CustomCriteria
import logging


class wx_EvalFactory():

    def __init__(self, credentials,project_id):
        model_id = "ibm-mistralai/mixtral-8x7b-instruct-v01-q"
        #model_id = ModelTypes.LLAMA_2_70B_CHAT
        generate_params = {
            #customise model parameters here
            GenParams.MAX_NEW_TOKENS: 4096,
            GenParams.STOP_SEQUENCES: ["Answer: Y","Answer: N"],
        }
        model = Model(
            model_id=model_id,
            credentials=credentials,
            params=generate_params,
            project_id=project_id,
        )
        self.llm = WatsonxLLM(model=model)

    
    def load_evaluator(self, criteria):
        logging.debug(f"creating evaluator for criteria: {criteria}")
        type = None
        if criteria in [Criteria.CONCISENESS,
                        Criteria.RELEVANCE,
                        CustomCriteria.RETRIEVAL_RELEVANCE,
                        ]:
            type = EvaluatorType.CRITERIA
            template = OS_PROMPT
        elif criteria in [Criteria.CORRECTNESS,
                          CustomCriteria.RAG_COHERENCE,
                         ]:
            type=EvaluatorType.LABELED_CRITERIA
            template = OS_PROMPT_WITH_REFERENCES
        if type!=None:
            return lang_load_evaluator(type,llm=self.llm,prompt=template,criteria=criteria)
        else:
            raise Exception("Evaluation criteria not supported")
        
