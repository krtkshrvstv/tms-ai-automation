import pandas as pd
import os

def read_contract_excel(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")
    
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"❌ File is empty: {file_path}")

    try:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        else:
            return pd.read_excel(file_path, engine="openpyxl")
    except Exception as e:
        raise ValueError(f"❌ Failed to read file {file_path}: {str(e)}")
