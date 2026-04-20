from langchain_community.llms    import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def get_ollama_model(model_name="llama3.2"):
    return Ollama(model=model_name)

def build_chain(prompt_template: PromptTemplate):
    llm = get_ollama_model()
    return LLMChain(llm=llm, prompt=prompt_template)