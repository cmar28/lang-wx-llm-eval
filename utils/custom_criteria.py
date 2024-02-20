

class CustomCriteria():
    
    RETRIEVAL_RELEVANCE = {
        "relevance": "Does the submission explicitely answer the question of the input? Base your step by step reasoning only on the submission, do not include any inference."
    }

    RAG_COHERENCE = {
        "coherence": "Does the submission addresses the question of the input, using only information available from the reference? If the reference doesn't contains information relevant for the input the submission must not provide an answer."
    }

