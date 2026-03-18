from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_changes(diff_summary):

    prompt = f"""
You are a senior software engineer reviewing a pull request.

Analyze the code changes and return issues in this format:

HIGH:
- ...

MEDIUM:
- ...

LOW:
- ...

Also include:
SUMMARY:
- ...

Code:
{diff_summary}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a strict code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content