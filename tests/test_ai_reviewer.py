import json
from app.ingestion.github_client import fetch_pr_files
from app.diff_parser.parser import parse_patch
from app.analysis.change_summarizer import summarize_changes
from app.analysis.ai_reviewer import review_changes

OWNER = "fastapi"
REPO = "fastapi"
PR_NUMBER = 1  # real PR


def main():
    files = fetch_pr_files(OWNER, REPO, PR_NUMBER)

    for file in files:
        if not file["patch"]:
            continue

        parsed = parse_patch(file["filename"], file["patch"])
        summarized = summarize_changes(parsed)

        result = review_changes(summarized)

        print("\n==== AI REVIEW RESULT ====")
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()