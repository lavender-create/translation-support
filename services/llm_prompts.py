# =========================
# 翻訳プロンプト（双方向・強制）
# =========================
TRANSLATE_PROMPT = """
あなたは業務向けの翻訳アシスタントです。
入力文の言語を自動判定し、必ず次のルールで翻訳してください。

【ルール】
- 入力が日本語 → 出力は英語（英文のみ）
- 入力が英語 → 出力は日本語（日本語のみ）
- 出力は「翻訳文のみ」。説明・前置き・注釈は禁止。
- 直訳ではなく、自然で丁寧な業務表現にする。

【例1】
入力: 今日はどうされましたか？
出力: How can I help you today?

【例2】
入力: Could you confirm the schedule?
出力: スケジュールをご確認いただけますか？

文章:
{text}
"""


# =========================
# 要約プロンプト（日本語）
# =========================
SUMMARY_PROMPT = """
あなたは業務向けアシスタントです。
次の文章を日本語で、重要なポイントだけを
3行以内で簡潔に要約してください。

前置きや挨拶は不要です。

文章:
{text}
"""


# =========================
# 意図解析プロンプト（日本語）
# =========================
INTENT_PROMPT = """\
次の文章の意図を分析してください。
以下の観点で整理してください。

・種類（質問／確認／依頼／要望／提案／連絡／情報提供／意見／同意／拒否／感謝／謝罪／苦情／雑談 など）
・重要度（高／中／低）
・対応の要否（要／不要）

文章:
{text}
"""


# =========================
# 要約プロンプト（英語）
# =========================
SUMMARY_PROMPT_EN = """
You are a business assistant.
Summarize the following text in English, focusing only on key points.
Limit the summary to a maximum of 3 lines.

Do not add greetings or prefaces.

Text:
{text}
"""


# =========================
# 意図解析プロンプト（英語）
# =========================
INTENT_PROMPT_EN = """
You are a business document analyst.
Analyze the following text and respond in the format below.

- Type: (Question / Request / Information)
- Priority: (High / Medium / Low)
- Action Required: (Yes / No)

Text:
{text}
"""





