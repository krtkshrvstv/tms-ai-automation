from langchain.prompts import PromptTemplate
from config.ollama_chain import build_chain

def get_logic_trainer_chain():
    template = """
    Analyze the following contract data and derive patterns, logic rules,
    and relationships. Return a structured summary.

    CONTRACT DATA:
    {contract_data}
    """
    prompt = PromptTemplate(
        input_variables=["contract_data"],
        template=template
    )
    return build_chain(prompt)
  
