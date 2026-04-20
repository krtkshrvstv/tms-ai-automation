def summarize_logic(extracted_records: list) -> str:
    # For now, just join sample rows. Will be improved with actual logic
    return "\n".join(str(row) for row in extracted_records[:5])
