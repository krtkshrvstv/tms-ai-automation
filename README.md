# AI Pipeline for TMS Data Automation

## Problem
Manual processing of logistics data into structured templates took 2–3 hours per dataset and was highly error-prone, especially for large datasets (1000+ rows).

## Solution
Built an AI-assisted pipeline that:
- Learns transformation logic from sample templates
- Generates Python code for deterministic execution
- Automatically converts raw data into structured formats

## How It Works
1. Input: Raw Excel dataset + sample structured template  
2. LLM infers transformation logic  
3. Python code is generated/executed  
4. Outputs: 6 structured templates (rates, lanes, etc.)

## Tech Stack
- Python
- Pandas
- LangChain
- Ollama (local LLM)

## Results
- 3 hours → under 2 minutes  
- Handles 1000+ rows  
- Eliminates manual errors  

## How to Run
```bash
pip install -r requirements.txt
python main.py
