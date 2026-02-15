from ragas import evaluate
from datasets import Dataset

def evaluate_rag(questions, answers, contexts):
    dataset = Dataset.from_dict({
        "question": questions,
        "answer": answers,
        "contexts": contexts
    })

    result = evaluate(dataset)
    return result
