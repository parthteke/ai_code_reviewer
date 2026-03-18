def format_review(file_name, review_text):
    return f"""
## 🤖 AI Code Review

### 📄 File: {file_name}

{review_text}

---
Generated automatically by AI Reviewer
"""