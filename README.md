# 🤖 AI Code Reviewer

An AI-powered tool that automatically reviews GitHub Pull Requests and posts structured feedback directly on the PR.

---

## 🚀 Overview

This project automates the code review process by analyzing pull request (PR) changes using a Large Language Model (LLM). It fetches code diffs from GitHub, evaluates them for potential issues, and posts review comments back to the PR.

The system is designed to simulate a developer-style review, identifying bugs, performance issues, security risks, and code quality improvements.

---

## 🎯 Features

* 🔍 Fetches PR files and diffs using GitHub API
* 🧠 AI-powered code analysis using LLaMA (via Groq)
* 📊 Structured output (bugs, performance, security, quality)
* ⚠️ Severity-based classification (HIGH / MEDIUM / LOW)
* 💬 Automatically posts comments on GitHub PRs
* ⚙️ GitHub Actions integration for automated reviews

---

## 🏗️ Architecture

```
GitHub Pull Request
        ↓
Fetch PR files (GitHub API)
        ↓
Extract & process code diffs
        ↓
Send to LLM (LLaMA via Groq)
        ↓
Generate structured review
        ↓
Post comment on PR
        ↓
Automated via GitHub Actions
```

---

## 🧰 Tech Stack

* Python
* GitHub REST API
* Groq API (LLaMA models)
* GitHub Actions (CI/CD)
* Requests library

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-code-reviewer.git
cd ai-code-reviewer
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set Environment Variables

```bash
export GITHUB_TOKEN=your_github_token
export GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the Project

```bash
python main.py <owner> <repo> <pr_number>
```

Example:

```bash
python main.py yourusername test-repo 1
```

---

## 🔄 GitHub Actions Automation

The project includes a GitHub Actions workflow that automatically runs the AI reviewer when a pull request is opened or updated.

Workflow file:

```
.github/workflows/ai-review.yml
```

---

## 📌 Example Output

```
🤖 AI Code Review

File
```
