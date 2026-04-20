import argparse
from tools.read_excel_tool import read_contract_excel
from tools.analyze_logic_tool import analyze_contract_logic
from tools.generate_templates_tool import generate_template
from utils.file_utils import save_output

def main():
    parser = argparse.ArgumentParser(description="Run Template Generator from Excel contract.")
    parser.add_argument("--file", type=str, required=True, help="Path to contract Excel file.")
    parser.add_argument("--output", type=str, default="generated_template.txt", help="Output file name.")
    args = parser.parse_args()

    print("🚚 Running Logistics Template Generator...")

    # Step 1: Read
    data = read_contract_excel(args.file)
    print(f"📄 Read {len(data)} records from {args.file}")

    # Step 2: Analyze logic
    logic_summary = analyze_contract_logic(data)
    print(f"🧠 Derived logic:\n{logic_summary[:300]}...\n")

    # Step 3: Generate template
    generated = generate_template(data, logic_summary)
    output_path = save_output(generated, args.output)

    print(f"✅ Template saved to: {output_path}")

if __name__ == "__main__":
    main()
