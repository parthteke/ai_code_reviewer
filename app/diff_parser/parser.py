def parse_patch(filename: str, patch: str):
    if not patch:
        return None

    hunks = []
    current_hunk = None

    lines = patch.split("\n")

    for line in lines:
        if line.startswith("@@"):
            parts = line.split(" ")

            old_info = parts[1]  # -123,7
            new_info = parts[2]  # +123,9

            old_start = int(old_info.split(",")[0][1:])
            new_start = int(new_info.split(",")[0][1:])

            current_hunk = {
                "old_start": old_start,
                "new_start": new_start,
                "changes": []
            }
            hunks.append(current_hunk)

        elif current_hunk:
            if line.startswith("+") and not line.startswith("+++"):
                current_hunk["changes"].append({
                    "type": "added",
                    "content": line[1:]
                })
            elif line.startswith("-") and not line.startswith("---"):
                current_hunk["changes"].append({
                    "type": "removed",
                    "content": line[1:]
                })
            else:
                current_hunk["changes"].append({
                    "type": "context",
                    "content": line
                })

    return {
        "file": filename,
        "hunks": hunks
    }
