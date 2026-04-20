import os
from tools.read_excel_tool import read_contract_excel
from tools.analyze_logic_tool import analyze_contract_logic
from tools.generate_templates_tool import generate_template
from utils.file_utils import save_output

def test_template_generation():
    test_file = "data/sample_contract.xlsx"
    if not os.path.exists(test_file):
        raise FileNotFoundError(f"{test_file} not found. Add a sample Excel sheet to `data/`.")

    data = read_contract_excel(test_file)
    assert isinstance(data, list) and len(data) > 0, "Contract data should be a non-empty list."

    logic_summary = analyze_contract_logic(data)
    assert logic_summary and isinstance(logic_summary, str), "Logic summary must be a string."

    template = generate_template(data, logic_summary)
    assert "Tariff ID" in template or "RateCode" in template, "Generated template should contain expected fields."

    output_file = save_output(template, "test_template_output.txt")
    assert os.path.exists(output_file), "Output file was not saved successfully."

    print("✅ Template generation test passed.")
