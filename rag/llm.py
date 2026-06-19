from langchain_ollama import ChatOllama


def get_model(llm,reasoning, max_tokens,temperature):
    
    model = ChatOllama(
    model=llm,
    reasoning=reasoning,
    num_predict=max_tokens,
    temperature=temperature)

    #force test to check if the model is installed
    model.invoke('hi')

    return model