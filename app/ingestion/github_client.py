import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def fetch_pr(owner: str, repo: str, pr_number: int):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Error fetching PR: {response.status_code} {response.text}")

    pr = response.json()

    return {
        "title": pr.get("title"),
        "description": pr.get("body"),
        "author": pr.get("user", {}).get("login"),
        "base_branch": pr.get("base", {}).get("ref"),
        "head_branch": pr.get("head", {}).get("ref")
    }


def fetch_pr_files(owner: str, repo: str, pr_number: int):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Error fetching PR files: {response.status_code} {response.text}")

    files = response.json()

    structured_files = []

    for file in files:
        structured_files.append({
            "filename": file.get("filename"),
            "status": file.get("status"),
            "additions": file.get("additions"),
            "deletions": file.get("deletions"),
            "patch": file.get("patch")
        })

    return structured_files

