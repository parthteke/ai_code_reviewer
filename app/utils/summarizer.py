def summarize_patch(patch, max_length=2000):
    if not patch:
        return ""

    if len(patch) <= max_length:
        return patch

    return patch[:max_length] + "\n...truncated..."