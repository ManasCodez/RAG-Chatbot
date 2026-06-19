from langchain_ollama import ChatOllama


def get_model(reasoning, max_tokens,temperature):
    
    model = ChatOllama(
    model="qwen3:8b",
    reasoning=reasoning,
    num_predict=max_tokens,
    temperature=temperature)

    return model