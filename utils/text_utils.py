def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.strip()
    text = " ".join(text.split())
    return text

