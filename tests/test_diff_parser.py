import json
from app.diff_parser.parser import parse_patch
from app.ingestion.github_client import fetch_pr_files

OWNER = "fastapi"
REPO = "fastapi"
PR_NUMBER = 15025  


def main():
    files = fetch_pr_files(OWNER, REPO, PR_NUMBER)

    for file in files:
        if not file["patch"]:
            continue

        parsed = parse_patch(file["filename"], file["patch"])

        print("\n==== PARSED OUTPUT ====")
        print(json.dumps(parsed, indent=4))


if __name__ == "__main__":
    main()
