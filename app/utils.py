import re

def clean_response(raw_response: str) -> str:
    return re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL).strip()

def final_response_logic(cleaned: str) -> str:
    if "i don't know" in cleaned.lower() or "cannot answer" in cleaned.lower():
        return "I don't know.\nI couldn’t find information about this. You might try rephrasing your question."

    return cleaned
