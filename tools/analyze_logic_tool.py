from template_logic.trainer import summarize_logic
from chains.logic_trainer_chain import get_logic_trainer_chain

def analyze_contract_logic(data: list) -> str:
    input_summary = summarize_logic(data)
    chain = get_logic_trainer_chain()
    result = chain.run(contract_data=input_summary)
    return result
