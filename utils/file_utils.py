import os
from pathlib import Path

def save_output(content: str, filename: str, directory: str = "output") -> str:
    """
    Saves the content to a file in the specified directory.
    Creates the directory if it doesn't exist.

    Returns the full path to the saved file.
    """
    output_path = Path(directory)
    output_path.mkdir(parents=True, exist_ok=True)

    full_path = output_path / filename
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

    return str(full_path)

def load_file_as_string(filepath: str) -> str:
    """
    Loads and returns the contents of a text file as a string.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()
