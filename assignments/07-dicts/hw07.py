def word_counts(text: str) -> dict[str, int]:
    raise NotImplementedError


def unique_sorted(xs: list[int]) -> list[int]:
    raise NotImplementedError


def group_by_value(d: dict[str, int]) -> dict[int, list[str]]:
    raise NotImplementedError


# This function is supposed to return the most common word in `text`, but it has a bug.
# Write a test that exposes the bug, then fix it. Explain the bug in AI_LOG.md.
def most_common_word(text: str) -> str:
    counts = word_counts(text)
    best = ""
    for word in counts:
        if counts[word] > counts.get(best, 0):
            best = word
        return best
    return best
