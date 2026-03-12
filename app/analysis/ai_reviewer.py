from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_changes(diff_summary):

    prompt = f"""
You are a senior code reviewer.

Analyze the following code changes.

Return ONLY valid JSON in this format:

{{
  "bugs": [],
  "performance_issues": [],
  "security_risks": [],
  "code_quality_improvements": [],
  "summary": ""
}}

Code changes:
{diff_summary}
"""


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a strict senior code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content