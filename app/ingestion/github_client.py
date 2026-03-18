import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_pr_files(owner, repo, pr_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error fetching PR files: {response.status_code} {response.text}")

    return response.json()