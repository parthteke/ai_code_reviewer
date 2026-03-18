import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def post_pr_comment(owner, repo, pr_number, comment):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "body": comment
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        raise Exception(f"Failed to post comment: {response.status_code} {response.text}")

    return response.json()