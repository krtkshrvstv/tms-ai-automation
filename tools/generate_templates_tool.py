from template_logic.generator import generate_all_templates

def generate_template(data: list, logic_summary: str) -> str:
    import pandas as pd

    df = pd.DataFrame(data)
    template_paths = generate_all_templates(df)
    return f"✅ Generated templates:\n" + "\n".join(f"- {k}: {v}" for k, v in template_paths.items())
