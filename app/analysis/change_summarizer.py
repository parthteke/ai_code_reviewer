def summarize_changes(parsed_patch):
    if not parsed_patch:
        return None

    summary = {
        "file": parsed_patch["file"],
        "total_additions": 0,
        "total_deletions": 0,
        "changes": []
    }

    for hunk in parsed_patch["hunks"]:
        current_line = hunk["new_start"]

        removed_buffer = []

        for change in hunk["changes"]:
            if change["type"] == "removed":
                summary["total_deletions"] += 1
                removed_buffer.append(change["content"])

            elif change["type"] == "added":
                summary["total_additions"] += 1

                removed_line = removed_buffer.pop(0) if removed_buffer else None

                summary["changes"].append({
                    "line_number": current_line,
                    "added": change["content"],
                    "removed": removed_line
                })

                current_line += 1

            elif change["type"] == "context":
                current_line += 1

    return summary
