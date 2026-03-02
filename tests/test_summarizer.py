import json
from app.ingestion.github_client import fetch_pr_files
from app.diff_parser.parser import parse_patch
from app.analysis.change_summarizer import summarize_changes

OWNER = "fastapi"
REPO = "fastapi"
PR_NUMBER = 15025  # real PR number


def main():
    files = fetch_pr_files(OWNER, REPO, PR_NUMBER)

    for file in files:
        if not file["patch"]:
            continue

        parsed = parse_patch(file["filename"], file["patch"])
        summarized = summarize_changes(parsed)

        print("\n==== SUMMARIZED OUTPUT ====")
        print(json.dumps(summarized, indent=4))


if __name__ == "__main__":
    main()

    
