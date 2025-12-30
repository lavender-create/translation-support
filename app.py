from flask import Flask, render_template, request

from utils.text_utils import clean_text
from services.llm_client import call_llm
from services.llm_prompts import (
    TRANSLATE_PROMPT,
    SUMMARY_PROMPT,
    INTENT_PROMPT,
    SUMMARY_PROMPT_EN,
    INTENT_PROMPT_EN,
)

app = Flask(__name__)


def is_english_text(text: str) -> bool:
    """
    簡易的な言語判定
    英語のみ（ASCII）で構成されていれば True
    """
    try:
        return text.encode("utf-8").isascii()
    except Exception:
        return False


@app.route("/", methods=["GET", "POST"])
def index():
    input_text = ""
    translation = ""
    summary = ""
    intent = ""

    if request.method == "POST":
        raw_text = request.form.get("text", "")
        input_text = clean_text(raw_text)

        if input_text:
            # ① 翻訳（双方向・強制）
            prompt_t = TRANSLATE_PROMPT.format(text=input_text)
            translation = call_llm(prompt_t)

            # ② 翻訳結果の言語判定
            is_en = is_english_text(translation)

            # ③ 要約（言語切替）
            if is_en:
                prompt_s = SUMMARY_PROMPT_EN.format(text=translation)
            else:
                prompt_s = SUMMARY_PROMPT.format(text=translation)
            summary = call_llm(prompt_s)

            # ④ 意図解析（言語切替）
            if is_en:
                prompt_i = INTENT_PROMPT_EN.format(text=translation)
            else:
                prompt_i = INTENT_PROMPT.format(text=translation)
            intent = call_llm(prompt_i)

    return render_template(
        "index.html",
        input_text=input_text,
        translation=translation,
        summary=summary,
        intent=intent,
    )


if __name__ == "__main__":
    app.run(debug=True)






