from dotenv import load_dotenv
load_dotenv()

import sys
from app.ingestion.github_client import fetch_pr_files
from app.analysis.ai_reviewer import review_changes
from app.ingestion.github_pr_review import post_pr_comment
from app.utils.formatter import format_review
from app.utils.summarizer import summarize_patch


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <owner> <repo> <pr_number>")
        return

    owner = sys.argv[1]
    repo = sys.argv[2]
    pr_number = sys.argv[3]

    print("Fetching PR files...")
    files = fetch_pr_files(owner, repo, pr_number)

    for file in files:
        if "patch" not in file:
            continue

        print(f"Reviewing file: {file['filename']}")

        patch = summarize_patch(file["patch"])
        review = review_changes(patch)

        comment = format_review(file["filename"], review)

        post_pr_comment(owner, repo, pr_number, comment)

    print("Review comments posted successfully.")


if __name__ == "__main__":
    main()