from app.ingestion.github_client import fetch_pr, fetch_pr_files

OWNER = "octocat"
REPO = "Hello-World"
PR_NUMBER = 1  # or real PR

def main():
    pr_data = fetch_pr(OWNER, REPO, PR_NUMBER)
    files = fetch_pr_files(OWNER, REPO, PR_NUMBER)

    print("\n=== PR INFO ===")
    print(pr_data)

    print("\n=== FILES ===")
    for file in files:
        print(file["filename"])
        print("Additions:", file["additions"])
        print("Deletions:", file["deletions"])
        print("Patch preview:", file["patch"][:200] if file["patch"] else "No patch")
        print("-" * 50)

if __name__ == "__main__":
    main()

    