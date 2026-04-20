from langchain.prompts import PromptTemplate
from config.ollama_chain import build_chain

def get_template_generator_chain():
    template = """
    Using the logic rules below, generate a logistics template
    for the following new contract data.

    LOGIC RULES:
    {logic_summary}

    NEW CONTRACT:
    {new_contract}

    Return a CSV-compatible structure or JSON.
    """
    prompt = PromptTemplate(
        input_variables=["logic_summary", "new_contract"],
        template=template
    )
    return build_chain(prompt)
